#!/usr/bin/env python3
"""Backfill encrypted client/branch addresses for local dev dummy data."""

from __future__ import annotations

import base64
import os
import secrets
import sys

import psycopg2
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

ORG_ID = "00000001-0001-4000-8000-000000000001"
BRANCH_ID = "00010101-0001-4000-8000-000000000001"
BUSAN_BRANCH_ID = "00010202-0002-4000-8000-000000000001"

CLIENT_ADDRESSES_BY_NAME = {
    "김영희": "서울특별시 강남구 역삼로 180",
    "이철수": "서울특별시 강남구 논현로 132",
    "박순자": "서울특별시 강남구 선릉로 428",
    "최만수": "서울특별시 강남구 봉은사로 524",
    "정미경": "서울특별시 강남구 삼성로 511",
    "한동진": "서울특별시 강남구 도곡로 401",
    "오금자": "서울특별시 강남구 남부순환로 2806",
    "윤태호": "서울특별시 강남구 압구정로 201",
    "강지연": "서울특별시 강남구 영동대로 513",
    "조성민": "서울특별시 강남구 강남대로 390",
    "홍길동(파일럿)": "서울특별시 강남구 테헤란로 1",
    "김영희(파일럿)": "서울특별시 강남구 논현로 2",
    "이철수(파일럿)": "서울특별시 강남구 선릉로 3",
}

BRANCH_ADDRESSES = {
    BRANCH_ID: "서울특별시 강남구 테헤란로 152",
    BUSAN_BRANCH_ID: "부산광역시 해운대구 해운대해변로 264",
}


def require_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise RuntimeError(f"{name} is not set")
    return value


def encrypt_pii(plain: str, encoded_key_b64: str) -> bytes:
    key = base64.b64decode(encoded_key_b64)
    iv = secrets.token_bytes(12)
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(iv, plain.encode("utf-8"), None)
    return iv + ciphertext


def main() -> int:
    pii_key = require_env("PII_ENCRYPTION_KEY")
    conn = psycopg2.connect(
        dbname=os.environ.get("DB_NAME", "ogada"),
        user=os.environ.get("DB_USERNAME", "ogada"),
        password=os.environ.get("DB_PASSWORD", "ogada"),
        host=os.environ.get("DB_HOST", "localhost"),
        port=os.environ.get("DB_PORT", "5432"),
    )

    updated_clients = 0
    with conn.cursor() as cur:
        for branch_id, address in BRANCH_ADDRESSES.items():
            cur.execute(
                """
                UPDATE branches
                   SET address_line1 = %s
                 WHERE id = %s::uuid
                   AND organization_id = %s::uuid
                """,
                (address, branch_id, ORG_ID),
            )

        cur.execute(
            """
            SELECT id::text, name
              FROM clients
             WHERE organization_id = %s::uuid
               AND is_active = TRUE
               AND (
                    address_encrypted IS NULL
                 OR address_search_encrypted IS NULL
               )
            """,
            (ORG_ID,),
        )
        rows = cur.fetchall()
        for client_id, name in rows:
            address = CLIENT_ADDRESSES_BY_NAME.get(name)
            if not address:
                print(f"skip {client_id} {name}: no mapping", file=sys.stderr)
                continue
            enc = encrypt_pii(address, pii_key)
            cur.execute(
                """
                UPDATE clients
                   SET address_encrypted = %s,
                       address_search_encrypted = %s,
                       address_verified = TRUE
                 WHERE id = %s::uuid
                """,
                (psycopg2.Binary(enc), psycopg2.Binary(enc), client_id),
            )
            updated_clients += 1
            print(f"updated {name} ({client_id}) -> {address}")

    conn.commit()
    conn.close()
    print(f"done: {updated_clients} client(s) backfilled")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
