---
name: plan
description: Explore, plan, then implement — structured workflow per best practices
---

# Plan

Structured workflow: Explore → Plan → Implement → Verify.
Respond to user in Japanese (敬語).

## Workflow

### Step 1: Explore (Plan Mode)
- Read relevant files and understand current state
- Do NOT make any changes
- Summarize findings in 3-5 bullets

### Step 2: Plan
- Create a detailed implementation plan
- List files to modify and the nature of each change
- Identify risks and edge cases
- Present plan to user for approval via AskUserQuestion

### Step 3: Implement
- Switch to Normal Mode
- Follow the approved plan step by step
- Run tests after each significant change

### Step 4: Verify
- Run the full test suite
- Run linter/type checker
- Summarize what was done and what to verify manually

## Rules
- Skip planning for trivial changes (typos, single-line fixes)
- If plan changes during implementation, update user before continuing
- Save the plan to `.claude/docs/plan-<topic>.md` if it exceeds 10 lines
