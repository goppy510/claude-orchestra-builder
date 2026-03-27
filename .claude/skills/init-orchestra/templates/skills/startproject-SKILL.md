---
name: startproject
description: Full project kickoff — analysis, research, design, implement, review
disable-model-invocation: true
---

# Start Project

Full project kickoff workflow: $ARGUMENTS
Respond to user in Japanese (敬語).

## Workflow

### Phase 1: Analysis
Use a subagent to analyze the existing codebase:
- Project structure and architecture
- Key patterns and conventions
- Dependencies and build system
- Save findings to `.claude/docs/analysis.md`

### Phase 2: Research & Design (parallel)
Launch subagents in parallel:

**Researcher:**
- Investigate relevant libraries, APIs, best practices
- Save to `.claude/docs/research.md`

**Architect:**
- Design implementation plan based on codebase analysis
- Identify files to create/modify
- Save to `.claude/docs/design.md`

### Phase 3: Plan Integration
- Merge research and design into a unified implementation plan
- Present to user for approval via AskUserQuestion
- Save approved plan to `.claude/docs/plan.md`

### Phase 4: Implementation
- Use `/team-implement` pattern if available, or implement sequentially
- Run tests after each module
- Commit at logical checkpoints

### Phase 5: Review
- Use `/review` skill for final review
- Address any critical findings
- Create PR or final commit

## Rules
- Each phase produces a document in `.claude/docs/`
- Get user approval before moving from Phase 3 to Phase 4
- If any phase reveals scope is larger than expected, re-scope with user
