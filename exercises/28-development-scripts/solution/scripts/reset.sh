#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
state="${PROJECT_STATE_DIR:-$root/.local-state}"
case "$state" in "$root/.local-state"|/tmp/jr-eng-*/state) ;; *) echo "Refusing unsafe state path" >&2; exit 2;; esac
find "$state" -mindepth 1 -maxdepth 1 -type f -delete 2>/dev/null || true
