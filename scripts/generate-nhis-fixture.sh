#!/usr/bin/env bash
# Generates scripts/seed-nhis-fixture.xlsx — synthetic NHIS pilot sample (결정 82).
# Requires: Java 17+, Maven, src/backend POI dependency.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BACKEND="$ROOT/src/backend"
OUTPUT="$ROOT/scripts/seed-nhis-fixture.xlsx"
TMP_CLASS="$BACKEND/target/test-classes"

cd "$BACKEND"
mvn -q test-compile -DskipTests
java -cp "$TMP_CLASS:$(mvn -q dependency:build-classpath -Dmdep.outputFile=/dev/stdout -DincludeScope=test)" \
  com.ogada.backend.billing.domain.NhisFixtureExporter "$OUTPUT"
echo "Wrote $OUTPUT"
