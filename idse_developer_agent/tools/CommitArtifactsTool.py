from __future__ import annotations

import requests


class CommitArtifactsTool:
    """Agency tool to commit generated artifacts and trigger repository dispatch."""

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def run(self, session_id: str, project: str, repo_url: str, branch: str, artifacts: dict):
        resp = requests.post(
            f"{self.base_url}/api/git/commit",
            json={
                "session_id": session_id,
                "project": project,
                "repo_url": repo_url,
                "branch": branch,
                "artifacts": artifacts,
            },
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()
