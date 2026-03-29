#!/usr/bin/env python3
"""
PostToolUse hook (Bash): Detects error patterns in command output and
suggests using the codex-debugger agent for root cause analysis.

Register in .claude/settings.json:
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "command": "python3 .claude/hooks/error-to-codex.py",
        "description": "Suggest Codex debugging on error detection"
      }
    ]
  }
}
"""

import json
import re
import sys

ERROR_PATTERNS = [
    r"(?i)(error|exception|traceback|panic|fatal|failed|segfault)",
    r"(?i)(cannot find|not found|no such file|undefined|unresolved)",
    r"(?i)(compilation failed|build failed|test failed)",
    r"exit code [1-9]",
]

# Don't trigger on these (common false positives)
IGNORE_PATTERNS = [
    r"(?i)(error handling|error message|on_error|error\.md)",
    r"(?i)(0 errors|no errors)",
]


def has_error(output: str) -> bool:
    for pattern in IGNORE_PATTERNS:
        if re.search(pattern, output):
            return False

    for pattern in ERROR_PATTERNS:
        if re.search(pattern, output):
            return True

    return False


def main():
    input_data = json.load(sys.stdin)
    tool_response = input_data.get("tool_response", {})
    tool_output = tool_response if isinstance(tool_response, str) else str(tool_response)

    if has_error(tool_output):
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": "[ErrorDetector] Error detected in output. Consider using the codex-assistant agent for root cause analysis.",
            }
        }
    else:
        output = {}

    json.dump(output, sys.stdout)


if __name__ == "__main__":
    main()
