"""Basic middleware - Open Source"""

from typing import Dict, Any
from prompt_guard_core.scanner import Scanner


class PromptGuardMiddleware:
    """Lightweight middleware for AI agents"""
    
    def __init__(self):
        self.scanner = Scanner()
    
    async def check_input(self, text: str) -> Dict[str, Any]:
        return self.scanner.scan_input(text)
    
    async def check_output(self, text: str) -> Dict[str, Any]:
        return self.scanner.scan_output(text)
