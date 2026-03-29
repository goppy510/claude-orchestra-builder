---
name: review
description: Multi-reviewer code review for team development
---

# Review (Team)

Parallel multi-reviewer code review using subagents.
Respond to user in Japanese (敬語).

## Workflow

1. Identify changed files (via `git diff` or user specification)
2. Launch 3 review subagents in parallel:

   **Security Reviewer:**
   - Injection vulnerabilities, auth flaws, secrets in code, data exposure

   **Quality Reviewer:**
   - Code correctness, edge cases, performance, style consistency

   **Test Reviewer:**
   - Test coverage, missing edge case tests, test quality

3. Aggregate findings from all reviewers
4. Deduplicate and present grouped by severity:
   - **Critical**: Must fix before merge
   - **Warning**: Should fix
   - **Suggestion**: Nice to have

## Rules
- Each reviewer runs as a separate subagent (isolated context)
- Aggregate results — don't show raw subagent output
- Reference specific lines (`file:line`)
- If reviewers disagree, present both perspectives
