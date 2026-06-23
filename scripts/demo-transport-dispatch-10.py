#!/usr/bin/env python3
"""
Seed 10 transport clients (address-only) and build pickup routes using
Kakao Geocoding + Mobility driving distances, then persist DRAFT runs via API.
"""

from __future__ import annotations

import base64
import json
import os
import secrets
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import date, time
from typing import Any

import psycopg2
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

ORG_ID = "00000001-0001-4000-8000-000000000001"
BRANCH_ID = "00010101-0001-4000-8000-000000000001"
USER_ID = "00000002-0002-4000-8000-000000000001"
VEHICLE_IDS = [
    "a1000001-0001-4000-8000-000000000001",
    "a1000002-0002-4000-8000-000000000002",
]
DEPOT_ADDRESS = "서울특별시 강남구 테헤란로 152"
RUN_DATE = date.today().isoformat()

CLIENTS = [
    ("김영희", "서울특별시 강남구 역삼로 180", "08:30:00", "LTC-D10-001"),
    ("이철수", "서울특별시 강남구 논현로 132", "08:35:00", "LTC-D10-002"),
    ("박순자", "서울특별시 강남구 선릉로 428", "08:40:00", "LTC-D10-003"),
    ("최만수", "서울특별시 강남구 봉은사로 524", "08:45:00", "LTC-D10-004"),
    ("정미경", "서울특별시 강남구 삼성로 511", "08:50:00", "LTC-D10-005"),
    ("한동진", "서울특별시 강남구 도곡로 401", "08:55:00", "LTC-D10-006"),
    ("오금자", "서울특별시 강남구 남부순환로 2806", "09:00:00", "LTC-D10-007"),
    ("윤태호", "서울특별시 강남구 압구정로 201", "09:05:00", "LTC-D10-008"),
    ("강지연", "서울특별시 강남구 영동대로 513", "09:10:00", "LTC-D10-009"),
    ("조성민", "서울특별시 강남구 강남대로 390", "09:15:00", "LTC-D10-010"),
]

CLIENT_IDS = [f"d10000{i:02d}-0001-4000-8000-0000000000{i:02d}" for i in range(1, 11)]


@dataclass
class Point:
    key: str
    name: str
    address: str
    lng: float
    lat: float


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


def http_json(method: str, url: str, headers: dict[str, str], body: Any | None = None) -> Any:
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read().decode()
            return json.loads(raw) if raw else None
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode()
        raise RuntimeError(f"{method} {url} -> HTTP {exc.code}: {detail[:800]}") from exc


def geocode(key: str, address: str) -> tuple[float, float, str]:
    query = urllib.parse.urlencode({"query": address})
    data = http_json(
        "GET",
        f"https://dapi.kakao.com/v2/local/search/address.json?{query}",
        {"Authorization": f"KakaoAK {key}"},
    )
    docs = data.get("documents") or []
    if not docs:
        raise RuntimeError(f"geocode failed: {address}")
    doc = docs[0]
    label = doc.get("address_name") or doc.get("road_address_name") or address
    return float(doc["x"]), float(doc["y"]), label


def driving_distances_m(
    key: str, origin: Point, destinations: list[Point]
) -> dict[str, int]:
    payload = {
        "origin": {"x": origin.lng, "y": origin.lat},
        "destinations": [
            {"key": dest.key, "x": dest.lng, "y": dest.lat} for dest in destinations
        ],
        "radius": 10000,
    }
    data = http_json(
        "POST",
        "https://apis-navi.kakaomobility.com/v1/destinations/directions",
        {
            "Authorization": f"KakaoAK {key}",
            "Content-Type": "application/json",
        },
        payload,
    )
    out: dict[str, int] = {}
    for route in data.get("routes") or []:
        if route.get("result_code") != 0:
            continue
        out[route["key"]] = int((route.get("summary") or {}).get("distance") or 0)
    return out


def build_distance_matrix(key: str, points: list[Point]) -> dict[str, dict[str, int]]:
    matrix: dict[str, dict[str, int]] = {p.key: {} for p in points}
    for origin in points:
        others = [p for p in points if p.key != origin.key]
        if not others:
            matrix[origin.key][origin.key] = 0
            continue
        distances = driving_distances_m(key, origin, others)
        matrix[origin.key][origin.key] = 0
        for dest in others:
            matrix[origin.key][dest.key] = distances.get(dest.key, 10**9)
    return matrix


def route_distance(matrix: dict[str, dict[str, int]], keys: list[str]) -> int:
    total = 0
    for i in range(len(keys) - 1):
        total += matrix[keys[i]][keys[i + 1]]
    return total


def nearest_neighbor_route(
    matrix: dict[str, dict[str, int]], depot_key: str, client_keys: list[str]
) -> list[str]:
    remaining = set(client_keys)
    ordered: list[str] = []
    current = depot_key
    while remaining:
        nxt = min(remaining, key=lambda k: matrix[current][k])
        ordered.append(nxt)
        remaining.remove(nxt)
        current = nxt
    return ordered


def assign_clients(clients: list[Point], vehicle_count: int, capacity: int) -> list[list[str]]:
    buckets: list[list[str]] = [[] for _ in range(vehicle_count)]
    for idx, client in enumerate(clients):
        vehicle_idx = idx % vehicle_count
        if len(buckets[vehicle_idx]) >= capacity:
            vehicle_idx = min(range(vehicle_count), key=lambda i: len(buckets[i]))
        buckets[vehicle_idx].append(client.key)
    return buckets


def seed_clients(conn, pii_key: str) -> None:
    roster_names = [name for name, _, _, _ in CLIENTS]
    with conn.cursor() as cur:
        cur.execute(
            "DELETE FROM transport_run_stops WHERE organization_id = %s::uuid",
            (ORG_ID,),
        )
        cur.execute(
            "DELETE FROM transport_runs WHERE organization_id = %s::uuid",
            (ORG_ID,),
        )
        # Legacy dev fixtures can share names with demo transport clients; keep them
        # registered but off the transport roster so the same person is not listed twice.
        cur.execute(
            """
            UPDATE clients
               SET uses_transport = FALSE
             WHERE organization_id = %s::uuid
               AND branch_id = %s::uuid
               AND uses_transport = TRUE
               AND name = ANY(%s)
               AND (ltc_cert_no IS NULL OR ltc_cert_no NOT LIKE 'LTC-D10-%%')
            """,
            (ORG_ID, BRANCH_ID, roster_names),
        )
        cur.execute(
            """
            DELETE FROM clients
             WHERE organization_id = %s::uuid
               AND ltc_cert_no LIKE 'LTC-D10-%%'
            """,
            (ORG_ID,),
        )
        for client_id, (name, address, pickup_time, cert_no) in zip(CLIENT_IDS, CLIENTS):
            enc = encrypt_pii(address, pii_key)
            cur.execute(
                """
                INSERT INTO clients (
                  id, organization_id, branch_id, name, birth_date, gender,
                  ltc_grade, ltc_cert_no, copay_type, consent_collected_at,
                  uses_transport, address_encrypted, address_search_encrypted,
                  pickup_lat, pickup_lng, geocoded_at,
                  default_pickup_time, is_active, address_verified
                ) VALUES (
                  %s::uuid, %s::uuid, %s::uuid, %s, '1940-01-01', 'F',
                  3, %s, 'GENERAL', NOW(),
                  TRUE, %s, %s,
                  NULL, NULL, NULL,
                  %s::time, TRUE, TRUE
                )
                """,
                (
                    client_id,
                    ORG_ID,
                    BRANCH_ID,
                    name,
                    cert_no,
                    psycopg2.Binary(enc),
                    psycopg2.Binary(enc),
                    pickup_time,
                ),
            )
        cur.execute(
            """
            UPDATE branches
               SET name = '서울 강남 주간보호센터',
                   address_line1 = %s
             WHERE id = %s::uuid
            """,
            (DEPOT_ADDRESS, BRANCH_ID),
        )
    conn.commit()


def login(base_url: str) -> str:
    data = http_json(
        "POST",
        f"{base_url}/api/v1/auth/login",
        {"Content-Type": "application/json"},
        {"email": "test@test.com", "password": "ogada1234"},
    )
    return data["accessToken"]


def create_run(
    base_url: str,
    token: str,
    vehicle_id: str,
    stop_client_ids: list[str],
) -> dict[str, Any]:
    stops = [
        {"clientId": client_id, "stopOrder": idx, "pickupTime": None}
        for idx, client_id in enumerate(stop_client_ids, start=1)
    ]
    return http_json(
        "POST",
        f"{base_url}/api/v1/transport/runs",
        {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        {
            "runDate": RUN_DATE,
            "direction": "PICKUP",
            "vehicleId": vehicle_id,
            "stops": stops,
        },
    )


def main() -> int:
    kakao_key = require_env("KAKAO_REST_KEY")
    pii_key = require_env("PII_ENCRYPTION_KEY")
    base_url = os.environ.get("OGADA_API_BASE", "http://127.0.0.1:8080")
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        dbname=os.environ.get("DB_NAME", "ogada"),
        user=os.environ.get("DB_USERNAME", "ogada"),
        password=os.environ.get("DB_PASSWORD", "ogada"),
    )

    print("=== 1) Seed 10 clients (address only, no coordinates) ===")
    seed_clients(conn, pii_key)
    conn.close()
    print("seeded 10 clients")

    print("\n=== 2) Geocode depot + clients ===")
    depot_lng, depot_lat, depot_label = geocode(kakao_key, DEPOT_ADDRESS)
    depot = Point("DEPOT", "센터", depot_label, depot_lng, depot_lat)
    client_points: list[Point] = []
    for client_id, (name, address, _, _) in zip(CLIENT_IDS, CLIENTS):
        lng, lat, label = geocode(kakao_key, address)
        client_points.append(Point(client_id, name, label, lng, lat))
        print(f"  {name}: {label} ({lat:.5f}, {lng:.5f})")

    print("\n=== 3) Build driving-distance matrix (Kakao Mobility) ===")
    all_points = [depot] + client_points
    matrix = build_distance_matrix(kakao_key, all_points)
    print(f"  matrix size: {len(all_points)} x {len(all_points)}")

    print("\n=== 4) Assign + route (2 vehicles, cap 8) ===")
    assignments = assign_clients(client_points, vehicle_count=2, capacity=8)
    plans: list[dict[str, Any]] = []
    for vehicle_idx, client_keys in enumerate(assignments):
        if not client_keys:
            continue
        ordered = nearest_neighbor_route(matrix, depot.key, client_keys)
        route_keys = [depot.key] + ordered + [depot.key]
        distance_m = route_distance(matrix, route_keys)
        plans.append(
            {
                "vehicleId": VEHICLE_IDS[vehicle_idx],
                "vehicleLabel": f"{vehicle_idx + 1}호차",
                "clientKeys": ordered,
                "distanceM": distance_m,
            }
        )

    print("\n=== 5) Persist DRAFT runs via API ===")
    token = login(base_url)
    created = []
    for plan in plans:
        run = create_run(base_url, token, plan["vehicleId"], plan["clientKeys"])
        created.append(run)
        names = [
            next(p.name for p in client_points if p.key == cid)
            for cid in plan["clientKeys"]
        ]
        print(
            f"\n[{plan['vehicleLabel']}] runId={run['id']} "
            f"stops={len(plan['clientKeys'])} driving={plan['distanceM']}m"
        )
        for idx, name in enumerate(names, start=1):
            print(f"  {idx}. {name}")

    total_m = sum(p["distanceM"] for p in plans)
    print(f"\n=== Summary ({RUN_DATE}) ===")
    print(f"clients: 10, vehicles: {len(plans)}, total driving distance: {total_m} m ({total_m/1000:.2f} km)")
    print("status: DRAFT (review at /transport)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
