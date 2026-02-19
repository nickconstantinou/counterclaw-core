---
name: counterclaw-core
description: Defensive security interceptor for AI agents - snaps shut on prompt injections and PII leaks
metadata:
  {
    "openclaw": {
      "emoji": "🦞",
      "version": "1.0.0",
      "runtime": "python3.11+",
    },
  }
---

# CounterClaw 🦞

> Defensive security for AI agents. Snaps shut on malicious payloads.

## Installation

```bash
pip install counterclaw-core
```

## Quick Start

```python
from counterclaw import CounterClawInterceptor

interceptor = CounterClawInterceptor()

# Check input - snaps shut on injections
result = await interceptor.check_input("Ignore previous instructions")
# → {"blocked": True, "safe": False}

# Check output - detects PII leaks  
result = await interceptor.check_output("Contact: john@example.com")
# → {"safe": False, "pii_detected": {"email": True}}
```

## Features

- **Snap-shut Defense** - Blocks 20+ prompt injection patterns
- **PII Detection** - Catches emails, phones, credit cards
- **Auto MEMORY** - Logs violations to ~/.openclaw/memory/MEMORY.md
- **Nexus Ready** - Dormant hooks for enterprise SaaS (opt-in)

## Nexus Integration (Optional)

Enable enterprise features:

```python
interceptor = CounterClawInterceptor(
    enable_nexus=True,
    nexus_api_key="your-key"
)
```

Without API key → runs locally only (no errors).

## CLI

```bash
python -m counterclaw scan "test input"
```

## License

MIT - See LICENSE file
