#!/usr/bin/env python3
"""Generate Flyway SQL to upsert full Korean legal-district master from korean_bcd.json."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "src/backend/src/main/resources/data/korean_bcd.json"
OUTPUT_FILE = ROOT / "src/backend/src/main/resources/db/migration/V163__seed_korean_regions_full.sql"

SIDO_ORDER = {
    "11": 1,
    "26": 2,
    "27": 3,
    "28": 4,
    "29": 5,
    "30": 6,
    "31": 7,
    "36": 8,
    "41": 9,
    "42": 10,
    "43": 11,
    "44": 12,
    "45": 13,
    "46": 14,
    "47": 15,
    "48": 16,
    "50": 17,
}

SIDO_ENG = {
    "11": "Seoul",
    "26": "Busan",
    "27": "Daegu",
    "28": "Incheon",
    "29": "Gwangju",
    "30": "Daejeon",
    "31": "Ulsan",
    "36": "Sejong",
    "41": "Gyeonggi",
    "42": "Gangwon",
    "43": "Chungbuk",
    "44": "Chungnam",
    "45": "Jeonbuk",
    "46": "Jeonnam",
    "47": "Gyeongbuk",
    "48": "Gyeongnam",
    "50": "Jeju",
}


def sql_literal(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def infer_dong_type(name: str) -> str:
    if name.endswith("리"):
        return "RI"
    if name.endswith("면"):
        return "MYUN"
    if name.endswith("읍"):
        return "EUP"
    return "DONG"


def chunk(values: list[str], size: int) -> list[list[str]]:
    return [values[index : index + size] for index in range(0, len(values), size)]


def main() -> None:
    rows = json.loads(DATA_FILE.read_text(encoding="utf-8"))

    sidos: dict[str, str] = {}
    sigungus: dict[str, tuple[str, str]] = {}
    dongs: list[tuple[str, str, str, str, str]] = []

    for row in rows:
        code = str(row["bcd"]).zfill(10)
        sido_code = code[:2]
        sigungu_code = code[:5]
        sidos[sido_code] = row["sido"]
        sigungus[sigungu_code] = (sido_code, row["sgg"])
        dongs.append((code, sigungu_code, sido_code, row["leg"], infer_dong_type(row["leg"])))

    sigungu_sort: dict[str, int] = {}
    by_sido: dict[str, list[str]] = defaultdict(list)
    for code, (sido_code, _name) in sigungus.items():
        by_sido[sido_code].append(code)
    for sido_code, codes in by_sido.items():
        for index, code in enumerate(sorted(codes, key=lambda item: sigungus[item][1]), start=1):
            sigungu_sort[code] = index

    lines: list[str] = [
        "-- V163: Upsert full Korean legal-district master (행안부 법정동 10자리).",
        "-- Source: src/backend/src/main/resources/data/korean_bcd.json",
        "-- Regenerate: python3 scripts/generate-region-seed-sql.py",
        "",
        "-- V51 pilot fixture rows can collide on (sido_code, name) with official codes.",
        "-- Drop unreferenced pilot rows first; branch FK dong codes are preserved.",
        "DELETE FROM region_dongs",
        "WHERE code NOT IN (",
        "    SELECT region_dong_code FROM branches WHERE region_dong_code IS NOT NULL",
        ");",
        "",
        "DELETE FROM region_sigungus s",
        "WHERE NOT EXISTS (",
        "    SELECT 1 FROM region_dongs d WHERE d.sigungu_code = s.code",
        ");",
        "",
        "DELETE FROM region_sidos si",
        "WHERE NOT EXISTS (",
        "    SELECT 1 FROM region_sigungus s WHERE s.sido_code = si.code",
        ");",
        "",
    ]

    official_sigungu_codes = sorted(sigungus.keys())
    official_code_list = ", ".join(sql_literal(code) for code in official_sigungu_codes)

    lines.extend(
        [
            "-- Drop pilot sigungu rows superseded by official codes (keep branch-referenced).",
            "DELETE FROM region_sigungus s",
            "WHERE NOT EXISTS (",
            "    SELECT 1 FROM region_dongs d WHERE d.sigungu_code = s.code",
            ")",
            f"  AND s.code NOT IN ({official_code_list});",
            "",
            "-- Align surviving rows to official names before inserting new sigungu codes.",
        ]
    )
    for code in official_sigungu_codes:
        sido_code, name = sigungus[code]
        lines.append(
            "UPDATE region_sigungus SET "
            f"name = {sql_literal(name)}, "
            f"sido_code = {sql_literal(sido_code)}, "
            f"sort_order = {sigungu_sort[code]} "
            f"WHERE code = {sql_literal(code)};"
        )
    lines.append("")

    sido_values = [
        f"({sql_literal(code)}, {sql_literal(name)}, {sql_literal(SIDO_ENG.get(code, ''))}, {SIDO_ORDER.get(code, 99)})"
        for code, name in sorted(sidos.items(), key=lambda item: SIDO_ORDER.get(item[0], 99))
    ]
    lines.extend(
        [
            "INSERT INTO region_sidos (code, name, name_eng, sort_order) VALUES",
            ",\n".join(sido_values),
            "ON CONFLICT (code) DO UPDATE SET",
            "    name = EXCLUDED.name,",
            "    name_eng = EXCLUDED.name_eng,",
            "    sort_order = EXCLUDED.sort_order;",
            "",
        ]
    )

    sigungu_values = [
        (
            f"({sql_literal(code)}, {sql_literal(meta[0])}, {sql_literal(meta[1])}, "
            f"{sigungu_sort[code]})"
        )
        for code, meta in sorted(sigungus.items())
    ]
    for batch in chunk(sigungu_values, 200):
        lines.extend(
            [
                "INSERT INTO region_sigungus (code, sido_code, name, sort_order) VALUES",
                ",\n".join(batch),
                "ON CONFLICT (code) DO UPDATE SET",
                "    sido_code = EXCLUDED.sido_code,",
                "    name = EXCLUDED.name,",
                "    sort_order = EXCLUDED.sort_order;",
                "",
            ]
        )

    dong_values = [
        (
            f"({sql_literal(code)}, {sql_literal(sigungu_code)}, {sql_literal(sido_code)}, "
            f"{sql_literal(name)}, {sql_literal(dong_type)}, TRUE)"
        )
        for code, sigungu_code, sido_code, name, dong_type in sorted(dongs)
    ]
    for batch in chunk(dong_values, 200):
        lines.extend(
            [
                "INSERT INTO region_dongs (code, sigungu_code, sido_code, name, dong_type, is_active) VALUES",
                ",\n".join(batch),
                "ON CONFLICT (code) DO UPDATE SET",
                "    sigungu_code = EXCLUDED.sigungu_code,",
                "    sido_code = EXCLUDED.sido_code,",
                "    name = EXCLUDED.name,",
                "    dong_type = EXCLUDED.dong_type,",
                "    is_active = EXCLUDED.is_active;",
                "",
            ]
        )

    OUTPUT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(
        f"Wrote {OUTPUT_FILE} "
        f"({len(sidos)} sidos, {len(sigungus)} sigungus, {len(dongs)} dongs)"
    )


if __name__ == "__main__":
    main()
