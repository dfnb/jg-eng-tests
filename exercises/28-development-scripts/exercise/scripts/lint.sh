#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
bash -n "$root/scripts/setup.sh" "$root/scripts/reset.sh" "$root/scripts/test.sh"
