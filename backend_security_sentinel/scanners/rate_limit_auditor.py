class RateLimitAuditor:
    """Audits HTTP response headers for rate limit governance."""
    STANDARD_HEADERS = [
        "x-ratelimit-limit", "x-ratelimit-remaining", "x-ratelimit-reset", "retry-after"
    ]

    @classmethod
    def evaluate_headers(cls, headers: dict) -> dict:
        lower_headers = {k.lower(): v for k, v in headers.items()}
        found = [h for h in cls.STANDARD_HEADERS if h in lower_headers]
        has_rate_limits = len(found) > 0
        return {
            "has_rate_limiting_headers": has_rate_limits,
            "detected_headers": found,
            "status": "COMPLIANT" if has_rate_limits else "DEFICIENT",
            "recommendation": "Implement standard RFC 6585 429 and Retry-After headers."
        }
