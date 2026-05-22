# Agentmail Python - Repository Map

## Directory Structure

```
agentmail-python/
├── README.md                    # Main documentation
├── reference.md                 # Full API reference (101KB)
├── pyproject.toml               # Poetry config, v0.5.0
├── poetry.lock
├── requirements.txt
├── .github/
│   └── workflows/
│       └── ci.yml               # compile → test → publish pipeline
├── src/agentmail/               # Main package
│   ├── __init__.py              # Exports AgentMail, AsyncAgentMail
│   ├── client.py               # Main client wrapper
│   ├── version.py              # Version info
│   ├── py.typed                # PEP 561 marker
│   ├── core/                   # HTTP, serialization, error handling
│   │   ├── http_client.py      # httpx-based HTTP layer (29KB)
│   │   ├── client_wrapper.py   # Client wrapper utilities
│   │   ├── api_error.py
│   │   ├── serialization.py
│   │   ├── query_encoder.py    # ⚠️ ruff: import sorting issue
│   │   └── ...
│   ├── inboxes/                # Inbox management
│   │   ├── client.py           # InboxClient (16KB)
│   │   ├── raw_client.py
│   │   ├── types/
│   │   ├── messages/
│   │   ├── threads/
│   │   ├── drafts/
│   │   └── ...
│   ├── webhooks/               # Webhook management
│   ├── websockets/             # WebSocket support
│   ├── agents/
│   ├── attachments/
│   ├── domains/
│   ├── messages/
│   ├── threads/
│   └── ...
└── tests/
    ├── utils/
    │   ├── test_query_encoding.py  # ⚠️ ruff: import sorting issue
    │   ├── test_serialization.py
    │   ├── test_http_client.py
    │   └── assets/models/
    └── custom/
        └── test_client.py
```

## API Surface (via `client.py`)

### Main Classes
- `AgentMail` - sync client
- `AsyncAgentMail` - async client

### Sub-clients (via `client.inboxes.*`, etc.)
- `inboxes` - Inbox CRUD operations
- `messages` - Message handling
- `threads` - Thread management
- `drafts` - Draft operations
- `attachments` - File attachments
- `webhooks` - Webhook management
- `websockets` - Real-time connections
- `agents` - Agent operations
- `domains` - Domain management
- `organizations` - Org management
- `api_keys` - API key management
- `lists` - Mailing lists
- `events` - Event handling
- `inbox_events` - Inbox event streams
- `metrics` - Analytics

## Quality Assurance

| Check | Status | Details |
|-------|--------|---------|
| Tests | ✅ Pass | 27 passed, 1 skipped |
| Mypy | ✅ Pass | 350 source files, no issues |
| Ruff | ⚠️ Fixable | 2 import sorting issues |

## Issues Analysis (6 Open)

| # | Title | Labels | Created |
|---|-------|--------|---------|
| 8 | Add nix package for reproducible builds | - | 2026-02-01 |
| 7 | feat: add nix support | - | 2026-02-01 |
| 6 | BUG: Missing contributor with SDK expertise | - | 2025-11-12 |
| 5 | feat: add MIT License | - | 2025-11-08 |
| 4 | fix: fix grammar and syntax issues | - | 2025-11-08 |
| 2 | README: Fix broken code block formatting | - | 2025-06-25 |

## Pull Requests (4 Open)

| # | Title | Created |
|---|-------|---------|
| 7 | feat: add nix support | 2026-02-01 |
| 5 | feat: add MIT License | 2025-11-08 |
| 4 | fix: fix grammar and syntax issues | 2025-11-08 |
| 2 | README: Fix broken code block formatting | 2025-06-25 |