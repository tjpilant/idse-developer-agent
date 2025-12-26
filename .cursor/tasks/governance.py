from __future__ import annotations

from pathlib import Path

from session_reader import SessionReader
from utils.doc_reader import IDSEDocReader


def show_session_info(base_dir: Path = Path(".")) -> None:
    """Print active session and resolved artifact paths."""
    session = SessionReader.get_active_session(base_dir=base_dir)
    reader = IDSEDocReader(base_dir=base_dir)

    print("\nIDSE Session Status")
    print("-" * 40)

    if not session:
        print("Session: none detected (.idse_active_session.json missing)")
    else:
        print(f"Session: {session.get('session_id')}")
        print(f"Project: {session.get('project')}")
        print(f"Owner: {session.get('owner')}")

    for stage_dir, filename in [
        ("intents", "intent.md"),
        ("contexts", "context.md"),
        ("specs", "spec.md"),
        ("plans", "plan.md"),
        ("tasks", "tasks.md"),
    ]:
        path = reader.resolve(stage_dir, filename)
        label = f"{stage_dir}/{filename}"
        if path:
            print(f"✓ {label}: {path}")
        else:
            print(f"• {label}: not found")


if __name__ == "__main__":
    show_session_info()
