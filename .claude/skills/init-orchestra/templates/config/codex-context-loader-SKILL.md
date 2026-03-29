---
name: context-loader
description: Load shared knowledge base from .claude/docs/ before starting work
---

# Context Loader

Load shared knowledge base from `.claude/docs/` before starting work.

## On every task
1. Check `.claude/docs/DESIGN.md` for current design decisions
2. Check `.claude/docs/libraries/` for library constraints relevant to the task
3. Check `.claude/docs/research/` for prior investigation results

## Rules
- Reference existing docs before starting new research
- If your work changes a design decision, update DESIGN.md
- If you discover library constraints, add to `libraries/<library-name>.md`
