#!/usr/bin/env bash
    set -euo pipefail
    root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
    dotnet build "$root/tests/PublicTests/PublicTests.csproj" --nologo --no-restore
