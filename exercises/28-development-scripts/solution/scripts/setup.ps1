$ErrorActionPreference = "Stop"
$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$State = if ($env:PROJECT_STATE_DIR) { $env:PROJECT_STATE_DIR } else { Join-Path $Root ".local-state" }
New-Item -ItemType Directory -Force -Path $State | Out-Null
$Migration = Join-Path $State "migrations.log"
if (-not (Test-Path $Migration)) { Set-Content -Path $Migration -Value "001-initial" }
Copy-Item (Join-Path $Root "fixtures/sample.json") (Join-Path $State "data.json") -Force
Write-Output "ready"
