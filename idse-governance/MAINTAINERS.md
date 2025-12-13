# 🧭 IDSE Governance Layer – Maintainers Guide

> 📂 **File:** `idse-governance/MAINTAINERS.md`
>
> This guide defines the **long-term stewardship, versioning, and update policies** for the IDSE Governance Layer — the coordination system governing Claude ↔ Codex collaboration in VS Code or Cursor.

---

## 🧩 Purpose

The IDSE Governance Layer is a **self-governing automation framework**. To preserve its stability and constitutional compliance, all modifications must follow structured versioning, governance reviews, and regression validation.

This document ensures continuity for future maintainers and agency developers who integrate or extend this system.

---

## 🧭 Stewardship Roles

| Role                                    | Responsibility                                            | Tools / Files                                                        |
| --------------------------------------- | --------------------------------------------------------- | -------------------------------------------------------------------- |
| 🧠 **Lead Maintainer (IDSE Architect)** | Defines direction and ensures constitutional alignment    | `docs/02-idse-constitution.md`, `idse-governance/protocols/`         |
| ⚙️ **Governance Engineer**              | Implements automation, validation, and role/handoff logic | `.cursor/tasks/governance.py`, `.cursor/config/idse-governance.json` |
| 🧪 **QA/Validation Maintainer**         | Tests integrity, schema, and CI compliance                | `.cursor/tasks/validate-idse-layer.sh`, `VALIDATION.md`              |
| 🧾 **Documentation Steward**            | Maintains and syncs internal/external docs                | `README.md`, `AUTOMATION.md`, `QUICK_START.md`                       |
| 🔄 **Release Manager**                  | Handles versioning, changelogs, and releases              | `CHANGELOG.md`, GitHub Releases                                      |

---

## 🧠 Governance Principles

1. **IDSE Constitution Supremacy**
   All changes must conform to `docs/02-idse-constitution.md`. No local modifications may override constitutional principles.

2. **Governance Isolation**
   Governance files belong strictly under `/idse-governance/`.
   Application logic, tools, or agents **must never** write here.

3. **Change Traceability**
   Every modification must be traceable via commit message, timestamp, and linked issue or PR.

4. **Feedback Incorporation**
   All refactors must incorporate user feedback via documented handoff cycles (Claude ↔ Codex).

---

## 🧱 Update Policy

| Type                         | Scope                                           | Frequency   | Review Required                        |
| ---------------------------- | ----------------------------------------------- | ----------- | -------------------------------------- |
| 🔹 **Minor Patch**           | Non-breaking bug fixes, documentation updates   | As needed   | 1 Reviewer                             |
| 🔸 **Feature Update**        | New governance automation or script improvement | Monthly     | 2 Reviewers (1 must be Architect)      |
| ⚙️ **Constitutional Update** | Affects IDSE principles or handoff semantics    | Quarterly   | Full Council (Architect + 2 Reviewers) |
| 🔺 **Breaking Change**       | Alters directory structure or automation logic  | By proposal | IDSE RFC Required                      |

---

## 🧮 Versioning Scheme

The Governance Layer follows **Semantic Versioning (SemVer)** extended with **Governance Suffixes**.

Format: `vMAJOR.MINOR.PATCH-govREV`

| Segment    | Meaning                                                    |
| ---------- | ---------------------------------------------------------- |
| **MAJOR**  | Incompatible governance or protocol changes                |
| **MINOR**  | Backward-compatible improvements                           |
| **PATCH**  | Bug fixes, documentation, or CI improvements               |
| **govREV** | Governance revision cycle counter (e.g., `-gov1`, `-gov2`) |

Example:

```
v1.1.0-gov3
```

Represents: version 1.1.0 of the governance layer, in its third governance revision cycle.

---

## 🧪 Validation Before Merge

Before merging or releasing:

1. Run `bash .cursor/tasks/validate-idse-layer.sh`
2. Confirm no governance artifacts exist in protected paths
3. Validate JSON schema for `state.json`
4. Generate updated `handoff_summary_<cycle_id>.md`
5. Document changes in `CHANGELOG.md`

CI Example:

```yaml
- name: Validate Governance Layer
  run: bash .cursor/tasks/validate-idse-layer.sh
```

---

## 🔄 Release Process

1. **Branching:** Create feature branch: `feature/governance-v1.2`
2. **Testing:** Run local validation + governance.py tests
3. **Review:** Peer review by another maintainer
4. **Version Bump:** Update version in `.cursor/config/idse-governance.json`
5. **Tag Release:**

   ```bash
   git tag -a v1.2.0-gov1 -m "Governance Layer v1.2.0 Release"
   git push origin v1.2.0-gov1
   ```
6. **Publish Docs:** Sync with `/docs/` and GitHub Wiki if enabled

---

## 🧭 Governance Lifecycle Sync

After every official release:

* Update state with new version reference:

  ```bash
  python3 .cursor/tasks/governance.py stage Feedback
  ```
* Regenerate feedback summary to close governance cycle:

  ```bash
  python3 .cursor/tasks/governance.py summarize
  ```

---

## 🛠️ Maintenance Tools

| Tool                                   | Purpose                              |
| -------------------------------------- | ------------------------------------ |
| `.cursor/tasks/governance.py`          | Manage handoffs, roles, and stages   |
| `.cursor/tasks/validate-idse-layer.sh` | Validate governance integrity        |
| `.vscode/tasks.json`                   | Run governance tasks from VS Code    |
| `AUTOMATION.md`                        | Understand internal automation logic |
| `VALIDATION.md`                        | Review QA + CI procedures            |

---

## 🧩 Backup & Recovery

* **State File:** Back up `idse-governance/state/state.json` daily (automated via CI or GitHub Actions).
* **Handoff Feedback:** Retain all `feedback/` files for audit history.
* **Recovery:** If state corruption occurs, restore last valid version and revalidate.

```bash
cp backups/state_2025-12-10.json idse-governance/state/state.json
bash .cursor/tasks/validate-idse-layer.sh
```

---

## 🧠 Governance Succession

In case of maintainer transfer:

1. Add new maintainer to `MAINTAINERS.md`
2. Conduct governance orientation (1-hour walkthrough of this file)
3. Validate operational understanding with `governance.py` dry-run
4. Assign ownership of validation + release tasks

---

## ✅ Summary

The IDSE Governance Layer is a **living constitutional framework** for IDE-level collaboration. Maintenance requires discipline, documentation, and validation at every change.

**You are not maintaining code — you are maintaining law.** ⚖️

> Stewardship means preserving the integrity of governance logic, ensuring Claude and Codex remain guided by the IDSE Constitution — across every repository, every cycle, forever.
