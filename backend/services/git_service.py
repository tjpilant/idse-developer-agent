from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from github import Github, GithubIntegration, InputGitTreeElement


@dataclass
class GitAuthConfig:
    mode: str  # "pat" or "app"
    pat: Optional[str] = None
    app_id: Optional[str] = None
    app_private_key: Optional[str] = None
    app_installation_id: Optional[str] = None


def load_auth_config() -> GitAuthConfig:
    """Load GitHub auth settings from environment variables."""
    mode = os.getenv("GITHUB_AUTH_MODE", "pat").lower()
    return GitAuthConfig(
        mode=mode,
        pat=os.getenv("GITHUB_PAT"),
        app_id=os.getenv("GITHUB_APP_ID"),
        app_private_key=os.getenv("GITHUB_APP_PRIVATE_KEY"),
        app_installation_id=os.getenv("GITHUB_APP_INSTALLATION_ID"),
    )


class GitService:
    """Lightweight GitHub commit/dispatch helper."""

    def __init__(self, auth: GitAuthConfig):
        self.auth = auth
        self.client = self._build_client(auth)

    def _build_client(self, auth: GitAuthConfig):
        if auth.mode == "pat":
            if not auth.pat:
                raise RuntimeError("GITHUB_PAT missing for pat mode")
            return Github(auth.pat)

        if auth.mode == "app":
            if not (auth.app_id and auth.app_private_key and auth.app_installation_id):
                raise RuntimeError("GitHub App configuration incomplete")
            integ = GithubIntegration(auth.app_id, auth.app_private_key)
            token = integ.get_access_token(int(auth.app_installation_id)).token
            return Github(token)

        raise RuntimeError(f"Unsupported GITHUB_AUTH_MODE: {auth.mode}")

    def _get_repo(self, repo_url: str):
        slug = repo_url.rstrip("/").split("github.com/")[-1]
        return self.client.get_repo(slug)

    def commit_artifacts(
        self,
        repo_url: str,
        branch: str,
        artifacts: dict[str, str],
        session_meta: dict,
        commit_message: Optional[str] = None,
    ) -> str:
        """
        Write artifacts and commit via GitHub API.

        artifacts: mapping alias -> local filesystem path to file contents.
        """
        repo = self._get_repo(repo_url)
        ref = repo.get_git_ref(f"heads/{branch}")
        latest_commit = repo.get_commit(ref.object.sha)
        base_tree = repo.get_git_tree(latest_commit.sha)

        tree_elements = []
        for _, path in artifacts.items():
            file_path = Path(path)
            if not file_path.exists():
                raise FileNotFoundError(f"Artifact not found: {file_path}")
            content = file_path.read_text()
            blob = repo.create_git_blob(content, "utf-8")
            tree_elements.append(
                InputGitTreeElement(
                    path=str(path),
                    mode="100644",
                    type="blob",
                    sha=blob.sha,
                )
            )

        tree = repo.create_git_tree(tree=tree_elements, base_tree=base_tree)
        message = commit_message or f"docs: update IDSE artifacts [{session_meta.get('session_id')}]"
        parent = repo.get_git_commit(latest_commit.sha)
        commit = repo.create_git_commit(message, tree, [parent])
        ref.edit(commit.sha)
        return commit.sha

    def send_repository_dispatch(self, repo_url: str, event_type: str, payload: dict) -> bool:
        repo = self._get_repo(repo_url)
        repo.create_repository_dispatch(event_type, payload)
        return True
