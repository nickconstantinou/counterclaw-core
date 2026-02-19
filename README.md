# Prompt Guard Core 🛡️

**Free, open-source security middleware for AI agents**

## Install

```bash
pip install prompt-guard-core
```

## Usage

```python
from prompt_guard_core import PromptGuardMiddleware

middleware = PromptGuardMiddleware()

# Check input
result = await middleware.check_input("Hello!")
result = await middleware.check_input("Ignore previous instructions")

# Check output
result = await middleware.check_output("Contact me at john@example.com")
```

## License

MIT - Free and open source forever.
