#!/usr/bin/env python3
import json, sys, os, time, tempfile

STATE_PATH = "idse-governance/state/state.json"

def load_state():
    with open(STATE_PATH) as f:
        return json.load(f)

def save_state(data):
    tmp = tempfile.NamedTemporaryFile("w", delete=False)
    json.dump(data, tmp, indent=2)
    tmp.close()
    os.replace(tmp.name, STATE_PATH)

def view():
    print(json.dumps(load_state(), indent=2))

def handoff(frm, to, reason):
    state = load_state()
    state.update({
        "active_llm": to,
        "awaiting_handoff": True,
        "handoff_cycle_id": time.strftime("%Y-%m-%dT%H:%MZ"),
        "last_handoff": {
            "from": frm,
            "to": to,
            "timestamp": time.strftime("%Y-%m-%dT%H:%MZ"),
            "reason": reason
        }
    })
    save_state(state)
    print(f"Handoff recorded: {frm} → {to}")

def role(role_name):
    state = load_state()
    state["role_change_event"] = {
        "role": role_name,
        "timestamp": time.strftime("%Y-%m-%dT%H:%MZ")
    }
    save_state(state)
    print(f"Role changed → {role_name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: governance.py [view|handoff|role]")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "view":
        view()
    elif cmd == "handoff":
        frm, to, *reason = sys.argv[2:]
        handoff(frm, to, " ".join(reason))
    elif cmd == "role":
        role(sys.argv[2])
