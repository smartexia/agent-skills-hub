param(
    [Parameter(Mandatory = $true)]
    [string]$Target,

    [string]$DestSubdir = ".ai/agency-agents",

    [switch]$Clean
)

$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Split-Path -Parent $scriptDir
$destRoot = Join-Path $Target $DestSubdir

$bundleDirs = @(
    "academic",
    "design",
    "engineering",
    "game-development",
    "marketing",
    "paid-media",
    "product",
    "project-management",
    "sales",
    "specialized",
    "spatial-computing",
    "support",
    "testing",
    "skills",
    "squads"
)

if (-not (Test-Path -LiteralPath $Target -PathType Container)) {
    throw "Target project does not exist: $Target"
}

if ($Clean -and (Test-Path -LiteralPath $destRoot)) {
    Remove-Item -LiteralPath $destRoot -Recurse -Force
    Write-Host "[OK] Removed existing bundle at $destRoot"
}

New-Item -ItemType Directory -Path $destRoot -Force | Out-Null

foreach ($dir in $bundleDirs) {
    $source = Join-Path $repoRoot $dir
    if (-not (Test-Path -LiteralPath $source -PathType Container)) {
        continue
    }

    $destination = Join-Path $destRoot $dir
    Copy-Item -LiteralPath $source -Destination $destination -Recurse -Force
    Write-Host "[OK] Copied $dir -> $destination"
}

Copy-Item -LiteralPath (Join-Path $repoRoot "README.md") -Destination (Join-Path $destRoot "README.source.md") -Force
Write-Host "[OK] Copied README.md -> $(Join-Path $destRoot 'README.source.md')"

$usage = @'
# Agency Bundle Usage

This project-scoped bundle was copied from the Agency repo so you can use the files directly inside another project.

## Folder Layout

- `agents`: agent files live inside the category folders such as `engineering/`, `design/`, and `marketing/`
- `skills/`: reusable task-specific instructions
- `squads/`: pre-composed teams that coordinate multiple agents

## Codex

No global installation is required.

1. Keep this bundle inside the project.
2. Reference the files during the conversation.
3. Example prompts:
   - "Use the agent in `.ai/agency-agents/engineering/engineering-frontend-developer.md` for this task."
   - "Apply the skill in `.ai/agency-agents/skills/...` to this change."
   - "Use the squad in `.ai/agency-agents/squads/squad-tech-development.md` as project context."

## Claude Code

- Agents: copy chosen `.md` files to `~/.claude/agents/`
- Skills: copy chosen `SKILL.md` files to `~/.claude/skills/<skill-name>/SKILL.md`
- Squads: normally use the squad file as project/conversation context rather than installing it globally

## Practical Rule

- Agent = one specialist
- Skill = one capability
- Squad = a prebuilt team
'@

Set-Content -LiteralPath (Join-Path $destRoot "USAGE.md") -Value $usage -Encoding utf8
Write-Host "[OK] Wrote usage guide -> $(Join-Path $destRoot 'USAGE.md')"
Write-Host "[OK] Project bundle ready at $destRoot"
