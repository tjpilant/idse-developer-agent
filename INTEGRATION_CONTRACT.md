# IDSE Agency ↔ Companion Integration Contract

This document pins the contract between the Agency service and the Companion (this repo) for the MVP (Phase 0 + Phase 1).

## Session File (Agency → Companion)
Written by Agency in repo root:
```json
{
  "session_id": "cli-1766328748",
  "name": "feature-auth",
  "created_at": 1766328748.0,
  "owner": "tjpilant",
  "project": "MyApp"
}
```

Companion behavior:
- Read-only via `session_reader.py`
- No session creation/switching in Companion

## Artifact Paths
- Session-scoped: `{stage}/projects/{project}/sessions/{session_id}/{filename}`
- Current symlink (Agency-maintained): `{stage}/current/{filename}`
- Simple fallbacks: `{stage}/{filename}` then `{filename}`
- Implemented in `utils/doc_reader.py`

Stage to filename map:
- intents → `intent.md`
- contexts → `context.md`
- specs → `spec.md`
- plans → `plan.md`
- tasks → `tasks.md`

## Webhook Payload (repository_dispatch)
- Event type: `agency-update`
- Payload (minimum):
```json
{
  "session_id": "cli-1766328748",
  "project": "MyApp",
  "commit_sha": "abc123",
  "artifacts_updated": ["spec", "plan"],
  "timestamp": "2025-01-15T10:30:00Z"
}
```
- Rationale: lets CI/IDE show which session changed and validate accordingly.

## Git Commit API (Agency side, Phase 0)
- Endpoint: `POST /api/git/commit`
- Request (minimum):
```json
{
  "session_id": "cli-1766328748",
  "project": "MyApp",
  "repo_url": "https://github.com/user/my-project",
  "branch": "main",
  "artifacts": {
    "spec": "specs/projects/MyApp/sessions/cli-1766328748/spec.md",
    "plan": "plans/projects/MyApp/sessions/cli-1766328748/plan.md"
  }
}
```
- Response (minimum):
```json
{
  "commit_sha": "abc123",
  "repository_dispatch_sent": true,
  "webhook_payload": {
    "session_id": "cli-1766328748",
    "project": "MyApp",
    "commit_sha": "abc123"
  }
}
```

## Companion Packaging Convention
- Recommended: add as submodule at `.idse/`
- Companion tools assume repository root contains `.idse_active_session.json` and stage directories under the working tree.

## CI Scope (MVP)
- Validation-only for now.
- Add `repository_dispatch` handler once Agency emits `agency-update`.
