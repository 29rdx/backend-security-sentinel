import json
import base64

class JWTConfusionAuditor:
    """Audits JWT tokens for signature algorithm confusion and header flaws."""
    @staticmethod
    def inspect_token_header(raw_token: str) -> dict:
        parts = raw_token.split(".")
        if len(parts) < 2:
            return {"valid_jwt": False, "reason": "malformed format"}
        try:
            padded = parts[0] + "=" * ((4 - len(parts[0]) % 4) % 4)
            header = json.loads(base64.urlsafe_b64decode(padded).decode())
        except Exception:
            return {"valid_jwt": False, "reason": "header decode failed"}

        alg = header.get("alg", "").upper()
        is_none = alg in ("NONE", "NO")
        is_weak_hmac = alg in ("HS256", "HS384", "HS512") and "RS" in header.get("typ", "")
        
        return {
            "valid_jwt": True,
            "header": header,
            "alg": alg,
            "has_none_algorithm": is_none,
            "risk_level": "CRITICAL" if is_none else "HIGH" if is_weak_hmac else "SAFE"
        }
