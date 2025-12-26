# AGENTS.md

This file provides guidelines to AI agents and human contributors working with the **IDSE Developer Agent** project.

## 1. Project Overview
This repository defines the **Intent‑Driven Systems Engineering (IDSE)** methodology and its primary implementation, the **IDSE Developer Agent**. It contains:
- The IDSE philosophy, pipeline, and constitution in `docs/`.
- System prompts and templates for creating custom GPTs in `prompts/` and `kb/templates/`.
- Example workflows and playbooks in `kb/examples/` and `kb/playbooks/`.
The Agent helps engineers move from high‑level intent to structured specifications, plans, tasks, and ultimately implementation.

## 2. Build and Test Commands
This project is documentation‑heavy and does not compile code. The main checks you can run are:
- **Validation Check:** Ensure no unresolved placeholders remain by running the GitHub Action (it executes `grep` to confirm there are no `[REQUIRES INPUT]` markers in docs/kb).
- **Templates:** Use the files under `kb/templates/` as the basis for new Intent, Context, Specification, Plan and Tasks documents. 

Because there is no application code here, there are no build or runtime steps. If you incorporate code in future (e.g., CLI tooling), describe how to install dependencies and run it in this section.

## 3. Code Style Guidelines
- **Markdown:** Follow standard Markdown syntax. Keep line lengths to <80 chars where possible. Use headings (`##`) to structure sections.  
- **PptxGenJS (if adding slides):** Use the provided `answer.js` and respect the slide guidelines (light theme, meaningful images, no leftover template slides).  
- **YAML/CI:** Keep YAML indented with 2 spaces per level; avoid tabs.  
- **JSON:** Indent with 2 spaces; never add trailing commas.

## 4. Testing Instructions
- Pull requests must pass the **validate-kb** GitHub Action. This action checks that no `[REQUIRES INPUT]` placeholders remain in `docs/` or `kb/`.  
- If adding new templates or examples, run the action locally by executing:
  ```bash
  grep -R "\[REQUIRES INPUT\]" -n kb/ docs/ || echo "✔ No unresolved placeholders."
