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

## Resources

- For template list and mapping, see [templates-reference.md](templates-reference.md)
- For detailed workflow (Phase 1-4), see [workflow-phases.md](workflow-phases.md)
- For generation quality rules, see `@.claude/rules/generation-quality.md`

## Workflow overview

1. **Phase 1: Interview** — Gather project info, AI tool selection, workflow preferences via AskUserQuestion
2. **Phase 2: Generation** — Fetch best practices (`/adjust-best-practice`), copy templates, customize from-scratch files
3. **Phase 3: Validation** — Structure check + best practices audit (`/adjust-best-practice <target-path>`) with interactive fix
4. **Phase 4: Post-generation** — Show file tree, suggest permissions and next steps

## Important rules

- NEVER generate a CLAUDE.md longer than 30 lines
- NEVER include information Claude can infer from reading code
- Copy templates first, then customize — do not improvise when a template exists
- Only generate from scratch: `rules/coding.md` and `rules/testing.md` (language-specific)
- All paths are relative to `<target-path>`, never write outside it
- Each skill must have proper frontmatter (name, description)
- Each agent must have proper frontmatter (name, description, tools, model)
- Hooks must be executable Python scripts with correct stdin/stdout JSON format
- NEVER store API keys, secrets, or credentials in generated project files
- Always generate settings.json with deny rules for sensitive files
- Use `/adjust-best-practice` output to align generated files with latest official best practices
