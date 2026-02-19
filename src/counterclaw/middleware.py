"""
CounterClaw - Defensive Interceptor Middleware
Snaps shut on malicious payloads before they reach your AI
"""

from typing import Dict, Any
from counterclaw.scanner import Scanner


class CounterClawInterceptor:
    """Defensive interceptor - snaps shut on threats"""
    
    def __init__(self):
        self.scanner = Scanner()
    
    async def check_input(self, text: str) -> Dict[str, Any]:
        return self.scanner.scan_input(text)
    
    async def check_output(self, text: str) -> Dict[str, Any]:
        return self.scanner.scan_output(text)
