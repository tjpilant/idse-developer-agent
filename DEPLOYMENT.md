# IDSE Developer Agent Deployment Guide

This guide covers three ways to deploy the IDSE Developer Agent:

1. **Claude.ai Projects/Skills** — Full agent in Claude's web interface
2. **OpenAI Custom GPT** — Full agent in ChatGPT
3. **VS Code / Cursor / Claude Code** — Local IDE integration

Each mode provides the same IDSE methodology; choose based on your workflow.

---

## Mode 1: Claude.ai Projects

Best for: Ongoing projects where you want Claude to remember context across sessions.

### Option A: Claude Project (Recommended)

1. **Create a Project** in claude.ai

2. **Upload to Project Knowledge:**

   ```
   docs/01-idse-philosophy.md
   docs/02-idse-constitution.md
   docs/03-idse-pipeline.md
   docs/04-idse-agents.md
   docs/04-idse-spec-plan-tasks.md
   kb/templates/*.md (all templates)
   kb/examples/real-time-notifications.md
   ```

3. **Set Custom Instructions** (Project Settings):

   ```
   You are Developer Agent implementing Intent-Driven Systems Engineering (IDSE).
   
   Pipeline: Intent → Context → Specification → Plan → Tasks → Implementation → Feedback
   
   Never skip stages. Never generate code without a plan. Never plan without a complete specification.
   
   Follow the IDSE Constitution in docs/02-idse-constitution.md.
   Use templates from kb/templates/ when generating artifacts.
   Mark unclear requirements with [REQUIRES INPUT].
   ```

4. **Start conversations** in the project — Claude will reference the methodology.

### Option B: Claude Skill

1. **Package the skill:**

   ```bash
   cd integrations/claude-skill
   zip -r idse-developer-agent.skill SKILL.md scripts/ 
   ```

2. **Upload** to Claude.ai Settings → Features → Skills

3. **Trigger** by saying "help me plan a feature" or "use IDSE methodology"

---

## Mode 2: OpenAI Custom GPT

Best for: Shareable agent that others can use without setup.

### Setup

1. **Create Custom GPT** at chat.openai.com/gpts/editor

2. **Paste Instructions** from `prompts/custom-gpt-system-prompt.md`

3. **Upload Knowledge Files:**

   ```
   docs/01-idse-philosophy.md
   docs/02-idse-constitution.md
   docs/03-idse-pipeline.md
   docs/04-idse-spec-plan-tasks.md
   docs/05-idse-prompting-guide.md
   kb/templates/*.md
   kb/examples/real-time-notifications.md
   kb/playbooks/*.md
   ```

4. **Optional: Add GitHub Action** for live repo access:

   - Import `actions/github-repo-reader.yaml` in the Actions tab
   - Set User-Agent to `idse-dev-agent`
   - Add a PAT for private repos (leave blank for public)

### Usage

Start with prompts like:

- "I want to build [feature]. Help me create the intent."
- "Here's my context. Generate the specification."
- "Review this spec and create an implementation plan."

---

## Mode 3: VS Code / Cursor / Claude Code

Best for: Active development where you're writing code alongside planning.

### Option A: Claude Code (Recommended)

1. **Clone the repo** into your project or as a submodule:

   ```bash
   git clone https://github.com/tjpilant/idse-developer-agent.git .idse
   # or as submodule:
   git submodule add https://github.com/tjpilant/idse-developer-agent.git .idse
   ```

2. **Start Claude Code:**

   ```bash
   claude
   ```

3. **Claude reads AGENTS.md** automatically and can reference all docs.

4. **Use the scripts:**

   ```bash
   python .idse/integrations/claude-skill/scripts/generate_artifact.py intent -o ./artifacts/intent.md
   python .idse/integrations/claude-skill/scripts/validate_artifacts.py ./artifacts/
   ```

### Option B: Cursor with Rules

1. **Clone/submodule** the repo as above

2. **Create `.cursorrules`** in your project root:

   ```markdown
   You are operating under IDSE (Intent-Driven Systems Engineering) methodology.
   
   Pipeline: Intent → Context → Specification → Plan → Tasks → Implementation → Feedback
   
   Rules:
   - Never write code without plan.md and tasks.md existing
   - Reference .idse/docs/02-idse-constitution.md for guardrails
   - Use templates from .idse/kb/templates/ when creating artifacts
   - Mark unclear requirements with [REQUIRES INPUT]
   - Follow test-first patterns
   
   When asked to implement features:
   1. Check if intent.md exists, if not, create it first
   2. Check if context.md exists, if not, create it first
   3. Check if spec.md exists, if not, create it first
   4. Check if plan.md exists, if not, create it first
   5. Check if tasks.md exists, if not, create it first
   6. Only then proceed with implementation
   ```

### Option C: VS Code Tasks

Use the existing `.vscode/tasks.json` in the repo:

1. **Copy governance files** to your project:

   ```bash
   cp -r idse-developer-agent/.vscode ./
   cp -r idse-developer-agent/.cursor ./
   cp idse-developer-agent/.idse-layer ./
   ```

2. **Run tasks** via Command Palette → "Tasks: Run Task":

   - View IDSE State
   - Validate IDSE Governance Layer
   - Handoff to Codex / Handoff to Claude (for dual-agent workflows)

---

## Script Reference

### generate_artifact.py

Generate IDSE artifact templates:

```bash
python scripts/generate_artifact.py <stage> [--output <path>]

# Stages: intent, context, spec, plan, tasks, test-plan

# Examples:
python scripts/generate_artifact.py intent -o ./artifacts/intent.md
python scripts/generate_artifact.py spec  # prints to stdout
python scripts/generate_artifact.py --list-templates  # show template locations
```

The script:

- Uses templates from `kb/templates/` if found in repo
- Falls back to embedded templates if not
- Adds `[REQUIRES INPUT]` markers for fields you need to fill

### validate_artifacts.py

Check artifacts for completeness:

```bash
python scripts/validate_artifacts.py <directory> [--json] [--check-ready]

# Examples:
python scripts/validate_artifacts.py ./artifacts/
python scripts/validate_artifacts.py . --json
python scripts/validate_artifacts.py . --check-ready  # outputs next stage name
```

Output shows:

- Pipeline status (which stages exist and are complete)
- Unresolved `[REQUIRES INPUT]` markers with line numbers
- Next stage ready for work
- Blockers if dependencies aren't satisfied

---

## Workflow Example

Regardless of deployment mode, the workflow is the same:

```
1. Start with Intent
   "I want to add real-time notifications to my app"
   → Generate intent.md with goals, success criteria, scope

2. Capture Context
   "Stack is Next.js + Node + Postgres, 5k users, GDPR compliant"
   → Generate context.md with constraints, risks, integrations

3. Create Specification
   → Generate spec.md with user stories, requirements, acceptance criteria
   → Resolve all [REQUIRES INPUT] before proceeding

4. Plan Implementation
   → Generate plan.md with architecture, components, API contracts
   → Generate test-plan.md with testing strategy

5. Break into Tasks
   → Generate tasks.md with atomic, testable work items
   → Mark parallelizable tasks with [P]

6. Implement
   → Write code and tests following the plan
   → Update artifacts if deviations occur

7. Feedback Loop
   → Production learnings update intent/context/spec
   → Cycle continues
```

---

## Choosing Your Mode

| Mode                    | Best For           | Pros                                                  | Cons                                 |
| ----------------------- | ------------------ | ----------------------------------------------------- | ------------------------------------ |
| **Claude Project**      | Ongoing projects   | Persistent memory, file uploads, extended context     | Requires claude.ai Pro               |
| **Custom GPT**          | Sharing with team  | Easy to share, no setup for users                     | Limited context, no file persistence |
| **VS Code/Claude Code** | Active development | Full repo access, real file creation, IDE integration | Requires local setup                 |

**Recommendation:** Use Claude Code or Cursor for active development, Claude Projects for planning sessions, Custom GPT for team access without setup.

---

## Troubleshooting

### "Claude isn't following IDSE stages"

- Explicitly mention "use IDSE methodology" or "follow the IDSE pipeline"
- Reference specific stages: "We're at the Specification stage"
- Upload/reference the constitution document

### "Scripts can't find templates"

- Run from repo root or ensure `kb/templates/` is in a parent directory
- Scripts fall back to embedded templates if repo structure isn't found

### "Validation shows unresolved markers"

- This is expected! Fill in the `[REQUIRES INPUT]` sections
- Don't proceed to next stage until resolved

### "Custom GPT doesn't have enough context"

- Upload more documents to the knowledge base
- Use the GitHub Action to fetch files dynamically
- Consider using Claude Projects for larger contexts