param(
  [Parameter(Mandatory=$true)][string]$Tool,
  [string]$ArgsJson = "{}",
  [int]$TimeoutSec = 120
)

$ErrorActionPreference = "Stop"

$authPath = Join-Path $env:USERPROFILE ".local\share\opencode\mcp-auth.json"
$auth = Get-Content $authPath -Raw | ConvertFrom-Json
$tok = $auth.clay.tokens.accessToken
$url = "https://api.clay.com/v3/mcp"

$H = @{
  "Authorization" = "Bearer $tok"
  "Content-Type"  = "application/json"
  "Accept"        = "application/json, text/event-stream"
}

function Parse-McpBody([string]$body) {
  if ($body.Contains("data:")) {
    $dataLines = @()
    foreach ($l in ($body -split "`n")) {
      if ($l.StartsWith("data:")) { $dataLines += $l.Substring(5).Trim() }
    }
    if ($dataLines.Count -gt 0) { $body = ($dataLines -join "`n") }
  }
  return $body
}

# initialize
$init = @{
  jsonrpc = "2.0"; id = 1; method = "initialize"
  params = @{
    protocolVersion = "2025-03-26"
    capabilities = @{}
    clientInfo = @{ name = "oc-agent"; version = "1.0" }
  }
} | ConvertTo-Json -Depth 6

$r = Invoke-WebRequest -Uri $url -Method Post -Headers $H -Body $init -UseBasicParsing -TimeoutSec $TimeoutSec
$sid = $r.Headers["Mcp-Session-Id"]
if ($sid -is [array]) { $sid = $sid[0] }
$H["Mcp-Session-Id"] = $sid

# initialized notification
$notif = '{"jsonrpc":"2.0","method":"notifications/initialized"}'
Invoke-WebRequest -Uri $url -Method Post -Headers $H -Body $notif -UseBasicParsing -TimeoutSec $TimeoutSec | Out-Null

# tools/call
$callObj = @{
  jsonrpc = "2.0"; id = 2; method = "tools/call"
  params = @{ name = $Tool; arguments = (ConvertFrom-Json $ArgsJson) }
}
$callBody = $callObj | ConvertTo-Json -Depth 10
$r2 = Invoke-WebRequest -Uri $url -Method Post -Headers $H -Body $callBody -UseBasicParsing -TimeoutSec $TimeoutSec
$raw = Parse-McpBody $r2.Content
$o = $raw | ConvertFrom-Json

if ($o.error) {
  Write-Output "MCP ERROR: $($o.error.message)"
  exit 1
}

# content is usually [{type:"text", text:"..."}]
$textParts = @()
foreach ($c in $o.result.content) {
  if ($c.type -eq "text") { $textParts += $c.text }
}
$out = $textParts -join "`n"
if (-not $out) { $out = ($o.result | ConvertTo-Json -Depth 10) }
Write-Output $out
