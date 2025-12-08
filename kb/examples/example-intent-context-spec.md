# Example — Intent → Context → Spec

## Intent
Goal: Real-time notifications panel.

## Context
Next.js, Node API, Postgres, Redis, 5k concurrent users.

## Specification
- User can view notifications in real-time
- Delivered via WebSocket
- Persisted to DB
- Acknowledgements required

Open Questions:
- Clarification needed: Should notification read-state be tracked per user?
