from __future__ import annotations

from fastapi import APIRouter, HTTPException

from backend.services.git_service import GitService, load_auth_config

router = APIRouter(prefix="/api/git", tags=["git"])


@router.get("/auth/status")
def auth_status():
    """Report configured GitHub auth mode and whether credentials are present."""
    cfg = load_auth_config()
    return {
        "mode": cfg.mode,
        "pat_configured": bool(cfg.pat),
        "app_configured": bool(
            cfg.app_id and cfg.app_private_key and cfg.app_installation_id
        ),
    }


@router.post("/commit")
def commit_artifacts(payload: dict):
    """Commit artifacts to a repository and optionally emit repository_dispatch."""
    required = ["session_id", "project", "repo_url", "branch", "artifacts"]
    missing = [r for r in required if r not in payload]
    if missing:
        raise HTTPException(status_code=400, detail=f"Missing fields: {', '.join(missing)}")

    auth = load_auth_config()
    service = GitService(auth)

    commit_sha = service.commit_artifacts(
        repo_url=payload["repo_url"],
        branch=payload["branch"],
        artifacts=payload["artifacts"],
        session_meta={"session_id": payload["session_id"], "project": payload["project"]},
    )

    webhook_payload = {
        "session_id": payload["session_id"],
        "project": payload["project"],
        "commit_sha": commit_sha,
    }

    dispatched = False
    try:
        dispatched = service.send_repository_dispatch(
            repo_url=payload["repo_url"],
            event_type="agency-update",
            payload=webhook_payload,
        )
    except Exception:
        dispatched = False

    return {
        "commit_sha": commit_sha,
        "repository_dispatch_sent": dispatched,
        "webhook_payload": webhook_payload,
    }
