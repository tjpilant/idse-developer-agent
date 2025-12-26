# IDE Integration (VS Code / Cursor / Claude Code)

Integrate IDSE Developer Agent directly into your development environment for real-time, file-based engineering workflows.

## Why IDE Integration?

- **Real Files**: Create actual artifacts in your project
- **Full Context**: AI sees your entire codebase
- **Immediate Use**: No copy-paste between chat and editor
- **Version Control**: Artifacts live in git with your code
- **Dual-Agent**: Optional Claude ↔ Codex governance workflows

## Integration Options

| Tool                   | Best For                              | Setup Effort |
| ---------------------- | ------------------------------------- | ------------ |
| **Claude Code**        | Full IDSE workflow with file creation | Low          |
| **Cursor**             | AI-assisted coding with IDSE rules    | Medium       |
| **VS Code + Copilot**  | Existing Copilot users                | Medium       |
| **VS Code + Continue** | Open-source AI integration            | Medium       |

---

## Option 1: Claude Code (Recommended)

Claude Code automatically reads `AGENTS.md` and can access all repo files.

### Setup

1. **Add IDSE to your project:**

   ```bash
   # As a subdirectory
   git clone https://github.com/tjpilant/idse-developer-agent.git .idse
   
   # Or as a git submodule (keeps it updatable)
   git submodule add https://github.com/tjpilant/idse-developer-agent.git .idse
   ```

2. **Create project AGENTS.md** (or append to existing):

   ```bash
   cat >> AGENTS.md << 'EOF'
   
   ## IDSE Methodology
   
   This project uses Intent-Driven Systems Engineering. See `.idse/` for full methodology.
   
   **Pipeline:** Intent → Context → Specification → Plan → Tasks → Implementation
   
   **Rules:**
   - Never write code without plan.md existing
   - Never create plan without spec.md existing  
   - Mark unclear requirements with [REQUIRES INPUT]
   - Reference `.idse/docs/02-idse-constitution.md` for guardrails
   - Use templates from `.idse/kb/templates/`
   
   **Artifacts Location:** `./artifacts/` or project root
   EOF
   ```

3. **Start Claude Code:**

   ```bash
   cd your-project
   claude
   ```

4. **Use IDSE commands:**

   ```
   > Create an intent.md for adding user authentication
   > Generate the context based on our codebase
   > Review spec.md and check for completeness
   > Break plan.md into tasks
   ```

### Using the Scripts

```bash
# Generate artifact templates
python .idse/integrations/claude-skill/scripts/generate_artifact.py intent -o ./artifacts/intent.md
python .idse/integrations/claude-skill/scripts/generate_artifact.py spec -o ./artifacts/spec.md

# Validate artifact completeness
python .idse/integrations/claude-skill/scripts/validate_artifacts.py ./artifacts/

# Check which stage is ready
python .idse/integrations/claude-skill/scripts/validate_artifacts.py ./artifacts/ --check-ready
```

### Example Session

```
you> I want to add real-time notifications. Let's use IDSE.

claude> I'll help you build this following the IDSE pipeline. Let me first check 
        if we have existing artifacts...
        
        No existing artifacts found in ./artifacts/
        
        **Starting at Intent stage.**
        
        Let me ask some questions to create intent.md:
        
        1. What's the primary goal of these notifications?
        2. Who are the target users?
        3. How will you measure success?
        ...

you> [answers questions]

claude> I'll create the intent artifact:
        
        *creates ./artifacts/intent.md*
        
        Intent captured. Ready for Context stage.
        
        Looking at your codebase, I can see:
        - Next.js frontend (app router)
        - Node/Express API
        - PostgreSQL database
        
        Let me generate context.md with what I observe...
```

---

## Option 2: Cursor with Rules

Cursor supports `.cursorrules` files for AI behavior customization.

### Setup

1. **Add IDSE to your project** (same as Claude Code step 1)

2. **Create `.cursorrules`:**

   ```bash
   cat > .cursorrules << 'EOF'
   You are an IDSE (Intent-Driven Systems Engineering) Developer Agent.
   
   ## Pipeline
   Intent → Context → Specification → Plan → Tasks → Implementation → Feedback
   
   ## Absolute Rules
   1. NEVER write implementation code without plan.md and tasks.md existing
   2. NEVER create a plan without spec.md existing
   3. NEVER create a spec without intent.md and context.md existing
   4. Mark ALL unclear requirements with [REQUIRES INPUT]
   
   ## When Asked to Implement Features
   First check for artifacts in ./artifacts/ or project root:
   1. intent.md exists? If not, create it first
   2. context.md exists? If not, create it first  
   3. spec.md exists? If not, create it first
   4. plan.md exists? If not, create it first
   5. tasks.md exists? If not, create it first
   6. ONLY THEN proceed with implementation
   
   ## Artifact Templates
   Use templates from .idse/kb/templates/ when creating artifacts.
   
   ## Constitution Reference
   Follow guardrails in .idse/docs/02-idse-constitution.md:
   - Intent Supremacy: All decisions trace to explicit intent
   - Context Alignment: Architecture reflects constraints
   - Specification Completeness: No unresolved ambiguities
   - Test-First Mandate: Tests before code
   - Plan Before Build: No code without plan
   
   ## When User Tries to Skip Stages
   Politely redirect:
   "I'd like to help with that, but IDSE requires we have [missing stage] first. 
   Let me help create that so we build on a solid foundation."
   
   ## File Locations
   - Methodology: .idse/
   - Templates: .idse/kb/templates/
   - Examples: .idse/kb/examples/
   - Artifacts: ./artifacts/ (create if needed)
   EOF
   ```

3. **Create artifacts directory:**

   ```bash
   mkdir -p artifacts
   echo "# IDSE Artifacts\nGenerated engineering artifacts for this project." > artifacts/README.md
   ```

4. **Open in Cursor:**

   ```bash
   cursor .
   ```

### Cursor Commands

In Cursor chat (Cmd+L / Ctrl+L):

```
Create intent.md for a new user dashboard feature
```

```
Based on our codebase, generate context.md
```

```
@artifacts/spec.md Review this spec for completeness
```

```
Generate tasks from @artifacts/plan.md
```

---

## Option 3: VS Code with Tasks

Use VS Code tasks for IDSE governance workflows.

### Setup

1. **Add IDSE to your project** (same as above)

2. **Copy VS Code configuration:**

   ```bash
   cp -r .idse/.vscode ./
   cp -r .idse/.cursor ./
   cp .idse/.idse-layer ./
   ```

3. **Create `artifacts/` directory:**

   ```bash
   mkdir -p artifacts
   ```

### Available Tasks

Open Command Palette (Cmd+Shift+P) → "Tasks: Run Task":

| Task                           | Description                   |
| ------------------------------ | ----------------------------- |
| View IDSE State                | Show current governance state |
| Validate IDSE Governance Layer | Check layer integrity         |
| Handoff to Codex               | Transfer control for review   |
| Handoff to Claude              | Transfer control for building |
| Change Role to Builder         | Set role to builder           |
| Change Role to Reviewer        | Set role to reviewer          |

### With GitHub Copilot

Add to `.github/copilot-instructions.md`:

```markdown
## IDSE Methodology

Follow Intent-Driven Systems Engineering for all feature work.

Pipeline: Intent → Context → Specification → Plan → Tasks → Implementation

Before writing implementation code:
1. Check for existing IDSE artifacts in ./artifacts/
2. If missing, help create them following templates in .idse/kb/templates/
3. Never skip stages

Mark unclear requirements with [REQUIRES INPUT].
```

---

## Option 4: Continue.dev (Open Source)

For VS Code users who prefer open-source AI.

### Setup

1. Install Continue extension in VS Code

2. Configure `.continue/config.json`:

   ```json
   {
     "models": [...],
     "systemMessage": "You are an IDSE Developer Agent. Follow the Intent-Driven Systems Engineering pipeline: Intent → Context → Spec → Plan → Tasks → Implementation. Never write code without a plan. Reference .idse/ for methodology and templates.",
     "docs": [
       {
         "name": "IDSE",
         "startUrl": ".idse/docs/",
         "faviconUrl": ""
       }
     ]
   }
   ```

---

## Governance Layer (Optional)

For teams using dual-agent workflows (Claude ↔ Codex):

### What It Does

- Tracks which AI is "active" (building vs reviewing)
- Manages handoffs between agents
- Enforces role boundaries
- Logs governance cycles

### Setup

```bash
# Copy governance infrastructure
cp -r .idse/idse-governance ./
cp -r .idse/.cursor ./
cp .idse/.idse-layer ./
```

### State File

`idse-governance/state/state.json` tracks:

```json
{
  "active_llm": "claude_code",
  "awaiting_handoff": false,
  "handoff_cycle_id": null,
  "active_stage": "Intent",
  "role_change_event": null
}
```

### Handoff Commands

```bash
# View current state
python .cursor/tasks/governance.py view

# Handoff to Codex for review
python .cursor/tasks/governance.py handoff claude_code codex_gpt "Implementation complete, ready for review"

# Handoff back to Claude
python .cursor/tasks/governance.py handoff codex_gpt claude_code "Review complete, feedback logged"

# Change role
python .cursor/tasks/governance.py role reviewer
```

---

## Recommended Project Structure

```
your-project/
├── .idse/                      # IDSE methodology (submodule or copy)
│   ├── docs/
│   ├── kb/
│   │   ├── templates/
│   │   ├── examples/
│   │   └── playbooks/
│   ├── prompts/
│   └── integrations/
│       └── claude-skill/
│           └── scripts/
├── .cursorrules                # Cursor AI rules (if using Cursor)
├── .vscode/                    # VS Code tasks
├── artifacts/                  # Generated IDSE artifacts
│   ├── intent.md
│   ├── context.md
│   ├── spec.md
│   ├── plan.md
│   ├── tasks.md
│   └── test-plan.md
├── idse-governance/            # Optional governance layer
├── src/                        # Your source code
├── tests/                      # Your tests
├── AGENTS.md                   # Agent instructions
└── .idse-layer                 # Governance boundary marker
```

---

## Workflow Example

### Starting a Feature

```bash
# 1. Generate intent template
python .idse/integrations/claude-skill/scripts/generate_artifact.py intent -o ./artifacts/intent.md

# 2. Fill in intent.md with Claude Code
claude "Help me fill in artifacts/intent.md for adding user authentication"

# 3. Generate context
python .idse/integrations/claude-skill/scripts/generate_artifact.py context -o ./artifacts/context.md
claude "Generate context.md based on our codebase"

# 4. Check readiness
python .idse/integrations/claude-skill/scripts/validate_artifacts.py ./artifacts/

# 5. Continue through stages...
```

### Validation Checks

```bash
# Full validation with report
python .idse/integrations/claude-skill/scripts/validate_artifacts.py ./artifacts/

# Output:
# ============================================================
# 📋 IDSE Artifact Validation: ./artifacts/
# ============================================================
# 
# 📊 Pipeline Status:
#    ✅ intent: complete
#    ✅ context: complete
#    🔶 spec: 3 unresolved
#    ⬜ plan: not started
#    ⬜ tasks: not started
# 
# 📈 Summary:
#    Total unresolved: 3
#    Ready for: spec
```

---

## Tips

### Do This ✅

- Keep `.idse/` as a submodule for easy updates
- Run validation before moving to next stage
- Commit artifacts with your code
- Use AGENTS.md to document project-specific conventions

### Avoid This ❌

- Don't modify `.idse/` directly (fork if customizing)
- Don't skip validation checks
- Don't commit artifacts with unresolved [REQUIRES INPUT]
- Don't ignore governance state in team settings