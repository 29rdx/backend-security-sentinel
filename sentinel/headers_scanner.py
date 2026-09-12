import urllib.request
import ssl

RECOMMENDED_HEADERS = {
    "Strict-Transport-Security": "Enforces HTTPS connections and prevents MITM attacks.",
    "Content-Security-Policy": "Mitigates Cross-Site Scripting (XSS) and data injection.",
    "X-Content-Type-Options": "Prevents MIME-sniffing vulnerabilities (must be 'nosniff').",
    "X-Frame-Options": "Protects against clickjacking attacks (must be 'DENY' or 'SAMEORIGIN').",
    "Referrer-Policy": "Controls information passed in the Referer header.",
    "Permissions-Policy": "Controls access to browser features and APIs."
}

def scan_headers(url: str):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": "BackendSecuritySentinel/1.0"})
    
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
            headers = {k: v for k, v in response.headers.items()}
            status_code = response.status
    except Exception as e:
        return {"error": str(e), "url": url}

    findings = []
    missing_count = 0
    present_count = 0

    for h, desc in RECOMMENDED_HEADERS.items():
        found = False
        val = None
        for k in headers:
            if k.lower() == h.lower():
                found = True
                val = headers[k]
                break
        if found:
            present_count += 1
            findings.append({"header": h, "status": "PRESENT", "value": val, "severity": "SECURE", "description": desc})
        else:
            missing_count += 1
            findings.append({"header": h, "status": "MISSING", "value": None, "severity": "MEDIUM", "description": desc})

    score = int((present_count / len(RECOMMENDED_HEADERS)) * 100)
    return {
        "url": url,
        "status_code": status_code,
        "security_score": score,
        "present_headers": present_count,
        "missing_headers": missing_count,
        "findings": findings
    }
# CSP parsing enhanced
