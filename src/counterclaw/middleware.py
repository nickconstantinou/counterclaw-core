"""
CounterClaw - Defensive Interceptor Middleware
Snaps shut on malicious payloads before they reach your AI
"""

import os
from typing import Dict, Any, Optional
from datetime import datetime
from counterclaw.scanner import Scanner


MEMORY_PATH = os.path.expanduser("~/.openclaw/memory/MEMORY.md")


def _ensure_memory_file() -> None:
    """Ensure MEMORY.md exists - create if missing"""
    memory_dir = os.path.dirname(MEMORY_PATH)
    if not os.path.exists(memory_dir):
        os.makedirs(memory_dir, exist_ok=True)
    if not os.path.exists(MEMORY_PATH):
        with open(MEMORY_PATH, "w") as f:
            f.write("# OpenClaw Memory\n\n")


def _log_violation(violation: Dict[str, Any], context: str) -> None:
    """Log violation to MEMORY.md - fails silently if inaccessible"""
    try:
        _ensure_memory_file()
        with open(MEMORY_PATH, "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            f.write(f"\n## {timestamp} - CounterClaw Violation\n")
            f.write(f"**Context:** {context}\n")
            f.write(f"**Violations:** {violation.get('violations', [])}\n")
    except (IOError, OSError):
        # Silent fail - don't crash the scanner
        pass


class CounterClawInterceptor:
    """Defensive interceptor - snaps shut on threats"""
    
    def __init__(self, enable_nexus: bool = False, nexus_api_key: Optional[str] = None):
        self.scanner = Scanner()
        self.enable_nexus = enable_nexus
        self.nexus_api_key = nexus_api_key
        
        if enable_nexus and not nexus_api_key:
            raise ValueError("Nexus API key required when enable_nexus=True")
    
    async def check_input(self, text: str, log_violations: bool = True) -> Dict[str, Any]:
        result = self.scanner.scan_input(text)
        
        if result["blocked"] and log_violations:
            _log_violation(result, "input")
        
        # Nexus hook - dormant unless enabled
        if self.enable_nexus:
            result["nexus_checked"] = True
            # TODO: Send to api.counterclaw.io if configured
        
        return result
    
    async def check_output(self, text: str, log_violations: bool = True) -> Dict[str, Any]:
        result = self.scanner.scan_output(text)
        
        if result.get("pii_detected") and log_violations:
            _log_violation(result, "output")
        
        # Nexus hook - dormant unless enabled
        if self.enable_nexus:
            result["nexus_checked"] = True
            # TODO: Send to api.counterclaw.io if configured
        
        return result
