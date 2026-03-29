---
name: add-feature
description: Add a new feature with complexity-based routing (Codex-assisted)
disable-model-invocation: true
---

# Add Feature

Implement a new feature: $ARGUMENTS
Respond to user in Japanese (敬語).

## Workflow

### Step 1: Scope analysis
Use a subagent to analyze the feature scope:
- List files that need to change
- Classify complexity:
  - **SIMPLE** (1-3 files): Implement directly
  - **MODERATE** (3-5 files): Codex-assisted design, then implement
  - **COMPLEX** (5+ files): Codex-first design and planning

### Step 2: Route by complexity

**SIMPLE:**
1. Implement changes directly
2. Write tests
3. Run tests and lint

**MODERATE:**
1. Ask Codex for design review via codex-assistant agent
2. Implement based on Codex recommendations
3. Write tests
4. Run tests and lint

**COMPLEX:**
1. Ask Codex for full design plan via codex-assistant agent
2. Present plan to user for approval
3. Implement in phases, running tests after each phase
4. Final Codex review of complete implementation

### Step 3: Verify
- Run full test suite
- Run linter/type checker
- Summarize changes for commit message
