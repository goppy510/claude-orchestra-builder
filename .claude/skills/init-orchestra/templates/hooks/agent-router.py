#!/usr/bin/env python3
"""
UserPromptSubmit hook: Analyzes user input and suggests routing to the
appropriate agent (Codex / Gemini / Opus subagent).

Register in .claude/settings.json:
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "command": "python3 .claude/hooks/agent-router.py",
        "description": "Suggest agent routing based on prompt keywords"
      }
    ]
  }
}
"""

import json
import re
import sys


# --- Routing rules (customize per project) ---

CODEX_KEYWORDS = [
    r"\b(design|architect|plan|debug|tradeoff|compare|analyze error)\b",
    r"\b(設計|計画|デバッグ|比較|分析)\b",
]

GEMINI_KEYWORDS = [
    r"\b(pdf|image|video|audio|screenshot|diagram|photo)\b",
    r"\b(画像|動画|音声|PDF|スクリーンショット)\b",
]

GEMINI_EXTENSIONS = [
    r"\.(pdf|png|jpg|jpeg|gif|mp4|mp3|wav|webm|svg)$",
]


def detect_route(prompt: str) -> str | None:
    text = prompt.lower()

    for pattern in GEMINI_EXTENSIONS:
        if re.search(pattern, text):
            return "gemini"

    for pattern in GEMINI_KEYWORDS:
        if re.search(pattern, text, re.IGNORECASE):
            return "gemini"

    for pattern in CODEX_KEYWORDS:
        if re.search(pattern, text, re.IGNORECASE):
            return "codex"

    return None


def main():
    input_data = json.load(sys.stdin)
    prompt = input_data.get("user_prompt", "")

    route = detect_route(prompt)

    if route == "codex":
        output = {
            "decision": "allow",
            "reason": "[Router] This looks like a design/debug task. Consider using the codex-assistant agent.",
        }
    elif route == "gemini":
        output = {
            "decision": "allow",
            "reason": "[Router] Multimodal content detected. Consider using the gemini-multimodal agent.",
        }
    else:
        output = {"decision": "allow"}

    json.dump(output, sys.stdout)


if __name__ == "__main__":
    main()
