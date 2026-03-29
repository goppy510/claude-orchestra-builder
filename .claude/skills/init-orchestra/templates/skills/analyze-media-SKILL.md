---
name: analyze-media
description: Analyze multimodal content (PDF, images, video, audio) via Gemini
disable-model-invocation: true
---

# Analyze Media

Analyze multimodal content: $ARGUMENTS
Respond to user in Japanese (敬語).

## Workflow

1. Identify file type and validate it's a supported format
2. Delegate to gemini-multimodal agent for extraction
3. Review extracted content for quality and completeness
4. Save structured results to `.claude/docs/extractions/`
5. Present summary to user

## Supported formats
- Documents: PDF, DOCX
- Images: PNG, JPG, SVG, GIF, WebP
- Video: MP4, WebM
- Audio: MP3, WAV

## Rules
- Always save full extraction to docs (multimodal output is typically large)
- For batch processing, process files in parallel using multiple subagents
- If extraction quality is low, retry with a more specific prompt
