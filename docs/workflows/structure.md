# Repository Guide

This repository is the working space for the Order of Reason channel.

Purpose:

- Keep files easy to find
- Prevent duplication
- Separate unrelated work
- Stay scalable without clutter

---

## FOLDER RESPONSIBILITIES

<u>**brand/**</u>  `# Channel identity assets.`

Contains:

- Logo
- Banner
- Watermark
- Thumbnail templates

Each folder holds:

- Source code (Manim / scripts)
- Final images

---

<u>**videos/**</u>  `# Actual channel content.`

Split by format:

- videos/longform/
- videos/shortform/

Each video gets one folder:

- video-001-topic/
  - `scene.py`
  - `render.mp4`
  - `notes.md`

---

<u>**animations/**</u>  `# Reusable visual components.`

Contains items reused across multiple videos:

- Intro
- Outro
- Transitions
- Generic visual helpers

Subfolders:

- reusable/     → Stable components
- experiments/  → Tests / prototypes

---

<u>**code/**</u>  `# Reusable logic & tooling.`

Contains:

- Utilities
- Libraries
- Experiments

Examples:

- Rendering scripts
- Compression helpers
- Shared math functions

Rule:
Non-visual helpers live here.

---

<u>**assets/**</u>  `# Shared media resources.`

Contains:

- Audio
- Images
- Textures
- Misc resources

---

<u>**docs/**</u>  `# Planning & organization.`

Contains:

- Scripts
- Workflows

---
