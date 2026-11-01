import json
import base64
import time

def analyze_jwt(token: str):
    parts = token.strip().split(".")
    if len(parts) != 3:
        return {"error": "Invalid JWT format. Must contain 3 dot-separated base64 segments."}

    def decode_segment(s):
        s += "=" * ((4 - len(s) % 4) % 4)
        return json.loads(base64.urlsafe_b64decode(s.encode("utf-8")).decode("utf-8"))

    try:
        header = decode_segment(parts[0])
        payload = decode_segment(parts[1])
    except Exception as e:
        return {"error": f"Failed to decode base64 JSON payload: {e}"}

    vulnerabilities = []
    
    # 1. Alg None Vulnerability
    alg = header.get("alg", "").upper()
    if alg in ["NONE", ""]:
        vulnerabilities.append({
            "vuln": "Critical Algorithm Flaw (alg: none)",
            "severity": "CRITICAL",
            "impact": "Allows attackers to bypass signature verification entirely."
        })
    elif alg.startswith("HS") and "RS" in header.get("typ", ""):
        vulnerabilities.append({
            "vuln": "Potential Key Confusion (HMAC vs RSA)",
            "severity": "HIGH",
            "impact": "Public key may be abused as HMAC secret."
        })

    # 2. Expiration Check
    exp = payload.get("exp")
    if exp is None:
        vulnerabilities.append({
            "vuln": "Missing Expiration Claim (exp)",
            "severity": "MEDIUM",
            "impact": "Tokens never expire, increasing replay attack window."
        })
    else:
        if exp < time.time():
            vulnerabilities.append({
                "vuln": "Expired Token",
                "severity": "INFO",
                "impact": f"Token expired at unix timestamp {exp}."
            })

    return {
        "header": header,
        "payload": payload,
        "algorithm": alg,
        "vulnerability_count": len(vulnerabilities),
        "vulnerabilities": vulnerabilities
    }
