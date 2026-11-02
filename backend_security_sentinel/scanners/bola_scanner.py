import re

class BOLAScanner:
    """Audits API endpoints for Broken Object Level Authorization vulnerabilities."""
    NUMERIC_ID_PATTERN = re.compile(r'/\d+(?:/|$)')
    UUID_PATTERN = re.compile(r'/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}(?:/|$)', re.IGNORECASE)

    @classmethod
    def analyze_endpoint(cls, endpoint: str) -> dict:
        has_numeric = bool(cls.NUMERIC_ID_PATTERN.search(endpoint))
        has_uuid = bool(cls.UUID_PATTERN.search(endpoint))
        risk = "HIGH" if has_numeric else "MEDIUM" if has_uuid else "LOW"
        return {
            "endpoint": endpoint,
            "has_object_reference": has_numeric or has_uuid,
            "reference_type": "sequential_integer" if has_numeric else "uuid" if has_uuid else "none",
            "risk_level": risk,
            "remediation": "Enforce context-aware ABAC/RBAC authorization at data layer rather than relying on unguessable IDs."
        }
