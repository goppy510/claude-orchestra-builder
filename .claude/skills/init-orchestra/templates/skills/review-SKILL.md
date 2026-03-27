---
name: review
description: Comprehensive code review for solo developers
---

# Review

Single-pass comprehensive code review.
Respond to user in Japanese (敬語).

## Workflow

1. Identify changed files (via `git diff` or user specification)
2. Review each file for:
   - Correctness and edge cases
   - Security vulnerabilities (injection, auth, data exposure)
   - Performance issues
   - Code style and consistency with project conventions
   - Test coverage gaps
3. Present findings grouped by severity:
   - **Critical**: Must fix before merge
   - **Warning**: Should fix, but not blocking
   - **Suggestion**: Nice to have improvements

## Rules
- Use subagents for review to keep main context clean
- Reference specific lines (`file:line`)
- Suggest concrete fixes, not just descriptions of problems
- If no issues found, say so — don't invent problems
