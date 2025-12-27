from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUNDLE_DIR = ROOT / "companion_bundle"

INCLUDE_PATHS = [
    "AGENTS.md",
    "CLAUDE.md",
    "session_reader.py",
    "utils/doc_reader.py",
    "utils/sync_detector.py",
    "utils/template_writer.py",
    "utils/feedback_writer.py",
    "guardrails/",
    "integrations/claude-skill/scripts/validate_artifacts.py",
    ".cursor/rules/",
    ".cursor/tasks/governance.py",
    ".github/workflows/agency-dispatch-validate.yml",
    ".github/workflows/guardrails-checks.yml",
    ".github/workflows/validate-and-notify.yml",
    "scripts/pre_commit_check.py",
    "docs/session-integration.md",
    "docs/hybrid-mode.md",
    "docs/feedback-loop.md",
    "docs/sync-protocol.md",
]


def copy_item(src: Path, dest: Path) -> None:
    if src.is_dir():
        shutil.copytree(src, dest, dirs_exist_ok=True)
    else:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)


def main() -> None:
    if BUNDLE_DIR.exists():
        shutil.rmtree(BUNDLE_DIR)
    BUNDLE_DIR.mkdir(parents=True, exist_ok=True)

    for rel in INCLUDE_PATHS:
        src = ROOT / rel
        if not src.exists():
            print(f"Skipping missing path: {rel}")
            continue
        dest = BUNDLE_DIR / rel
        copy_item(src, dest)
        print(f"Added: {rel}")

    print(f"\nCompanion bundle created at: {BUNDLE_DIR}")


if __name__ == "__main__":
    main()
