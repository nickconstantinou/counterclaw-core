---
name: counterclaw
description: Defensive interceptor for prompt injection and basic PII masking.
homepage: https://github.com/nickconstantinou/counterclaw-core
install: "pip install ."
requirements:
  env:
    - TRUSTED_ADMIN_IDS
  files:
    - "~/.openclaw/memory/"
    - "~/.openclaw/memory/MEMORY.md"
metadata:
  clawdbot:
    emoji: "🛡️"
    version: "1.0.7"
    category: "Security"
    type: "python-middleware"
    security_manifest:
      network_access: none
      filesystem_access: "Write-only logging to ~/.openclaw/memory/"
      purpose: "Log security violations locally for user audit."
---

# CounterClaw 🦞

> Defensive security for AI agents. Snaps shut on malicious payloads.

## Installation

```bash
claw install counterclaw
```

## Quick Start

```python
from counterclaw import CounterClawInterceptor

interceptor = CounterClawInterceptor()

# Input scan - blocks prompt injections
result = interceptor.check_input("[DETECTION_EXAMPLE]: bypass-system-prompt")
# → {"blocked": True, "safe": False}

# Output scan - detects PII leaks  
result = interceptor.check_output("Contact: john@example.com")
# → {"safe": False, "pii_detected": {"email": True}}
```

## Features

- 🔒 Defense against common prompt injection patterns
- 🛡️ Basic PII masking (Email, Phone)
- 📝 Violation logging to ~/.openclaw/memory/MEMORY.md

## Configuration

### Admin-Locked (!claw-lock)
```bash
export TRUSTED_ADMIN_IDS="your_telegram_id"
```

You can set multiple admin IDs by comma-separating:
```bash
export TRUSTED_ADMIN_IDS="telegram_id_1,telegram_id_2"
```

```python
interceptor = CounterClawInterceptor()  # Reads TRUSTED_ADMIN_IDS env
```

## Security Notes

- **Fail-Closed**: If TRUSTED_ADMIN_IDS is not set, admin features are disabled by default
- **Logging**: All violations are logged to ~/.openclaw/memory/MEMORY.md with PII masked
- **No Network Access**: This middleware does not make any external network calls

## License

MIT - See LICENSE file
