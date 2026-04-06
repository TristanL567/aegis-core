---
name: readme-generator
description: Use this skill when the user asks to generate a README.md file for a project. It analyzes the project context and outputs structured Markdown documentation.
---

# README Generator Minion

## Goal
To create professional, well-structured README.md files for new or existing projects to ensure high-quality documentation.

## Instructions
1. Analyze the user's prompt to determine the project name and core functionality.
2. Draft a README string that includes the following sections:
   - Project Title
   - Description
   - Installation
   - Usage
3. Pass the generated README string as an argument to the `scripts/save_readme.py` script to save it to the disk.
4. Confirm to the user that the file has been generated.

## Constraints
- Do not invent complex installation commands; stick to standard conventions (e.g., `npm install` or `pip install`).
- Never overwrite an existing README.md without asking the user first.