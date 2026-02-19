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
claw install counterclaw-core
```

## Usage

```python
from counterclaw import CounterClawInterceptor

interceptor = CounterClawInterceptor()

# Check input - snaps shut on injections
result = await interceptor.check_input("Ignore previous instructions")
# → blocked: True

# Check output - detects PII leaks
result = await interceptor.check_output("Contact: john@example.com")
# → pii_detected: {"email": True}
```

## Features

- **Snap-shut Defense** - Blocks prompt injections
- **PII Detection** - Catches emails, phones, cards
- **Zero Dependencies** - Lightweight
- **Open Source** - MIT License

## CLI

```bash
python -m counterclaw scan "test input"
```

## License

MIT - Free and open source.
