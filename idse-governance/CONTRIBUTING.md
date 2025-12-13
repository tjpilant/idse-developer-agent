# 🤝 Contributing to the IDSE Governance Layer

> 📂 **File:** `idse-governance/CONTRIBUTING.md`
>
> This guide defines the rules, best practices, and constitutional constraints for contributing to the **Intent-Driven Systems Engineering (IDSE) Governance Layer**.
> All contributions must preserve **constitutional integrity**, **role compliance**, and **auditability**.

---

## 🧭 Purpose

The IDSE Governance Layer is not a normal codebase — it is a **constitutional system**. Contributions are accepted only when they enhance clarity, compliance, automation reliability, or developer usability **without violating IDSE principles**.

This guide ensures that all contributors, regardless of role or origin, operate under the same governance logic as Claude and Codex themselves.

---

## 🧱 Core Principles

| Principle                        | Description                                                              |
| -------------------------------- | ------------------------------------------------------------------------ |
| 🧠 **Intent Supremacy**          | Every change must begin with a clearly defined intent and rationale.     |
| ⚖️ **Constitutional Compliance** | No change may contradict or bypass `docs/02-idse-constitution.md`.       |
| 🔒 **Governance Isolation**      | Application code **must never** be written into `/idse-governance/`.     |
| 🔁 **Transparency**              | All state, handoff, and review artifacts must be auditable.              |
| 🧩 **Feedback Incorporation**    | Suggestions must follow a full Claude ↔ Codex review cycle before merge. |

---

## 🧩 Contribution Workflow

### 1️⃣ Identify Intent

Before making any change, clarify intent:

* Why does this update exist?
* What constitutional principle or stage does it serve?
* Is it governance logic, automation, or documentation?

### 2️⃣ Fork and Branch

```bash
git fork https://github.com/tjpilant/idse-developer-agent.git
cd idse-developer-agent
git checkout -b feature/your-feature-name
```

### 3️⃣ Validate Before Edit

Run the validation task to confirm integrity:

```bash
bash .cursor/tasks/validate-idse-layer.sh
```

If validation fails, stop and resolve before proceeding.

### 4️⃣ Make Your Changes

* Add or update files **only under `/idse-governance/`**
* Never modify `src/`, `lib/`, `app/`, or `implementation/`
* If editing automation (`.cursor/tasks/governance.py`), include inline docstrings referencing relevant IDSE Articles.

### 5️⃣ Run Local Tests

```bash
python3 .cursor/tasks/governance.py view
bash .cursor/tasks/validate-idse-layer.sh
```

Ensure the layer validates cleanly and all state files remain atomic.

### 6️⃣ Document the Change

Add a new section to `CHANGELOG.md` using the provided template:

```markdown
## [vX.Y.Z-govN] – YYYY-MM-DD
### Added / Changed / Fixed
- Describe your change here
### Governance Notes
- Cite IDSE articles (e.g., Article IX – Feedback Incorporation)
### Contributors
- @your-handle
```

### 7️⃣ Submit a Pull Request

Push your branch and open a PR:

```bash
git push origin feature/your-feature-name
```

In your PR description, include:

* Purpose of the change
* Validation results (copy terminal output)
* Linked governance documents (if applicable)

---

## 🧩 Review & Approval Process

| Stage                | Reviewer            | Requirements                                      |
| -------------------- | ------------------- | ------------------------------------------------- |
| 🔍 Initial Review    | Governance Engineer | Validate integrity and compliance                 |
| ⚖️ Governance Review | IDSE Architect      | Approve constitutional alignment                  |
| 🧪 QA Validation     | QA Maintainer       | Validate automation and scripts                   |
| ✅ Merge Approval     | Release Manager     | Confirm versioning and documentation completeness |

Each PR must include at least **two reviewer approvals** before merging.

---

## 🧮 Validation Requirements

All contributions must:

* Pass `validate-idse-layer.sh`
* Maintain valid `state/state.json` schema
* Include updated or new tests for `governance.py` (if applicable)
* Maintain directory isolation rules

Validation can be run manually or via CI:

```yaml
- name: Validate IDSE Governance Layer
  run: bash .cursor/tasks/validate-idse-layer.sh
```

---

## ⚙️ Adding New Governance Tools

When adding a new script or automation task:

1. Place file in `.cursor/tasks/`
2. Prefix with a clear name (e.g., `governance_sync.py`)
3. Add inline docstrings with purpose and linked article(s)
4. Register in `AUTOMATION.md` and update `MAINTAINERS.md`

---

## 🧾 Coding Standards

| Rule                     | Description                                                                        |
| ------------------------ | ---------------------------------------------------------------------------------- |
| 🐍 **Python PEP-8**      | All scripts must follow standard style conventions                                 |
| 📚 **Docstrings**        | Every class and method must include a docstring with purpose and article reference |
| 🧪 **Atomic Operations** | Use temp files and atomic writes for all state updates                             |
| ⚡ **Error Handling**     | Use descriptive error messages referencing governance rule violations              |

---

## 🧠 Best Practices

* Use **Claude ↔ Codex handoff templates** to communicate changes between LLM collaborators.
* Always confirm the **active LLM** in `state.json` before editing.
* Include **role and stage context** in your PR description.
* Follow the **7-stage IDSE lifecycle** in all contributions.

---

## 🔒 Prohibited Actions

❌ Writing governance metadata into `/src/`, `/app/`, `/implementation/`
❌ Editing `idse-governance/state/state.json` manually
❌ Bypassing validation scripts before PR submission
❌ Submitting undocumented or unreferenced constitutional changes

Violations will trigger an automatic governance rollback and CI failure.

---

## 🧭 Governance Feedback Loop

After every accepted contribution:

1. Update `GOVERNANCE_HISTORY.md` with a summary of your cycle
2. Increment the governance revision number (`-govN`) in `CHANGELOG.md`
3. Run:

   ```bash
   python3 .cursor/tasks/governance.py summarize
   ```
4. Validate again before final merge.

---

## 🧩 Getting Help

* For general issues: open a GitHub Discussion under **#governance**
* For technical questions: contact the **Governance Engineer** listed in `MAINTAINERS.md`
* For constitutional questions: consult the **IDSE Architect** or read `docs/02-idse-constitution.md`

---

## ✅ Summary

When contributing, remember:

> You are not just editing files — you are participating in a **governed collaboration system**. Every pull request is a governance act.

Keep it constitutional. Keep it auditable. Keep it IDSE.
