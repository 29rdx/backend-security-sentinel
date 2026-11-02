class CORSAuditor:
    """Evaluates Cross-Origin Resource Sharing (CORS) policy safety."""
    @staticmethod
    def evaluate_cors_policy(allow_origin: str, allow_credentials: bool) -> dict:
        is_wildcard = allow_origin.strip() == "*"
        is_null = allow_origin.strip() == "null"
        dangerous_combo = is_wildcard and allow_credentials
        return {
            "allow_origin": allow_origin,
            "allow_credentials": allow_credentials,
            "dangerous_credentials_wildcard": dangerous_combo,
            "null_origin_allowed": is_null,
            "severity": "CRITICAL" if dangerous_combo else "HIGH" if is_null else "CLEAN"
        }
