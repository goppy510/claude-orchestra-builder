---
name: init-orchestra
description: Interactive scaffolder for Claude Code orchestration environments (like create-next-app)
disable-model-invocation: true
---

# Init Orchestra

Interactively set up a Claude Code orchestration environment for a target project.
Respond to user in Japanese (敬語). All generated files must be in English.

## Usage

```
/init-orchestra <target-path>
```

`<target-path>` is the root of the project to set up. If omitted, ask the user for the path.
All generated files are placed relative to this path (e.g., `<target-path>/.claude/`).

## Templates

Source: `@.claude/skills/init-orchestra/templates/`

### CLAUDE.md composition
The target CLAUDE.md is assembled from two layers:
1. `@templates/config/CLAUDE.md.template` — project-specific (name, description, commands). Replace `{{placeholders}}`.
2. `@templates/config/CLAUDE.md.base` — shared foundation (language policy, references, principles). Copy as-is.

Merge: template (top) + base (bottom). Final result must be under 30 lines.

### Other file templates

| Template | Target (relative to target-path) | When |
|----------|--------|------|
| `@templates/skills/plan-SKILL.md` | `.claude/skills/plan/SKILL.md` | Always |
| `@templates/skills/review-SKILL.md` | `.claude/skills/review/SKILL.md` | Solo mode |
| `@templates/skills/review-team-SKILL.md` | `.claude/skills/review/SKILL.md` | Team mode |
| `@templates/agents/codex-assistant.md` | `.claude/agents/codex-assistant.md` | Codex selected |
| `@templates/rules/codex-delegation.md` | `.claude/rules/codex-delegation.md` | Codex selected |
| `@templates/skills/add-feature-SKILL.md` | `.claude/skills/add-feature/SKILL.md` | Codex selected |
| `@templates/config/codex-config.toml` | `.codex/config.toml` | Codex selected |
| `@templates/config/codex-context-loader-SKILL.md` | `.codex/skills/context-loader/SKILL.md` | Codex selected |
| `@templates/agents/gemini-multimodal.md` | `.claude/agents/gemini-multimodal.md` | Gemini selected |
| `@templates/skills/analyze-media-SKILL.md` | `.claude/skills/analyze-media/SKILL.md` | Gemini selected |
| `@templates/config/GEMINI.md` | `.gemini/GEMINI.md` | Gemini selected |
| `@templates/config/gemini-context-loader-SKILL.md` | `.gemini/skills/context-loader/SKILL.md` | Gemini selected |
| `@templates/config/DESIGN.md` | `.claude/docs/DESIGN.md` | Codex or Gemini |
| `@templates/hooks/agent-router.py` | `.claude/hooks/agent-router.py` | Full automation |
| `@templates/hooks/error-to-codex.py` | `.claude/hooks/error-to-codex.py` | Full + Codex |
| `@templates/skills/startproject-SKILL.md` | `.claude/skills/startproject/SKILL.md` | Full automation |
| `@templates/agents/general-purpose.md` | `.claude/agents/general-purpose.md` | Standard+ |

## Workflow

### Phase 1: Interview

Use AskUserQuestion to gather information step by step. Ask one group at a time.

**Step 1 — Target path:**
If `$ARGUMENTS` is provided, use it as the target path. Otherwise ask:
- Target project path (absolute or relative)
- Validate the path exists. If not, ask whether to create it.

**Step 2 — Project basics:**
- Project name and brief description
- Primary language(s) and framework(s)
- Monorepo or single project?
- Existing project or starting fresh?
- If existing: detect build/test/lint commands from package.json, Makefile, Cargo.toml, etc.

**Step 3 — AI tool selection:**
Present these options:

```
AI構成を選択してください:

1. Claude only        — Claude Code単体で開発
2. Claude + Codex     — 設計・計画・デバッグにCodex CLIを活用
3. Claude + Gemini    — PDF・画像・動画などマルチモーダル処理を追加
4. Full (Claude + Codex + Gemini) — フル構成
```

If Codex or Gemini selected, confirm CLI is installed.

**Step 4 — Workflow preferences:**
- Solo developer or team?
- CI/CD integration needed?
- Primary use case: new development / maintenance / analysis / mixed
- Level of automation: minimal / standard / full

**Step 5 — Confirmation:**
Show a summary table of all selections and the files to be generated. Ask for confirmation.

### Phase 2: Generation

Generate files under `<target-path>`. Follow `@.claude/rules/generation-quality.md`.

**Strategy: copy then customize.**
1. Create directory structure under `<target-path>`
2. Copy relevant templates (based on selections) to their target paths
3. Customize only what needs project-specific changes:
   - CLAUDE.md: merge template (with placeholders replaced) + base
   - `rules/coding.md`: generate based on user's language/framework (no template — language-specific)
   - `rules/testing.md`: generate based on user's test framework (no template — framework-specific)
   - `hooks/agent-router.py`: adjust keyword patterns for user's stack
4. Leave all other copied templates as-is (they are already production-ready)

**Always generated (all configurations):**
- `<target>/.claude/CLAUDE.md` — merged from template + base. Max 30 lines.
- `<target>/.claude/rules/coding.md` — generated for user's language. Max 20 lines.
- `<target>/.claude/rules/testing.md` — generated for user's test framework. Max 15 lines.
- `<target>/.claude/docs/.gitkeep` — empty file
- `<target>/.claude/skills/plan/SKILL.md` — copied from template
- `<target>/.claude/skills/review/SKILL.md` — solo or team template

**docs/ structure (varies by AI tool selection):**
- Claude only → `docs/` (flat)
- +Codex → `docs/` + `docs/libraries/`+ `docs/DESIGN.md`
- +Gemini → `docs/` + `docs/research/` + `docs/DESIGN.md`
- Full → `docs/` + `docs/research/` + `docs/libraries/` + `docs/DESIGN.md`

**Codex-related (when Codex selected):**
- `.claude/agents/codex-assistant.md` — copied
- `.claude/rules/codex-delegation.md` — copied
- `.claude/skills/add-feature/SKILL.md` — copied
- `.codex/config.toml` — copied (project root)
- `.codex/skills/context-loader/SKILL.md` — copied (project root)

**Gemini-related (when Gemini selected):**
- `.claude/agents/gemini-multimodal.md` — copied
- `.claude/skills/analyze-media/SKILL.md` — copied
- `.gemini/GEMINI.md` — copied (project root)
- `.gemini/skills/context-loader/SKILL.md` — copied (project root)

**Full automation additions:**
- `.claude/hooks/agent-router.py` — copied, then customize keywords for user's stack
- `.claude/hooks/error-to-codex.py` — copied (only if Codex selected)
- `.claude/skills/startproject/SKILL.md` — copied
- `.claude/agents/general-purpose.md` — copied
- Register hooks in `<target>/.claude/settings.json`

**Automation level adjustments:**
- **minimal**: CLAUDE.md + rules + basic skills (plan, review). No agents, no hooks.
- **standard**: Above + agents + workflow skills. No hooks.
- **full**: Everything including hooks and settings.json.

### Phase 3: Validation

Verify each generated file at `<target-path>`:
- Skills have frontmatter (name, description)
- Agents have frontmatter (name, description, tools, model)
- CLAUDE.md is under 30 lines
- Hooks have shebang (`#!/usr/bin/env python3`)
- All directories exist

If any check fails, fix immediately before proceeding.

### Phase 4: Post-generation

1. Show a tree of all generated files under `<target-path>`
2. If hooks were generated, show the settings.json hook registration and remind user to review
3. Suggest permission setup:
   - Run `/permissions` to whitelist safe commands
   - Consider auto mode: `claude --permission-mode auto`
   - Consider sandbox mode: `/sandbox`
4. Suggest next steps:
   - `cd <target-path> && claude` to start using
   - `/plan` for the first task
   - If Codex: verify `codex --version`
   - If Gemini: verify `gemini` works

## Important rules

- NEVER generate a CLAUDE.md longer than 30 lines
- NEVER include information Claude can infer from reading code
- Copy templates first, then customize — do not improvise when a template exists
- Only generate from scratch: `rules/coding.md` and `rules/testing.md` (language-specific)
- All paths are relative to `<target-path>`, never write outside it
- Each skill must have proper frontmatter (name, description)
- Each agent must have proper frontmatter (name, description, tools, model)
- Hooks must be executable Python scripts with correct stdin/stdout JSON format
- Follow https://code.claude.com/docs/ja/best-practices strictly
