---
name: startproject
description: Full project kickoff — adapts workflow based on available AI tools (Claude/Codex/Gemini)
disable-model-invocation: true
---

# Start Project

Project kickoff workflow: $ARGUMENTS
Respond to user in Japanese (敬語).

This workflow adapts based on available AI tools. Check which agents exist
in `.claude/agents/` to determine the configuration:
- `codex-assistant.md` exists → Codex available
- `gemini-multimodal.md` exists → Gemini available

## Phase 1: Research (background, parallel with Phase 2)

**If Gemini available:**
Launch gemini-multimodal agent in background:
```
Analyze this repository for implementing: $ARGUMENTS
Provide:
1. Repository structure and architecture
2. Relevant existing code and patterns
3. Library/dependency investigation
4. Technical considerations and constraints
5. Recommendations
```
Save results to `.claude/docs/research/$ARGUMENTS.md`

**If Gemini NOT available:**
Launch a general-purpose subagent in background:
- Read project structure, key files, dependencies
- Search for relevant patterns and conventions
- Save findings to `.claude/docs/research/analysis.md`

Do NOT wait for research to complete — proceed to Phase 2 immediately.

## Phase 2: Requirements Interview

Interview the user via AskUserQuestion. Ask one group at a time:

1. **Goal**: What do you want to achieve?
2. **Scope**: What to include and what to explicitly exclude?
3. **Technical requirements**: Specific libraries, patterns, constraints?
4. **Success criteria**: How do we know it's done?

Produce a draft implementation plan from the interview answers.

## Phase 3: Design Review (background)

**If Codex available:**
Launch codex-assistant agent with:
```
Objective: Review this implementation plan for: $ARGUMENTS
Constraints: Must align with existing codebase patterns
Relevant files:
  - .claude/docs/research/ (if Gemini research is ready)
  - Draft plan from Phase 2
Acceptance checks: Identify risks, suggest implementation order, propose refinements
Output format: Structured review with Risk Analysis, Implementation Order, Refinements
```
Save results to `.claude/docs/design-review.md`

**If Codex NOT available:**
Launch a general-purpose subagent:
- Review the draft plan for risks and edge cases
- Check consistency with existing codebase patterns
- Save to `.claude/docs/design-review.md`

## Phase 4: Integration and Approval

Wait for all background tasks (Phase 1 + Phase 3) to complete.

Merge inputs into a unified plan:
- Research findings (Phase 1)
- User requirements (Phase 2)
- Design review feedback (Phase 3)

Enter Plan Mode and present the integrated plan:
- Files to create/modify (with estimated scope per file)
- Implementation order and dependencies
- Risks identified and mitigations
- Tasks breakdown

Save plan to `.claude/docs/plan.md`.
Ask user for approval via AskUserQuestion before proceeding.

## Phase 5: Document Design Decisions

Update `.claude/docs/DESIGN.md` with:
- Date and feature name
- Key design decisions made during planning
- Alternatives considered
- Rationale

This ensures context is preserved for future sessions.

## Phase 6: Implementation

Exit Plan Mode. Implement according to the approved plan:
- Follow the task order from Phase 4
- Run tests after each significant change
- Commit at logical checkpoints
- If scope expands during implementation, pause and re-scope with user

## Phase 7: Review (separate context)

Use `/review` skill for final review.
This runs in a separate subagent context to avoid implementation bias.

**If Codex available:**
Also request a Codex review via codex-assistant agent for a second opinion.

Address any critical findings before finalizing.
Create PR or final commit.

## Rules
- Each phase produces a document in `.claude/docs/`
- Phase 1 and 3 run in background — never block on them during Phase 2
- Get user approval in Phase 4 before any implementation
- If scope is larger than expected at any phase, re-scope with user
- DESIGN.md must be updated before implementation starts
