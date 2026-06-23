#!/usr/bin/env python3
"""Verify Kakao Geocoding + Mobility Directions (car) for two addresses."""

from __future__ import annotations

import json
import os
import sys
import urllib.parse
import urllib.request

ADDR_A = "서울특별시 강남구 테헤란로 152"
ADDR_B = "서울특별시 강남구 역삼로 180"


def http_get(url: str, headers: dict[str, str] | None = None) -> tuple[int, str]:
    req = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, resp.read().decode()
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode()


def geocode(key: str, address: str) -> tuple[float, float, str]:
    query = urllib.parse.urlencode({"query": address})
    status, body = http_get(
        f"https://dapi.kakao.com/v2/local/search/address.json?{query}",
        {"Authorization": f"KakaoAK {key}"},
    )
    data = json.loads(body)
    if status != 200:
        raise RuntimeError(f"geocode HTTP {status}: {body[:300]}")
    docs = data.get("documents") or []
    if not docs:
        raise RuntimeError(f"geocode no result for {address!r}: {body[:300]}")
    doc = docs[0]
    lng = float(doc["x"])
    lat = float(doc["y"])
    label = doc.get("address_name") or doc.get("road_address_name") or address
    return lng, lat, label


def directions(key: str, origin_lng: float, origin_lat: float, dest_lng: float, dest_lat: float) -> dict:
    params = urllib.parse.urlencode(
        {
            "origin": f"{origin_lng},{origin_lat}",
            "destination": f"{dest_lng},{dest_lat}",
            "priority": "RECOMMEND",
            "summary": "true",
        }
    )
    status, body = http_get(
        f"https://apis-navi.kakaomobility.com/v1/directions?{params}",
        {"Authorization": f"KakaoAK {key}"},
    )
    data = json.loads(body)
    if status != 200:
        raise RuntimeError(f"directions HTTP {status}: {body[:500]}")
    routes = data.get("routes") or []
    if not routes:
        raise RuntimeError(f"directions empty routes: {body[:500]}")
    route = routes[0]
    if route.get("result_code") != 0:
        raise RuntimeError(
            f"directions failed: code={route.get('result_code')} msg={route.get('result_msg')}"
        )
    return route.get("summary") or {}


def destinations_directions(
    key: str,
    origin_lng: float,
    origin_lat: float,
    destinations: list[tuple[str, float, float]],
) -> dict:
    """One origin -> many destinations driving distance/time (public v1 API)."""
    payload = {
        "origin": {"x": origin_lng, "y": origin_lat},
        "destinations": [
            {"key": label, "x": lng, "y": lat}
            for label, lng, lat in destinations
        ],
        "radius": 10000,
    }
    req = urllib.request.Request(
        "https://apis-navi.kakaomobility.com/v1/destinations/directions",
        data=json.dumps(payload).encode(),
        headers={
            "Authorization": f"KakaoAK {key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode()
            status = resp.status
    except urllib.error.HTTPError as exc:
        status = exc.code
        body = exc.read().decode()
        raise RuntimeError(f"destinations/directions HTTP {status}: {body[:800]}") from exc
    return json.loads(body)


def main() -> int:
    key = os.environ.get("KAKAO_REST_KEY", "").strip()
    if not key:
        print("KAKAO_REST_KEY is not set", file=sys.stderr)
        return 1

    print("=== Kakao API verification (car directions) ===")
    print(f"A: {ADDR_A}")
    print(f"B: {ADDR_B}")
    print()

    lng_a, lat_a, label_a = geocode(key, ADDR_A)
    lng_b, lat_b, label_b = geocode(key, ADDR_B)
    print(f"Geocode A: {label_a} -> lng={lng_a}, lat={lat_a}")
    print(f"Geocode B: {label_b} -> lng={lng_b}, lat={lat_b}")
    print()

    summary = directions(key, lng_a, lat_a, lng_b, lat_b)
    distance_m = summary.get("distance", 0)
    duration_s = summary.get("duration", 0)
    print("=== Driving Directions (A -> B) ===")
    print(f"distance: {distance_m} m ({distance_m / 1000:.2f} km)")
    print(f"duration: {duration_s} s ({duration_s / 60:.1f} min)")
    print()

    print("=== Multi-destination Directions (A -> A,B) ===")
    try:
        multi = destinations_directions(
            key,
            lng_a,
            lat_a,
            [("A", lng_a, lat_a), ("B", lng_b, lat_b)],
        )
        for route in multi.get("routes") or []:
            summary = route.get("summary") or {}
            print(
                f"  key={route.get('key')}: "
                f"{summary.get('distance')} m, {summary.get('duration')} s "
                f"({route.get('result_msg')})"
            )
    except RuntimeError as exc:
        print(f"multi-destination call failed: {exc}")

    print()
    print("OK: address -> geocode -> car driving distance/time is available")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
