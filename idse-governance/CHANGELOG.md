# 🧾 IDSE Governance Layer – CHANGELOG

> 📂 **File:** `idse-governance/CHANGELOG.md`
>
> This changelog tracks all major, minor, and governance revisions to the IDSE Governance Layer. Each release reflects an evolution in automation logic, constitutional compliance, and IDE-level governance.

---

## 🧩 Format

Each release follows the format:

```
## [vX.Y.Z-govN] – YYYY-MM-DD
### Added
- New features or files

### Changed
- Updates, improvements, or optimizations

### Fixed
- Bugs or validation corrections

### Governance Notes
- Constitutional article references or governance updates

### Contributors
- @maintainer1, @maintainer2
```

---

## [v1.1.0-gov1] – 2025-12-11

### Added

* 🧠 Full automation layer with `governance.py` (handoff, stage, role automation)
* ⚙️ Validation system with `validate-idse-layer.sh` and `VALIDATION.md`
* 🧩 Documentation suite: `README.md`, `QUICK_START.md`, `AUTOMATION.md`, `MAINTAINERS.md`
* 🧱 Governance templates for dual LLM handoff: `claude_to_codex_template.md`, `codex_to_claude_template.md`, `handoff_feedback_template.md`

### Changed

* Integrated `idse-governance/` boundary enforcement via `.idse-layer`
* Aligned file structure with IDSE Constitution Article III (Governance Isolation)
* Improved CI workflow for validation and schema checks

### Fixed

* Resolved misalignment between stage tracking and role reassignment
* Improved feedback summary generation for multi-cycle operations

### Governance Notes

* 🔖 Article IV – Specification: defines how handoffs include constitutional citations
* 🔖 Article IX – Feedback Incorporation: codified automated feedback summary generation
* 🔒 Layer enforcement ensures `src/`, `lib/`, and `app/` remain free of governance metadata

### Contributors

* @tjpilant (Lead Maintainer)
* IDSE Developer Agent (Automation Author)

---

## [v1.0.0-gov0] – 2025-12-10

### Added

* Initial governance layer bootstrapped under `/idse-governance/`
* Created `.cursor/config/idse-governance.json` for boundary definitions
* Introduced first draft of `handoff_protocol.md`
* Added `state/state.json` schema for IDE-level role and stage tracking

### Governance Notes

* Establishes constitutional foundation for dual-LLM IDE governance
* Introduces governance versioning suffix `-govN` for traceable cycles

### Contributors

* @tjpilant
* IDSE Developer Agent

---

## 📘 Future Governance Cycle Template

### [vX.Y.Z-govN] – YYYY-MM-DD

### Added

* *List new features or governance automation components*

### Changed

* *Describe improvements to existing governance logic*

### Fixed

* *List bugs or validation corrections*

### Governance Notes

* *Include references to relevant IDSE Constitution articles*

### Contributors

* *List maintainers and contributors*

---

> 🧠 **Note:** Each governance revision (`-govN`) represents a full handoff-feedback loop and validation of the governance system itself. Only release after passing all CI and validation checks defined in `VALIDATION.md`.
