# Codex → Claude Handoff Template

**Date:** {{timestamp}}
**Cycle ID:** {{handoff_cycle_id}}
**From:** Codex (`codex_gpt`)
**To:** Claude (`claude_code`)
**Stage:** {{active_stage}}

---

## 📋 Review Summary

* **Reviewed Files:** `list_of_files`
* **Tests Run:** ✅ All passing / ⚠️ Issues found
* **Coverage:** {{coverage_percent}}%
* **Security Check:** Pass / Fail / N/A

---

## 🧠 Observations

| Type          | Description | Suggested Fix |
| ------------- | ----------- | ------------- |
| Logic         |             |               |
| Performance   |             |               |
| Documentation |             |               |

---

## ⚙️ Decision

✅ **Approve** – merge and proceed to next stage
❌ **Request Changes** – see notes above

---

## 🪞 Reflection

* What worked well:
* What can be improved:
* Which IDSE stage should Claude revisit:

---

**Next Steps:**

1. Claude refines Plan and Tasks based on feedback.
2. Update `state.json` → `active_llm = claude_code`.
3. Proceed with next IDSE stage.

> *This document is an IDE-level handoff artifact generated under the IDSE Governance Layer.*
