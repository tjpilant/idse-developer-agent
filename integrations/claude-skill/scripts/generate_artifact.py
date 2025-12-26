#!/usr/bin/env python3
"""
IDSE Artifact Generator

Generates structured markdown templates for each IDSE pipeline stage.

Usage:
    python generate_artifact.py <stage> --output <path>
    python generate_artifact.py intent --output ./project/intent.md
    python generate_artifact.py spec   # outputs to stdout
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime

TEMPLATES = {
    "intent": '''# Intent

> Generated: {timestamp}

## Goal

[REQUIRES INPUT] What are we building and why? (One sentence)

## Problem / Opportunity

[REQUIRES INPUT] What pain point or opportunity does this address?

## Success Criteria

- [ ] [REQUIRES INPUT] Measurable outcome 1
- [ ] [REQUIRES INPUT] Measurable outcome 2
- [ ] [REQUIRES INPUT] Measurable outcome 3

## Scope

### In Scope

- [REQUIRES INPUT] Feature/capability 1
- [REQUIRES INPUT] Feature/capability 2

### Out of Scope

- [REQUIRES INPUT] Explicitly excluded item 1
- [REQUIRES INPUT] Explicitly excluded item 2
''',

    "context": '''# Context

> Generated: {timestamp}
> Depends on: intent.md

## Environment

- **Product/Project:** [REQUIRES INPUT]
- **Domain:** [REQUIRES INPUT]
- **Users/Actors:** [REQUIRES INPUT]

## Stack

- **Frontend:** [REQUIRES INPUT] Frameworks, state management
- **Backend/API:** [REQUIRES INPUT] Languages, frameworks
- **Database:** [REQUIRES INPUT] Primary DB, caching
- **Infrastructure:** [REQUIRES INPUT] Cloud, orchestration
- **Integrations:** [REQUIRES INPUT] External APIs/services

## Constraints

- **Scale:** [REQUIRES INPUT] Expected users, data volume, throughput
- **Performance:** [REQUIRES INPUT] Latency targets, response times
- **Compliance:** [REQUIRES INPUT] GDPR, SOC2, HIPAA, etc.
- **Team:** [REQUIRES INPUT] Skills available, time capacity
- **Deadlines:** [REQUIRES INPUT] Key dates, release windows
- **Legacy:** [REQUIRES INPUT] Systems that cannot change

## Risks & Unknowns

- **Technical Risks:** [REQUIRES INPUT]
- **Operational Risks:** [REQUIRES INPUT]
- **Regulatory Risks:** [REQUIRES INPUT]
- **Unknowns:** [REQUIRES INPUT] Areas needing research
''',

    "spec": '''# Specification

> Generated: {timestamp}
> Depends on: intent.md, context.md

## Overview

[REQUIRES INPUT] 2-3 sentence summary of system behavior

## User Stories

- As a [REQUIRES INPUT role], I want [REQUIRES INPUT capability], so that [REQUIRES INPUT benefit]
- As a [REQUIRES INPUT role], I want [REQUIRES INPUT capability], so that [REQUIRES INPUT benefit]
- As a [REQUIRES INPUT role], I want [REQUIRES INPUT capability], so that [REQUIRES INPUT benefit]

## Functional Requirements

1. **FR-1:** [REQUIRES INPUT] System shall...
2. **FR-2:** [REQUIRES INPUT] System shall...
3. **FR-3:** [REQUIRES INPUT] System shall...

## Non-Functional Requirements

1. **NFR-1 (Performance):** [REQUIRES INPUT] Response time < Xms for Y% of requests
2. **NFR-2 (Security):** [REQUIRES INPUT] Authentication, authorization requirements
3. **NFR-3 (Scalability):** [REQUIRES INPUT] Support X concurrent users
4. **NFR-4 (Availability):** [REQUIRES INPUT] Uptime target

## Acceptance Criteria

- **AC-1:** Given [REQUIRES INPUT precondition], when [REQUIRES INPUT action], then [REQUIRES INPUT result]
- **AC-2:** Given [REQUIRES INPUT precondition], when [REQUIRES INPUT action], then [REQUIRES INPUT result]
- **AC-3:** Given [REQUIRES INPUT precondition], when [REQUIRES INPUT action], then [REQUIRES INPUT result]

## Open Questions

- [REQUIRES INPUT] List any unresolved questions here
''',

    "plan": '''# Implementation Plan

> Generated: {timestamp}
> Depends on: spec.md

## Architecture Summary

[REQUIRES INPUT] High-level overview of system architecture and component interactions

## Components

| Component | Responsibility | Dependencies |
|-----------|---------------|--------------|
| [REQUIRES INPUT] | [REQUIRES INPUT] | [REQUIRES INPUT] |
| [REQUIRES INPUT] | [REQUIRES INPUT] | [REQUIRES INPUT] |
| [REQUIRES INPUT] | [REQUIRES INPUT] | [REQUIRES INPUT] |

## Data Model

```sql
-- [REQUIRES INPUT] Schema definitions
CREATE TABLE example (
    id UUID PRIMARY KEY,
    -- Add columns
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- [REQUIRES INPUT] Indexes
CREATE INDEX idx_example ON example(column);
```

## API Contracts

### [REQUIRES INPUT] Endpoint Name

- **Method/Path:** [REQUIRES INPUT] GET /api/resource
- **Description:** [REQUIRES INPUT]
- **Request:**
  ```json
  {
    "field": "value"
  }
  ```
- **Response (200):**
  ```json
  {
    "data": []
  }
  ```
- **Errors:** 400 Bad Request, 401 Unauthorized, 404 Not Found, 500 Server Error

## Test Strategy

### Contract Tests
[REQUIRES INPUT] API schema validation approach

### Integration Tests
[REQUIRES INPUT] Component interaction testing

### E2E Tests
[REQUIRES INPUT] User workflow validation

### Performance Tests
[REQUIRES INPUT] Load testing approach and targets

## Phases

### Phase 0: Foundations
- [REQUIRES INPUT] Infrastructure, scaffolding, initial schemas

### Phase 1: Core Behavior
- [REQUIRES INPUT] Primary functionality implementation

### Phase 2: Hardening
- [REQUIRES INPUT] NFRs, scaling, security, resilience
''',

    "tasks": '''# Tasks

> Generated: {timestamp}
> Depends on: plan.md

`[P]` = parallelizable (can be done simultaneously with other [P] tasks in same phase)

## Phase 0: Foundations

- [ ] **Task 0.1:** [REQUIRES INPUT] Description
  - Deliverable: [REQUIRES INPUT]
  - Test: [REQUIRES INPUT]

- [ ] **Task 0.2:** [REQUIRES INPUT] Description
  - Deliverable: [REQUIRES INPUT]
  - Test: [REQUIRES INPUT]

## Phase 1: Core Behavior

- [ ] **Task 1.1:** [REQUIRES INPUT] Description
  - Deliverable: [REQUIRES INPUT]
  - Test: [REQUIRES INPUT]

- [P] [ ] **Task 1.2:** [REQUIRES INPUT] Description
  - Deliverable: [REQUIRES INPUT]
  - Test: [REQUIRES INPUT]

- [P] [ ] **Task 1.3:** [REQUIRES INPUT] Description
  - Deliverable: [REQUIRES INPUT]
  - Test: [REQUIRES INPUT]

- [ ] **Task 1.4:** [REQUIRES INPUT] Description (depends on 1.2, 1.3)
  - Deliverable: [REQUIRES INPUT]
  - Test: [REQUIRES INPUT]

## Phase 2: Hardening

- [ ] **Task 2.1:** [REQUIRES INPUT] Integration/E2E tests
  - Deliverable: [REQUIRES INPUT]
  - Test: [REQUIRES INPUT]

- [ ] **Task 2.2:** [REQUIRES INPUT] Performance testing and tuning
  - Deliverable: [REQUIRES INPUT]
  - Test: [REQUIRES INPUT]

- [ ] **Task 2.3:** [REQUIRES INPUT] Documentation and compliance review
  - Deliverable: [REQUIRES INPUT]
  - Test: [REQUIRES INPUT]
'''
}

def generate_artifact(stage: str, output_path: str = None) -> str:
    """Generate an IDSE artifact template."""
    if stage not in TEMPLATES:
        valid = ", ".join(TEMPLATES.keys())
        raise ValueError(f"Unknown stage: {stage}. Valid stages: {valid}")
    
    content = TEMPLATES[stage].format(
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M")
    )
    
    if output_path:
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        print(f"✅ Generated {stage}.md at {output_path}")
    else:
        print(content)
    
    return content

def main():
    parser = argparse.ArgumentParser(
        description="Generate IDSE artifact templates"
    )
    parser.add_argument(
        "stage",
        choices=["intent", "context", "spec", "plan", "tasks"],
        help="Pipeline stage to generate"
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file path (prints to stdout if not specified)"
    )
    
    args = parser.parse_args()
    
    try:
        generate_artifact(args.stage, args.output)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()