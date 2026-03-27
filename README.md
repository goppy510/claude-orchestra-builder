# Claude Orchestra Builder

Claude Code のオーケストレーション環境をインタラクティブに構築するツール。
`create-next-app` のように対話形式で `.claude/` 配下の設定ファイル一式を生成します。

## Features

- **AI構成選択**: Claude only / +Codex / +Gemini / Full
- **自動化レベル**: minimal / standard / full
- **19テンプレート**: skills, agents, hooks, rules, config を網羅
- **ベストプラクティス準拠**: https://code.claude.com/docs/ja/best-practices
- **ターゲットパス指定**: 任意のプロジェクトに対して生成可能
- **セキュリティ**: 機密ファイルの deny ルール自動生成、APIキーのプロジェクトファイル保存禁止

## Setup

```bash
git clone https://github.com/goppy510/claude-orchestra-builder.git
cd claude-orchestra-builder

# グローバルスキルとして登録（どこからでも /init-orchestra が使えるようになる）
ln -s "$(pwd)/.claude/skills/init-orchestra" ~/.claude/skills/init-orchestra
```

## Usage

任意のディレクトリで Claude Code を起動し、以下を実行:

```
/init-orchestra /path/to/your-project
```

対話形式で以下を聞かれます:

1. **プロジェクト基本情報** — 名前、言語、フレームワーク
2. **AI構成** — Claude only / +Codex / +Gemini / Full
3. **ワークフロー** — ソロ/チーム、CI/CD、用途、自動化レベル
4. **確認** — 生成ファイル一覧を表示後、実行

## Language Policy

生成されるファイル（CLAUDE.md, skills, agents, rules 等）は**すべて英語**で記述されます。

- **英語にする理由**: 日本語に比べてトークン消費が約半分で済み、Claude の指示遵守精度も高い傾向があります。CLAUDE.md は毎セッション読み込まれるため、この差が蓄積します
- **ユーザーとのやり取りは日本語（敬語）** です。Claude への質問、Claude からの回答はすべて日本語で行われます
- コード内のコメントは英語です

つまり「内部処理は英語、対話は日本語」という使い分けです。

## Generated Structure

選択内容に応じて以下のファイルが生成されます:

```
<target-project>/
├── .claude/
│   ├── CLAUDE.md                    # プロジェクト情報 + 共通基盤
│   ├── rules/
│   │   ├── coding.md                # 言語別コーディング規約
│   │   ├── testing.md               # テスト規約
│   │   └── codex-delegation.md      # [Codex] 委譲ルール
│   ├── skills/
│   │   ├── plan/SKILL.md            # 探索→計画→実装
│   │   ├── review/SKILL.md          # コードレビュー (solo/team)
│   │   ├── add-feature/SKILL.md     # [Codex] 複雑度ルーティング
│   │   ├── analyze-media/SKILL.md   # [Gemini] マルチモーダル分析
│   │   └── startproject/SKILL.md    # [Full] フルキックオフ
│   ├── agents/
│   │   ├── codex-assistant.md       # [Codex] 委譲エージェント
│   │   ├── gemini-multimodal.md     # [Gemini] 抽出エージェント
│   │   └── general-purpose.md       # [Standard+] Opus汎用エージェント
│   ├── hooks/
│   │   ├── agent-router.py          # [Full] キーワードルーティング
│   │   └── error-to-codex.py        # [Full+Codex] エラー検出
│   ├── docs/
│   │   ├── DESIGN.md                # [Codex/Gemini] 設計決定追跡
│   │   ├── research/                # [Gemini] 調査結果
│   │   └── libraries/               # [Codex] ライブラリドキュメント
│   └── settings.json                # [Full] パーミッション + フック登録
├── .codex/                          # [Codex]
│   ├── config.toml
│   └── skills/context-loader/
└── .gemini/                         # [Gemini]
    ├── GEMINI.md
    └── skills/context-loader/
```

`[ ]` 内はその構成を選択した場合のみ生成されます。

## Automation Levels

| Level | 内容 |
|-------|------|
| **minimal** | CLAUDE.md + rules + 基本skills (plan, review) |
| **standard** | + agents + ワークフローskills |
| **full** | + hooks + settings.json パーミッション |

## Prerequisites

- [Claude Code](https://claude.ai/download) がインストール済みであること
- Codex を使う場合: `codex` CLI + `OPENAI_API_KEY` 環境変数
- Gemini を使う場合: `gemini` CLI + `GOOGLE_API_KEY` 環境変数

API キーはシェル環境変数に設定してください。プロジェクトファイルには保存しないでください。

```bash
# ~/.zshrc or ~/.bashrc
export OPENAI_API_KEY=sk-...
export GOOGLE_API_KEY=...
```

## References

- [Claude Code Best Practices](https://code.claude.com/docs/ja/best-practices)
- [Skills](https://code.claude.com/docs/ja/skills)
- [Hooks](https://code.claude.com/docs/ja/hooks-guide)
- [Sub-agents](https://code.claude.com/docs/ja/sub-agents)
- [claude-code-orchestra](https://github.com/DeL-TaiseiOzaki/claude-code-orchestra) — 参考にしたマルチエージェントテンプレート
