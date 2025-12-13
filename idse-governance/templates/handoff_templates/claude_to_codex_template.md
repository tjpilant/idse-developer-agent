# Claude → Codex Handoff Template

**Date:** {{timestamp}}
**Cycle ID:** {{handoff_cycle_id}}
**From:** Claude (`claude_code`)
**To:** Codex (`codex_gpt`)
**Stage:** {{active_stage}}

---

## 📋 Summary

* **Purpose:** What was built and why.
* **Files Changed:**

  * `path/to/file1.py` (+45 / -12)
  * `path/to/file2.md` (+10 / -3)
* **PLAN Path:** `docs/plan.md`
* **Risks:** Identify key risks or open questions.

---

## ✅ Review Checklist

| Category | Requirement                                 | Status |
| -------- | ------------------------------------------- | ------ |
| CMS      | No hardcoded IDs, fields, or rules          | ☐      |
| Security | Sensitive data isolated, keys not committed | ☐      |
| Tests    | ≥80% coverage or justified exception        | ☐      |
| Docs     | Updated Plan.md + Feedback.md               | ☐      |

---

## 🧩 Notes for Codex

* Review implementation consistency with PLAN.
* Check all test results and validate file structure.
* Focus review on: {{critical_areas}}

---

**Next Steps:**

1. Perform code review and mark findings in `REVIEW_NOTES.md`.
2. Complete Codex → Claude template when ready.

> *This document is an IDE-level handoff artifact generated under the IDSE Governance Layer.*
