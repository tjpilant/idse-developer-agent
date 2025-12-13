# Contributing to IDSE Developer Agent

> 🧠 **Note:**  
> This document governs contributions to the **IDSE Developer Agent repository**.  
> For the internal governance subsystem (automation scripts, handoffs, and state management),  
> see [`idse-governance/CONTRIBUTING.md`](idse-governance/CONTRIBUTING.md).

Thanks for your interest in improving IDSE. This project uses the Intent-Driven Systems Engineering pipeline to keep contributions consistent, testable, and traceable.

## How to Propose Work
- Open an issue using `.github/ISSUE_TEMPLATE.md` and provide intent, context, stage, and details.
- For feature work, outline the planned IDSE artifacts (spec, plan, tasks) before implementation.

## Development Workflow
- Follow the IDSE stages: Intent → Context → Specification → Plan → Tasks → Implementation → Feedback.
- Keep artifacts up to date under `kb/` as you progress.
- Use the templates in `kb/templates/` to ensure consistent formatting.
- Avoid leaving unresolved markers in committed files; use `[REQUIRES INPUT]` sparingly and replace before merge.

## Pull Requests
- Reference the related issue and IDSE stage(s).
- Summarize which artifacts were updated (Intent, Context, Spec, Plan, Tasks).
- Add or update tests where relevant; prefer test-first changes.
- Run `rg -n "\[NEEDS CLARIFICATION\]" docs kb` to confirm no old markers remain.
- CI: ensure `Validate IDSE KB` passes.

## Code Style
- Favor clarity over abstraction; keep changes cohesive and scoped.
- Document complex reasoning with concise comments when necessary.
- Maintain ASCII in source unless existing files already use other characters.

## Security
- Do not include sensitive data in issues or PRs.
- Report vulnerabilities privately as described in `SECURITY.md`.

---

## Governance Layer Contributions

If your contribution affects any of the following files:
- `.cursor/tasks/governance.py`
- `.cursor/tasks/validate-idse-layer.sh`
- Any file under `idse-governance/`
- VS Code task integrations or governance configs

You must follow the specialized governance contribution process:
- Read [`idse-governance/CONTRIBUTING.md`](idse-governance/CONTRIBUTING.md)
- Pass all governance validation tests before submitting a PR
- Reference constitutional articles in your PR summary when relevant
