# Claude Projects Integration

Set up IDSE Developer Agent as a Claude Project for persistent, context-aware engineering sessions.

## Why Claude Projects?

- **Persistent Memory**: Claude remembers your project context across conversations
- **Extended Context**: Upload your entire methodology as knowledge
- **File Handling**: Claude can read your uploads and create artifacts
- **Project-Specific**: Keep IDSE methodology isolated to engineering work

## Quick Setup (5 minutes)

### 1. Create the Project

1. Go to [claude.ai](https://claude.ai)
2. Click **Projects** in the sidebar
3. Click **+ New Project**
4. Name it: "IDSE Developer Agent" (or your project name)

### 2. Upload Knowledge Base

Upload these files to **Project Knowledge**:

**Core Methodology (Required):**

```
docs/01-idse-philosophy.md
docs/02-idse-constitution.md
docs/03-idse-pipeline.md
```

**Templates (Required):**

```
kb/templates/intent-template.md
kb/templates/context-template.md
kb/templates/spec-template.md
kb/templates/plan-template.md
kb/templates/tasks-template.md
kb/templates/test-plan-template.md
```

**Reference (Recommended):**

```
docs/04-idse-spec-plan-tasks.md
docs/05-idse-prompting-guide.md
kb/examples/real-time-notifications.md
```

**Playbooks (Optional):**

```
kb/playbooks/full-feature-idse-playbook.md
kb/playbooks/bug-fix.md
kb/playbooks/refactor-under-idse.md
```

### 3. Set Custom Instructions

Go to **Project Settings** → **Custom Instructions** and paste:

```markdown
You are **Developer Agent** implementing **Intent-Driven Systems Engineering (IDSE)**.

## Pipeline
Intent → Context → Specification → Plan → Tasks → Implementation → Feedback

## Core Rules
1. Never skip stages
2. Never generate code without a plan
3. Never generate a plan without a complete specification
4. Mark unclear requirements with [REQUIRES INPUT]

## When Starting New Work
1. Ask what stage we're at or determine from context
2. Check if prior artifacts exist
3. Generate the appropriate artifact using templates from kb/templates/

## Artifact Production
- Use the exact template structure from kb/templates/
- Include generation timestamp
- Mark all unknowns with [REQUIRES INPUT]
- Ensure traceability to prior stages

## Constitution (Always Apply)
Reference docs/02-idse-constitution.md:
- Intent Supremacy: All decisions trace to explicit intent
- Context Alignment: Architecture reflects constraints
- Specification Completeness: No unresolved ambiguities
- Test-First Mandate: Tests before code
- Plan Before Build: No code without plan

## When Asked to Code
1. Verify plan.md exists
2. Verify tasks.md exists
3. Only then proceed with implementation
4. Follow test-first patterns
```

### 4. Start Using It

Begin conversations with context about where you are:

**Starting Fresh:**

> "I want to build [feature/project]. Let's start with the intent."

**Resuming Work:**

> "We're at the Specification stage for [feature]. Here's the intent and context we have..."

**Uploading Existing Artifacts:**

> Upload your current intent.md, context.md, etc. and say:
> "Review these artifacts and help me continue to the next stage."

---

## Workflow Patterns

### Pattern 1: Full Feature Development

```
Session 1: Intent + Context
├── Define what you're building and why
├── Capture environment, constraints, risks
└── Output: intent.md, context.md

Session 2: Specification
├── Upload intent.md and context.md
├── Generate user stories, requirements, acceptance criteria
└── Output: spec.md

Session 3: Planning
├── Upload spec.md
├── Design architecture, components, contracts
└── Output: plan.md, test-plan.md

Session 4: Task Breakdown
├── Upload plan.md
├── Break into atomic, testable tasks
└── Output: tasks.md

Session 5+: Implementation
├── Upload tasks.md and plan.md
├── Implement task by task, test-first
└── Output: Code and tests
```

### Pattern 2: Quick Planning Session

```
Single Session:
├── "I need to add user authentication. Walk me through IDSE."
├── Claude guides through each stage
├── Produces all artifacts in one conversation
└── Copy artifacts to your project
```

### Pattern 3: Review and Refine

```
Upload existing artifacts:
├── "Here's our current spec. Review for completeness."
├── Claude identifies gaps, missing acceptance criteria
├── Resolves [REQUIRES INPUT] markers through discussion
└── Produces refined artifacts
```

---

## Prompt Templates

### Starting Intent Stage

```
I want to build [brief description].

Help me create an intent.md covering:
- Goal and problem we're solving
- Who the stakeholders/users are
- Measurable success criteria
- What's in and out of scope
- Known constraints and risks

Use the intent template format.
```

### Starting Context Stage

```
Based on this intent:
[paste intent.md or upload file]

Help me create context.md covering:
- Our tech stack: [describe]
- Scale expectations: [describe]
- Key integrations: [list]
- Compliance requirements: [list]
- Timeline: [describe]

Identify risks and unknowns I should consider.
```

### Starting Specification Stage

```
Based on our intent and context:
[paste/upload both files]

Generate a specification with:
- User stories
- Functional requirements
- Non-functional requirements
- Acceptance criteria (testable)
- Open questions marked [REQUIRES INPUT]
```

### Starting Plan Stage

```
Based on this specification:
[paste/upload spec.md]

Create an implementation plan covering:
- Architecture summary
- Component breakdown
- Data model
- API contracts
- Test strategy
- Delivery phases
```

### Starting Tasks Stage

```
Based on this plan:
[paste/upload plan.md]

Break down into tasks that are:
- Atomic and independently testable
- Organized by phase
- Marked [P] if parallelizable
- Include owner placeholder and acceptance criteria
```

---

## Tips for Best Results

### Do This ✅

- **Upload files** rather than pasting long content
- **Reference stages explicitly**: "We're at the Spec stage"
- **Iterate within stages**: Refine before moving on
- **Resolve [REQUIRES INPUT]** before advancing
- **Keep artifacts** in your local project for reference

### Avoid This ❌

- **Don't skip stages**: Even if you "know" the solution
- **Don't ask for code first**: Pipeline exists for a reason
- **Don't leave ambiguity**: Resolve unknowns before planning
- **Don't ignore the constitution**: It prevents common failures

---

## Troubleshooting

### Claude isn't using IDSE structure

- Explicitly say: "Use the IDSE methodology"
- Reference: "Follow the pipeline: Intent → Context → Spec → Plan → Tasks"
- Check that docs/02-idse-constitution.md is in Project Knowledge

### Artifacts are too vague

- Ask for specific details: "Include concrete acceptance criteria"
- Reference examples: "Follow the structure in kb/examples/real-time-notifications.md"
- Iterate: "This requirement is too vague. Make it testable."

### Claude wants to jump to code

- Remind: "We need plan.md first. What's the architecture?"
- Check: "Do we have a complete spec with all [REQUIRES INPUT] resolved?"
- Enforce: "Per IDSE constitution, no code without a plan."

### Context is getting lost

- Upload files each session rather than relying on memory
- Summarize current state at session start
- Use Project Knowledge for methodology, upload working artifacts per session