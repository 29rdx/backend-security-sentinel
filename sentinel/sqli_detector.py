import re

SQLI_PATTERNS = [
    re.compile(r"(\%27)|(')|(\-\-)|(\%23)|(#)", re.IGNORECASE),
    re.compile(r"((SELECT|UNION|INSERT|UPDATE|DELETE|DROP|ALTER|EXEC))", re.IGNORECASE),
    re.compile(r"(OR\s+\d+=\d+)", re.IGNORECASE),
    re.compile(r"(AND\s+\d+=\d+)", re.IGNORECASE),
    re.compile(r"(SLEEP\s*\(\s*\d+\s*\))", re.IGNORECASE),
]

def analyze_sqli_payload(payload: str) -> dict:
    matched = []
    for pattern in SQLI_PATTERNS:
        if pattern.search(payload):
            matched.append(pattern.pattern)
    return {
        "vulnerable": len(matched) > 0,
        "matched_rules": len(matched),
        "patterns": matched
    }
