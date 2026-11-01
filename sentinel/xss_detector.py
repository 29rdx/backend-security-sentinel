import html
import re

XSS_PATTERNS = [
    re.compile(r"<script[^>]*>.*?</script>", re.IGNORECASE | re.DOTALL),
    re.compile(r"javascript:[^\s"'>]+", re.IGNORECASE),
    re.compile(r"onerror\s*=\s*['"].*?['"]", re.IGNORECASE),
    re.compile(r"onload\s*=\s*['"].*?['"]", re.IGNORECASE),
    re.compile(r"eval\s*\([^\)]*\)", re.IGNORECASE),
]

def scan_xss_vectors(input_str: str) -> dict:
    threats = []
    for pattern in XSS_PATTERNS:
        match = pattern.search(input_str)
        if match:
            threats.append(match.group(0))
    return {
        "is_xss": len(threats) > 0,
        "vector_count": len(threats),
        "vectors": threats
    }
