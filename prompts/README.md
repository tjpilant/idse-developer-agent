# /prompts Overview

This directory is the operational brain of the IDSE Developer Agent. Each
`*.prompt.md` defines a specialized agent role that enforces the IDSE
Constitution through its part of the pipeline:

Intent → Context → Specification → Plan → Tasks → Implementation → Feedback

Instead of one monolithic “AI,” you can split responsibilities into focused
agents with clear scope and guardrails.

## Files and roles
- `intent-agent.prompt.md` — purpose, stakeholders, measurable success, scope,
  risks.
- `context-agent.prompt.md` — environment, stack, scale, constraints,
  compliance, risks.
- `spec-agent.prompt.md` — user stories, functional/non-functional reqs,
  acceptance criteria, assumptions, open questions.
- `plan-agent.prompt.md` — architecture, components, data models, API
  contracts, test strategy, phases; produces `plan.md` + `test-plan.md`.
- `task-agent.prompt.md` — atomic, testable tasks with dependencies and `[P]`
  for parallel-safe items.
- `implementation-agent.prompt.md` — code/tests per plan/tasks; test-first,
  simple, observable; reports deviations.

## How these prompts are used
- **Single Developer Agent:** Dynamically adopt each role as you move through
  the pipeline; prompts are reference contracts. One agent can orchestrate all
  stages without spawning separate roles if preferred.
- **VS Code / Copilot / Workspace:** Embed a prompt as a custom instruction or
  agent config so the AI behaves consistently for that stage.
- **API (OpenAI/Claude/etc.):** Set `system` to a prompt file, then send
  intent/context/spec to get the next artifact (e.g., spec.md).
- **Agency Swarm / LangGraph / CrewAI / AutoGen:** Each prompt is a node; the
  orchestrator passes outputs (files) between nodes in sequence, or a single
  orchestrator agent can “switch hats” by loading the needed prompt per stage.
- **CI/CD:** Call a model with the right prompt to validate an artifact (e.g.,
  “Does `spec.md` comply with `spec-agent.prompt.md`?”).
- **Single Developer Agent:** Dynamically adopt each role as you move through
  the pipeline; prompts are reference contracts.
- **VS Code / Copilot / Workspace:** Embed a prompt as a custom instruction or
  agent config so the AI behaves consistently for that stage.
- **API (OpenAI/Claude/etc.):** Set `system` to a prompt file, then send
  intent/context/spec to get the next artifact (e.g., spec.md).
- **Agency Swarm / LangGraph / CrewAI / AutoGen:** Each prompt is a node; the
  orchestrator passes outputs (files) between nodes in sequence.
- **CI/CD:** Call a model with the right prompt to validate an artifact (e.g.,
  “Does `spec.md` comply with `spec-agent.prompt.md`?”).

## Example flow (notifications feature)
- **Intent Agent:** Produces `intent.md` with purpose, users, measurable success.
- **Context Agent:** Produces `context.md` with stack (Next.js, Node, Redis),
  constraints (GDPR, <2s latency), risks.
- **Spec Agent:** Produces `spec.md` with user stories, requirements,
  acceptance criteria.
- **Plan Agent:** Produces `plan.md` + `test-plan.md` with architecture,
  components, data model, API, tests.
- **Task Agent:** Produces `tasks.md` with atomic tasks and `[P]` markers.
- **Implementation Agent:** Produces code, migrations, tests; reports deviations.

## Why this design is powerful
- **Role specialization:** Clear responsibility per stage.
- **Constitutional compliance:** Guardrails like “no code without a plan.”
- **Traceability/auditability:** Artifacts map to the prompt/agent that created
  them; rerun to validate.
- **Automation-ready:** Modular for orchestration; multi-model friendly.
