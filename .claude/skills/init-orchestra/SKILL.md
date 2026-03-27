---
name: init-orchestra
description: Interactive scaffolder for Claude Code orchestration environments (like create-next-app)
disable-model-invocation: true
---

# Init Orchestra

Interactively set up a Claude Code orchestration environment for the user's project.
Respond to user in Japanese (敬語). All generated files must be in English.

## Templates

All templates are in `@.claude/skills/init-orchestra/templates/`. Read the relevant template before generating each file.

| Template | Target | When |
|----------|--------|------|
| `@templates/config/CLAUDE.md.template` | `.claude/CLAUDE.md` | Always |
| `@templates/skills/plan-SKILL.md` | `.claude/skills/plan/SKILL.md` | Always |
| `@templates/skills/review-SKILL.md` | `.claude/skills/review/SKILL.md` | Solo mode |
| `@templates/skills/review-team-SKILL.md` | `.claude/skills/review/SKILL.md` | Team mode |
| `@templates/agents/codex-assistant.md` | `.claude/agents/codex-assistant.md` | Codex selected |
| `@templates/rules/codex-delegation.md` | `.claude/rules/codex-delegation.md` | Codex selected |
| `@templates/skills/add-feature-SKILL.md` | `.claude/skills/add-feature/SKILL.md` | Codex selected |
| `@templates/config/codex-config.toml` | `.codex/config.toml` | Codex selected |
| `@templates/agents/gemini-multimodal.md` | `.claude/agents/gemini-multimodal.md` | Gemini selected |
| `@templates/skills/analyze-media-SKILL.md` | `.claude/skills/analyze-media/SKILL.md` | Gemini selected |
| `@templates/config/GEMINI.md` | `.gemini/GEMINI.md` | Gemini selected |
| `@templates/config/codex-context-loader-SKILL.md` | `.codex/skills/context-loader/SKILL.md` | Codex selected |
| `@templates/config/gemini-context-loader-SKILL.md` | `.gemini/skills/context-loader/SKILL.md` | Gemini selected |
| `@templates/config/DESIGN.md` | `.claude/docs/DESIGN.md` | Codex or Gemini selected |
| `@templates/hooks/agent-router.py` | `.claude/hooks/agent-router.py` | Full automation |
| `@templates/hooks/error-to-codex.py` | `.claude/hooks/error-to-codex.py` | Full + Codex |
| `@templates/skills/startproject-SKILL.md` | `.claude/skills/startproject/SKILL.md` | Full automation |
| `@templates/agents/general-purpose.md` | `.claude/agents/general-purpose.md` | Standard+ |

## Workflow

### Phase 1: Interview

Use AskUserQuestion to gather information step by step. Ask one group at a time.

**Step 1 — Project basics:**
- Project name and brief description
- Primary language(s) and framework(s)
- Monorepo or single project?
- Existing project or starting fresh?

**Step 2 — AI tool selection:**
Present these options:

```
AI構成を選択してください:

1. Claude only        — Claude Code単体で開発
2. Claude + Codex     — 設計・計画・デバッグにCodex CLIを活用
3. Claude + Gemini    — PDF・画像・動画などマルチモーダル処理を追加
4. Full (Claude + Codex + Gemini) — フル構成
```

If Codex or Gemini selected, confirm CLI is installed.

**Step 3 — Workflow preferences:**
- Solo developer or team?
- CI/CD integration needed?
- Primary use case: new development / maintenance / analysis / mixed
- Level of automation: minimal / standard / full

**Step 4 — Confirmation:**
Show a summary table of all selections and the files to be generated. Ask for confirmation.

### Phase 2: Generation

Generate files under `.claude/` in the current working directory.
Follow `@.claude/rules/generation-quality.md`.

**For each file:**
1. Read the corresponding template from the Templates table above
2. Adapt to the user's project (replace placeholders, adjust language/framework specifics)
3. Write to the target path

**Always generated (all configurations):**
- `.claude/CLAUDE.md` — from template, fill in project info. Max 30 lines.
- `.claude/rules/coding.md` — generate based on user's language/framework. Max 20 lines.
- `.claude/rules/testing.md` — generate based on user's test framework. Max 15 lines.
- `.claude/docs/.gitkeep` — empty file
- `.claude/skills/plan/SKILL.md` — from template
- `.claude/skills/review/SKILL.md` — use solo or team template based on Step 3

**docs/ structure (varies by AI tool selection):**
- Claude only → `.claude/docs/` (flat, no subdirectories)
- +Codex → `.claude/docs/` + `docs/libraries/` + `docs/DESIGN.md`
- +Gemini → `.claude/docs/` + `docs/research/` + `docs/DESIGN.md`
- Full → `.claude/docs/` + `docs/research/` + `docs/libraries/` + `docs/DESIGN.md`

**Codex-related (when Codex selected):**
- `.claude/agents/codex-assistant.md` — from template
- `.claude/rules/codex-delegation.md` — from template
- `.claude/skills/add-feature/SKILL.md` — from template
- `.codex/config.toml` — from template (project root, not .claude)
- `.codex/skills/context-loader/SKILL.md` — from template (loads shared docs)

**Gemini-related (when Gemini selected):**
- `.claude/agents/gemini-multimodal.md` — from template
- `.claude/skills/analyze-media/SKILL.md` — from template
- `.gemini/GEMINI.md` — from template (project root, not .claude)
- `.gemini/skills/context-loader/SKILL.md` — from template (loads shared docs)

**Full automation additions:**
- `.claude/hooks/agent-router.py` — from template. Customize keywords for user's stack.
- `.claude/hooks/error-to-codex.py` — from template (only if Codex selected)
- `.claude/skills/startproject/SKILL.md` — from template
- `.claude/agents/general-purpose.md` — from template
- Register hooks in `.claude/settings.json`

**Automation level adjustments:**
- **minimal**: CLAUDE.md + rules + basic skills (plan, review). No agents, no hooks.
- **standard**: Above + agents + workflow skills. No hooks.
- **full**: Everything including hooks and settings.json.

### Phase 3: Post-generation

1. Show a tree of all generated files
2. If hooks were generated, show the settings.json hook registration and remind user to review
3. Suggest next steps:
   - `cd <project> && claude` to start using
   - `/plan` for the first task
   - If Codex: verify `codex --version`
   - If Gemini: verify `gemini` works

## Important rules

- NEVER generate a CLAUDE.md longer than 30 lines
- NEVER include information Claude can infer from reading code
- Always read the template before generating — do not improvise when a template exists
- Adapt templates to the user's specific stack (replace placeholders, adjust patterns)
- Each skill must have proper frontmatter (name, description)
- Each agent must have proper frontmatter (name, description, tools, model)
- Hooks must be executable Python scripts with correct stdin/stdout JSON format
- Follow https://code.claude.com/docs/ja/best-practices strictly
