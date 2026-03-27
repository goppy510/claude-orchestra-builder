# Generation Quality Rules

## File size limits
- CLAUDE.md: max 30 lines
- rules/*.md: max 20 lines each
- skills/*/SKILL.md: max 80 lines each
- agents/*.md: max 40 lines each

## CLAUDE.md constraints
- Only include what Claude cannot infer from reading the code
- Must include: project name, language policy, build/test commands
- Must NOT include: code style rules (use rules/), workflows (use skills/), detailed docs (use docs/)
- Link to best practices URL, don't duplicate its content

## Skills constraints
- Must have frontmatter: name, description
- Add `disable-model-invocation: true` for skills with side effects
- One clear workflow per skill — don't combine unrelated tasks
- End with verification step when possible

## Agents constraints
- Must have frontmatter: name, description, tools, model
- Restrict tools to minimum needed (principle of least privilege)
- Include clear role definition and output format expectations

## Hooks constraints
- Must be executable (`#!/usr/bin/env python3`)
- Read input from stdin (JSON), write output to stdout (JSON)
- Keep simple — hooks run on every matching event
- Never block on network calls or long computations

## Language
- All generated files: English
- Skill descriptions in frontmatter: English
- User responses during generation: Japanese
