#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
echo "Executando o componente de domínio pelo host local de demonstração..."
dotnet run --project "$root/tests/PublicTests/PublicTests.csproj" --nologo
