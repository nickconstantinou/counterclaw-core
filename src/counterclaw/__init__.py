"""
CounterClaw - Defensive Security for AI Agents

A defensive interceptor that snaps shut on malicious payloads.
"""

__version__ = "1.0.0"

from counterclaw.scanner import Scanner
from counterclaw.middleware import CounterClawInterceptor, _log_violation

__all__ = ["Scanner", "CounterClawInterceptor", "_log_violation", "__version__"]
