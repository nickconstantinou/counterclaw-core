---
name: prompt-guard-core
description: Free open-source security middleware for AI agents - blocks prompt injections and basic PII detection
metadata:
  {
    "openclaw": {
      "emoji": "🛡️",
      "version": "1.0.0",
      "runtime": "python3.11+",
      "permissions": [],
    },
  }
---

# Prompt Guard Core

Free, open-source security middleware for AI agents.

## Installation

```bash
claw install prompt-guard-core
```

## Usage

```python
from prompt_guard_core import PromptGuardMiddleware

middleware = PromptGuardMiddleware()

# Check input
result = await middleware.check_input("Hello!")

# Check output  
result = await middleware.check_output("Contact: john@example.com")
```

## Features

- **Prompt Injection Detection** - Regex-based blocking
- **Basic PII Detection** - Email, phone, credit card
- **Lightweight** - No external dependencies
- **Open Source** - MIT License

## API

### check_input(text: str) -> dict
Returns: `{"safe": bool, "blocked": bool, "violations": list}`

### check_output(text: str) -> dict
Returns: `{"safe": bool, "pii_detected": dict}`

## License

MIT - Free and open source forever.
