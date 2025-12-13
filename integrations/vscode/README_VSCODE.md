# 🧠 IDSE Dual-Agent VS Code Integration

This workspace uses the Anthropic Claude and OpenAI VS Code extensions
as governed agents under the **Intent-Driven Systems Engineering (IDSE)** framework.

## Agents
- **Claude (Anthropic Extension)** — Intent, Context, Spec, Plan
- **Codex (OpenAI Extension)** — Tasks, Implementation, Feedback  
  Reads `AGENTS.md` for active roles and behaviors.

## Governance Layer
- `idse-governance/` — metadata, state, and automation
- `.cursor/config/idse-governance.json` — path boundaries
- `.vscode/tasks.json` — handoff & role commands
- `.idse-layer` — boundary marker

## Typical Cycle
1. Claude builds → creates `Plan.md` and `Tasks.md`
2. Run **Task: Handoff to Codex**
3. Codex implements & tests → produces code + feedback
4. Run **Task: Handoff to Claude**
5. Claude refines plan; next iteration begins

All activity is logged in `idse-governance/state/state.json` and feedback docs.

## Diagram

```mermaid
flowchart TD
    subgraph IDE["VS Code Workspace (Governed)"]
        S[state.json – active_llm, stage]
        A[AGENTS.md – Codex roles]
        G[idse-governance.json – path boundaries]
    end

    Claude[Claude – Intent/Spec/Plan]
    Codex[Codex – Implementation/Feedback (reads AGENTS.md)]

    Claude -->|Handoff: Plan & Tasks| Codex
    Codex -->|Feedback.md| Claude
    S --> Claude
    S --> Codex
    A --> Codex
    G --> Codex

---

### **README.md (Patch)**

Add this near the bottom of your main README:

```markdown
---

## 🧭 Governance Lifecycle & Dual-Agent Integration

This repository implements a **self-governing dual-agent environment**
for Anthropic **Claude** and OpenAI **Codex** inside VS Code.

### Lifecycle
1️⃣ **Intent → Context → Specification → Plan → Tasks → Implementation → Feedback**

Each IDE agent transition mirrors these seven IDSE stages.

### Alternation
**Claude builds → Codex reviews → Feedback → Claude refines**  
Each loop is timestamped via `handoff_cycle_id`.

### Enforcement
- Governance rules: `.cursor/config/idse-governance.json`
- State control: `idse-governance/state/state.json`
- Agent behaviors: `AGENTS.md`
- Automation: `.cursor/tasks/governance.py` and `.vscode/tasks.json`

### Diagram
```mermaid
flowchart TD
    subgraph IDSE_Governance["IDSE Governance Layer"]
        S[state.json]
        A[AGENTS.md]
        C[idse-governance.json]
    end

    Claude[Claude – Intent / Spec / Plan]
    Codex[Codex (OpenAI VS Code Extension) – Implementation / Feedback]

    Claude -->|Handoff| Codex
    Codex -->|Feedback| Claude
    S --> Claude
    S --> Codex
    A --> Codex
    C --> Codex

---

## 🧩 **4 | Local Setup Checklist**

1. Paste all files into their respective paths.  
2. Commit and push:
   ```bash
   git checkout -b governance-integration
   git add .
   git commit -m "Add IDSE Governance Layer and Dual-Agent Integration"
   git push origin governance-integration
