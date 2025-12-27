# IDSE Companion Bundle

Use this bundle to consume the IDE Companion without pulling the entire repo.

## Build the bundle
From repo root:
```bash
python scripts/build_companion_bundle.py
```
This creates `companion_bundle/` containing only the Companion files (session reader, utils, guardrails, validators, docs, workflows, agent instructions, cursor rules).

## Use in a project
Option A: Copy the `companion_bundle/` contents into your project under `.idse/`.
Option B: Add this repo as a submodule and reference `companion_bundle/` as the payload.

## Included components
- Session awareness (`session_reader.py`, `utils/doc_reader.py`)
- Sync detection (`utils/sync_detector.py`)
- Hybrid drafts (`utils/template_writer.py`, `docs/hybrid-mode.md`)
- Feedback loop (`utils/feedback_writer.py`, `scripts/pre_commit_check.py`, `docs/feedback-loop.md`)
- Validation (`integrations/claude-skill/scripts/validate_artifacts.py`)
- Guardrails (`guardrails/` + CI self-test)
- Agent instructions (`AGENTS.md`, `CLAUDE.md`)
- Cursor rules (`.cursor/rules/*.mdc`, `.cursor/tasks/governance.py`)
- Dispatch/validation workflows (`.github/workflows/agency-dispatch-validate.yml`, `guardrails-checks.yml`, `validate-and-notify.yml`)
