# Handoff Feedback Summary Template

**Date:** {{timestamp}}
**Cycle ID:** {{handoff_cycle_id}}
**Stage Completed:** {{active_stage}}
**From:** {{from_llm}}
**To:** {{to_llm}}

---

## 🧭 Overview

This document summarizes the outcomes of a completed dual-LLM governance cycle between Claude and Codex. It represents the closure of one **Intent-Driven Systems Engineering (IDSE)** feedback loop.

---

## 📋 Summary of Work

| Category       | Description                                         |
| -------------- | --------------------------------------------------- |
| Intent         | What was the goal of this cycle?                    |
| Context        | Which environment, repo, or system was affected?    |
| Specification  | Which PRD/spec components were targeted?            |
| Plan           | What implementation strategy was followed?          |
| Tasks          | Which atomic tasks were completed or added?         |
| Implementation | Summary of commits, code, or content created        |
| Feedback       | Issues found, improvements applied, or pending work |

---

## ⚙️ Handoff Details

| Field             | Value                               |
| ----------------- | ----------------------------------- |
| Cycle ID          | {{handoff_cycle_id}}                |
| From LLM          | {{from_llm}}                        |
| To LLM            | {{to_llm}}                          |
| Duration          | {{cycle_duration}}                  |
| Role Changes      | {{role_change_summary}}             |
| Stage Progression | {{previous_stage}} → {{next_stage}} |
| Awaiting Handoff  | false                               |

---

## 🧠 Key Learnings & Improvements

| Category      | Observation | Recommended Action |
| ------------- | ----------- | ------------------ |
| Process       |             |                    |
| Technical     |             |                    |
| Governance    |             |                    |
| Collaboration |             |                    |

---

## 📈 Metrics

| Metric                    | Value                 | Target     | Status                  |
| ------------------------- | --------------------- | ---------- | ----------------------- |
| Test Coverage             | {{coverage_percent}}% | 80%        | ☐ Pass / ☐ Fail         |
| Feedback Cycle Duration   | {{cycle_duration}}    | ≤ 5 min    | ☐ Pass / ☐ Needs Review |
| Artifacts Updated         | {{artifact_count}}    | N/A        | ☐ Validated             |
| Constitutional References | {{articles_cited}}    | Contextual | ☐ Confirmed             |

---

## 🪞 Reflection (Meta)

* Which IDSE principles were applied effectively?
* What governance improvements are suggested for next cycle?
* Any gaps between plan and execution?
* Is a role or stage redefinition required?

---

## ✅ Next Steps

1. Confirm state update in `idse-governance/state/state.json`.
2. Log metrics and observations in `feedback/current/feedback.md`.
3. Update `plan.md` and `tasks.md` as needed for next cycle.
4. Trigger next cycle (`Claude → Codex` or `Codex → Claude`).

> *This summary closes one full IDSE constitutional loop and provides traceable evidence of compliance and progress.*
