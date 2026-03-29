---
name: search-best-practice
description: Fetch and analyze official Claude Code best practices docs to inform skills, hooks, rules, and agent configuration
---

# Search Best Practice

Fetch official Claude Code documentation, extract actionable patterns, and apply them to project configuration.
Respond to user in Japanese (敬語). Analysis output in Japanese.

## Usage

```
/search-best-practice                  # Fetch and summarize all best practices
/search-best-practice <topic>          # Focus: skills, hooks, agents, rules, permissions
/search-best-practice <project-path>   # Audit project config against best practices
```

When called from another skill (e.g., init-orchestra), `$ARGUMENTS` may contain a topic or path.

## Documentation Sources

Fetch these pages via WebFetch (launch in parallel where possible):

| Page | URL |
|------|-----|
| Best practices | `https://code.claude.com/docs/ja/best-practices` |
| Skills | `https://code.claude.com/docs/ja/skills` |
| Hooks | `https://code.claude.com/docs/ja/hooks-guide` |
| Sub-agents | `https://code.claude.com/docs/ja/sub-agents` |
| Permissions | `https://code.claude.com/docs/ja/permissions` |
| Features overview | `https://code.claude.com/docs/ja/features-overview` |

## Workflow

### Step 1: Determine mode

Parse `$ARGUMENTS`:
- Empty → **summary mode** (fetch all, summarize)
- Known topic (`skills`, `hooks`, `agents`, `rules`, `permissions`) → **topic mode** (fetch relevant subset)
- Existing directory path → **audit mode** (fetch all + analyze project)

### Step 2: Fetch documentation

Use WebFetch to retrieve pages. In topic mode, fetch only relevant pages:
- `skills` → best-practices + skills
- `hooks` → best-practices + hooks-guide
- `agents` → best-practices + sub-agents
- `rules` → best-practices
- `permissions` → best-practices + permissions

### Step 3: Extract patterns

From fetched content, extract and organize by category:

- **CLAUDE.md**: structure, what to include/exclude, size constraints
- **Skills**: frontmatter requirements, workflow patterns, when to use `disable-model-invocation`
- **Hooks**: event types, stdin/stdout format, performance constraints
- **Agents**: tool restrictions, model selection, role scoping
- **Rules**: content guidelines, file size, what belongs in rules vs CLAUDE.md
- **Permissions**: deny patterns, security best practices

### Step 4: Present or apply

**Summary/Topic mode**: Present extracted patterns as a structured report with:
- Key principles (箇条書き)
- Common patterns with examples
- Anti-patterns to avoid

**Audit mode**: Read the target project's `.claude/` directory and compare against best practices:
1. Read existing CLAUDE.md, rules/, skills/, agents/, hooks/ if present
2. Compare each against extracted patterns
3. Report findings as: conformant / needs improvement / missing
4. Suggest specific fixes with code examples

## Output format (audit mode)

```
## 監査結果: <project-path>

### ✓ 準拠項目
- ...

### △ 改善推奨
- [ファイル]: 問題の説明 → 推奨する修正

### ✗ 未対応
- [カテゴリ]: 推奨される設定
```

## Important rules

- Always fetch live documentation — never rely on cached or assumed content
- Keep analysis actionable: every finding should have a clear recommendation
- In audit mode, do not modify files — only report and suggest
- When called from init-orchestra, return structured findings for the caller to apply
