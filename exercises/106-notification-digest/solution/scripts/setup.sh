#!/usr/bin/env bash
        set -euo pipefail
        root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
        command -v dotnet >/dev/null || { echo "Instale o SDK .NET 10." >&2; exit 1; }
        dotnet restore "$root/tests/PublicTests/PublicTests.csproj" --nologo
