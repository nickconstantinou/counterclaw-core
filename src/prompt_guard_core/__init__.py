"""
Prompt Guard Core - Free Open Source Security Middleware

A lightweight, open-source security layer for AI agents.
"""

__version__ = "1.0.0"

from prompt_guard_core.scanner import Scanner
from prompt_guard_core.middleware import PromptGuardMiddleware

__all__ = ["Scanner", "PromptGuardMiddleware", "__version__"]
