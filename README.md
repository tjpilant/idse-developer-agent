# IDSE Developer Agent

> **Intent-Driven Systems Engineering (IDSE)**
> Build from purpose. Engineer through context. Deliver with clarity.

This repository defines:

- The **IDSE methodology**
- The **IDSE Developer Agent**
- The **system prompts**, **templates**, and **playbooks**
- The complete knowledge base for an **OpenAI Custom GPT**

IDSE unifies:

- **Intent-first reasoning**
- **Context-aware decision making**
- **Specification-driven development**
- **AI-accelerated structured engineering**

Use this repo when you want a reliable, repeatable way to turn a loosely worded product idea into a concrete specification, implementation plan, and working code with human-in-the-loop checkpoints along the way.

---

# 🔁 IDSE Pipeline

Intent
→ Context
→ Specification
→ Implementation Plan
→ Tasks
→ Implementation
→ Feedback → (loop)

Artifacts:
- `intent.md`
- `context.md`
- `spec.md`
- `plan.md`
- `tasks.md`
- `implementation/`

## Stage-by-stage snapshot

| Stage | Goal | Key questions | Artifact |
| --- | --- | --- | --- |
| Intent | Capture the problem statement, motivation, and constraints. | Why is this being built? What success looks like? | `intent.md` |
| Context | Gather environment, stakeholders, existing systems, and assumptions. | Who depends on this? What integrations exist? | `context.md` |
| Specification | Translate intent + context into requirements and acceptance criteria. | What must be true for this to ship? | `spec.md` |
| Implementation Plan | Choose architecture, outline components, define testing and delivery plan. | How will the work be sequenced? | `plan.md` |
| Tasks | Break the plan into executable steps with ownership and acceptance checks. | What does “done” mean for each task? | `tasks.md` |
| Implementation | Execute tasks, write code/docs, and run validation. | Does the change satisfy intent/spec? | `implementation/` |

Each stage feeds the next; if feedback reveals gaps, loop back to the last stable artifact instead of improvising changes.

---

# 🧠 Developer Agent Role

The Agent acts as:

- Senior Full-Stack Engineer
- Architect
- API & Database Designer
- AI/ML Integrator
- UI/UX-Aware Frontend Developer

It follows IDSE strictly and does not skip pipeline stages.

The agent is optimized for structured collaboration: it writes drafts for every artifact, asks for missing context, proposes plans with explicit trade-offs, and only proceeds once checkpoints are confirmed.

---

# 📘 File Structure

- `docs/` – methodology, constitution, pipeline, agent framework, prompting tips, and implementation patterns
- `prompts/` – system prompt for Custom GPT
- `kb/templates/` – empty shells for all IDSE artifacts to accelerate new projects
- `kb/examples/` – worked examples showing intent → implementation
- `kb/playbooks/` – repeatable operating guides for common scenarios (e.g., feature builds, refactors)
- `.github/workflows/` – quality validation tools

See `docs/03-idse-pipeline.md` for the canonical description of how stages connect, and `docs/05-idse-prompting-guide.md` for how to drive the agent with clear prompts.

---

# 🚀 Using With OpenAI Custom GPT

1. Create a Custom GPT in OpenAI.
2. Paste `prompts/custom-gpt-system-prompt.md` into the Instructions box.
3. Upload everything under:
   - `docs/`
   - `kb/templates/`
   - `kb/examples/`
   - `kb/playbooks/`

This gives the GPT full IDSE-awareness.

### Running the pipeline with the agent

1. **Start with intent** – Provide the product/problem statement, constraints, and success criteria. The agent will draft `intent.md` and ask clarifying questions.
2. **Confirm context** – Answer follow-ups so the agent can produce `context.md` (stakeholders, integrations, assumptions, risks).
3. **Lock the spec** – The agent synthesizes requirements in `spec.md` and attaches acceptance criteria. Review before moving on.
4. **Plan and tasks** – The agent drafts `plan.md` (architecture, sequencing, validation) and `tasks.md` (independent, testable steps). Approve and assign.
5. **Implement with checkpoints** – Code changes land in `implementation/` (or your project repo) with tests and notes on deviations from the spec.
6. **Feedback loop** – If something changes, revisit the upstream artifact instead of patching downstream.

### Tips for great outputs

- Provide examples of desired UX/API/architecture when describing intent.
- Share existing system constraints early (APIs, data models, SLAs) so the plan aligns with reality.
- Ask the agent to compare alternatives when making architectural choices; it will document the rationale.
- Keep `tasks.md` granular so work can be parallelized and verified independently.

---

# 🧭 Getting involved

- **Start a new project** – Copy the templates from `kb/templates/` as a starter kit.
- **Learn the methodology** – Read `docs/01-idse-philosophy.md` and `docs/02-idse-constitution.md` to understand the guiding principles.
- **Follow a walkthrough** – Explore `kb/examples/` to see how intent evolves into a shipped change.
- **Use a playbook** – For common scenarios (feature build, refactor, incident review), start from `kb/playbooks/` and adapt.

Contributions that add examples, playbooks, or refinements to the prompting guide are especially valuable.

---

# 📄 License

MIT License © You
