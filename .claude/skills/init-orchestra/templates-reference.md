# Template Reference

Source: `@.claude/skills/init-orchestra/templates/`

## CLAUDE.md composition
The target CLAUDE.md is assembled from two layers:
1. `@templates/config/CLAUDE.md.template` — project-specific (name, description, commands). Replace `{{placeholders}}`.
2. `@templates/config/CLAUDE.md.base` — shared foundation (language policy, references, principles). Copy as-is.

Merge: template (top) + base (bottom). Final result must be under 30 lines.

## File templates

| Template | Target (relative to target-path) | When |
|----------|--------|------|
| `@templates/skills/plan-SKILL.md` | `.claude/skills/plan/SKILL.md` | Always |
| `@templates/skills/review-SKILL.md` | `.claude/skills/review/SKILL.md` | Single session |
| `@templates/skills/review-team-SKILL.md` | `.claude/skills/review/SKILL.md` | Multi-agent |
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
