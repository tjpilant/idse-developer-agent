# GitHub Auth Setup (PAT or App)

## PAT (MVP/testing)
- Create a classic PAT with `repo` scope.
- Set `GITHUB_AUTH_MODE=pat` and `GITHUB_PAT=<token>`.

## GitHub App (production)
- Create an App with:
  - Repository permissions: Contents (Read/Write)
  - Webhooks: optional
- Install the App on target org/repo.
- Set:
  - `GITHUB_AUTH_MODE=app`
  - `GITHUB_APP_ID=<app id>`
  - `GITHUB_APP_PRIVATE_KEY=<pem contents>`
  - `GITHUB_APP_INSTALLATION_ID=<installation id>`

## Verify
- `GET /api/auth/status` should show the configured mode and flags.
