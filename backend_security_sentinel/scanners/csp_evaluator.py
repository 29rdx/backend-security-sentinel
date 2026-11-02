class CSPEvaluator:
    """Audits Content-Security-Policy directives for anti-XSS posture."""
    @staticmethod
    def evaluate_policy(csp_string: str) -> dict:
        directives = [d.strip() for d in csp_string.split(";") if d.strip()]
        has_unsafe_inline = any("'unsafe-inline'" in d for d in directives)
        has_unsafe_eval = any("'unsafe-eval'" in d for d in directives)
        has_default_src = any(d.startswith("default-src") for d in directives)
        risk = "HIGH" if (has_unsafe_inline or has_unsafe_eval) else "MEDIUM" if not has_default_src else "SAFE"
        return {
            "has_unsafe_inline": has_unsafe_inline,
            "has_unsafe_eval": has_unsafe_eval,
            "has_default_src": has_default_src,
            "posture": risk
        }
