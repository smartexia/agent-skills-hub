#!/usr/bin/env bash
#
# install-project-bundle.sh -- Copy the Agency source bundle into another project.
#
# Creates a project-scoped bundle with agents, skills, squads, and a short
# usage guide so tools like Codex can consume the files directly from the repo.
#
# Usage:
#   ./scripts/install-project-bundle.sh --target /path/to/project [--dest-subdir .ai/agency-agents] [--clean] [--help]
#
# Examples:
#   ./scripts/install-project-bundle.sh --target /work/my-app
#   ./scripts/install-project-bundle.sh --target /work/my-app --dest-subdir ai/agency
#   ./scripts/install-project-bundle.sh --target /work/my-app --clean

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

DEST_SUBDIR=".ai/agency-agents"
TARGET_PROJECT=""
CLEAN=false

BUNDLE_DIRS=(
  academic
  design
  engineering
  game-development
  marketing
  paid-media
  product
  project-management
  sales
  specialized
  spatial-computing
  support
  testing
  skills
  squads
)

usage() {
  sed -n '3,12p' "$0" | sed 's/^# \{0,1\}//'
  exit 0
}

err() { printf '[ERR] %s\n' "$*" >&2; }
ok() { printf '[OK]  %s\n' "$*"; }
warn() { printf '[!!]  %s\n' "$*"; }

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target)
      TARGET_PROJECT="${2:-}"
      shift 2
      ;;
    --dest-subdir)
      DEST_SUBDIR="${2:-}"
      shift 2
      ;;
    --clean)
      CLEAN=true
      shift
      ;;
    --help|-h)
      usage
      ;;
    *)
      err "Unknown argument: $1"
      usage
      ;;
  esac
done

[[ -n "$TARGET_PROJECT" ]] || { err "Missing --target /path/to/project"; exit 1; }
[[ -d "$TARGET_PROJECT" ]] || { err "Target project does not exist: $TARGET_PROJECT"; exit 1; }

DEST_ROOT="$TARGET_PROJECT/$DEST_SUBDIR"

if $CLEAN && [[ -e "$DEST_ROOT" ]]; then
  rm -rf "$DEST_ROOT"
  ok "Removed existing bundle at $DEST_ROOT"
fi

mkdir -p "$DEST_ROOT"

for dir in "${BUNDLE_DIRS[@]}"; do
  [[ -d "$REPO_ROOT/$dir" ]] || continue
  cp -R "$REPO_ROOT/$dir" "$DEST_ROOT/"
  ok "Copied $dir -> $DEST_ROOT/$dir"
done

cp "$REPO_ROOT/README.md" "$DEST_ROOT/README.source.md"
ok "Copied README.md -> $DEST_ROOT/README.source.md"

cat > "$DEST_ROOT/USAGE.md" <<EOF
# Agency Bundle Usage

This project-scoped bundle was copied from the Agency repo so you can use the files directly inside another project.

## Folder Layout

- \`agents\`: agent files live inside the category folders such as \`engineering/\`, \`design/\`, and \`marketing/\`
- \`skills/\`: reusable task-specific instructions
- \`squads/\`: pre-composed teams that coordinate multiple agents

## Codex

No global installation is required.

1. Keep this bundle inside the project.
2. Reference the files during the conversation.
3. Example prompts:
   - "Use the agent in \`.ai/agency-agents/engineering/engineering-frontend-developer.md\` for this task."
   - "Apply the skill in \`.ai/agency-agents/skills/... \` to this change."
   - "Use the squad in \`.ai/agency-agents/squads/squad-tech-development.md\` as project context."

## Claude Code

- Agents: copy chosen \`.md\` files to \`~/.claude/agents/\`
- Skills: copy chosen \`SKILL.md\` files to \`~/.claude/skills/<skill-name>/SKILL.md\`
- Squads: normally use the squad file as project/conversation context rather than installing it globally

## Practical Rule

- Agent = one specialist
- Skill = one capability
- Squad = a prebuilt team
EOF

ok "Wrote usage guide -> $DEST_ROOT/USAGE.md"
ok "Project bundle ready at $DEST_ROOT"
