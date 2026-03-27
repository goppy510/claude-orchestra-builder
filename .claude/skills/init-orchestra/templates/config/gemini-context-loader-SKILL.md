---
name: context-loader
description: Load shared knowledge base from .claude/docs/ before starting work
---

# Context Loader

Load shared knowledge base from `.claude/docs/` before starting work.

## On every task
1. Check `.claude/docs/DESIGN.md` for current design decisions
2. Check `.claude/docs/research/` for prior extraction and investigation results

## Rules
- Reference existing research before starting new extraction
- Save all extraction results to `research/<topic>.md`
- Use consistent markdown formatting across all research files
