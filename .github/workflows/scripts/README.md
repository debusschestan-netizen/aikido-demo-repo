# Aikido Demo Repo

This repository contains intentionally insecure/demo files for showcasing Aikido scans.
All values are FAKE. Do NOT use any secret from here in production.

Files to review:
- app.py — hardcoded secret, debug mode, insecure CORS, command injection, unsafe deserialization
- .env — fake secrets
- requirements.txt — old/vulnerable dependency versions
- Dockerfile — demo ENV variable
- .github/workflows/ci.yml — prints env secret in CI (bad)
- scripts/request_demo.py — verify=False (disables TLS)
- config.yaml — plaintext password
