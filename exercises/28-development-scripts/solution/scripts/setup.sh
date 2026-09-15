#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
state="${PROJECT_STATE_DIR:-$root/.local-state}"
mkdir -p "$state"
if [[ ! -f "$state/migrations.log" ]]; then printf '%s
' 001-initial > "$state/migrations.log"; fi
cp "$root/fixtures/sample.json" "$state/data.json"
printf '%s
' ready
