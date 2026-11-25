#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INPUT="${SCRIPT_DIR}/slides.md"
OUTPUT="${SCRIPT_DIR}/week13-web-application-security.pptx"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "Pandoc is required to generate PPTX output." >&2
  exit 1
fi

pandoc "${INPUT}" --from markdown --to pptx --output "${OUTPUT}"
echo "Wrote ${OUTPUT}"
