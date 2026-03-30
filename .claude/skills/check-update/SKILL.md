---
name: check-update
description: Check for Claude Code updates and show changelog diff in natural language
disable-model-invocation: true
---

# Check Update

Check if a Claude Code update is available and summarize what changed since the current version.
Respond to user in Japanese (敬語).

## Workflow

### Step 1: Check current version and update availability

Run via Bash:
```bash
claude --version
claude update 2>&1
```

If output says "up to date", report the current version and stop.
If an update is available, note the current and latest versions and proceed to Step 2.

### Step 2: Fetch changelog

Use WebFetch to retrieve the official changelog:
- URL: `https://code.claude.com/docs/ja/changelog`
- Extract: all entries between the latest available version and the current version

### Step 3: Summarize changes

Present the diff as a natural language summary organized by:
- **新機能**: New features and additions
- **パフォーマンス改善**: Performance improvements
- **バグ修正**: Notable bug fixes
- **その他**: Other changes

Keep it concise — highlight what matters to a developer, skip trivial fixes.

### Step 4: Ask to update

Ask the user via AskUserQuestion: `アップデートしますか？ (Y/n)`

If yes, run `claude update` via Bash and verify the new version.
If no, end.
