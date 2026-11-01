def check_cve_fingerprint(server_header: str) -> list:
    known_vulnerabilities = {
        "Apache/2.4.49": ["CVE-2021-41773", "CVE-2021-42013"],
        "nginx/1.20.0": ["CVE-2021-23017"],
        "OpenSSL/1.0.1": ["CVE-2014-0160 (Heartbleed)"]
    }
    for signature, cves in known_vulnerabilities.items():
        if signature.lower() in server_header.lower():
            return cves
    return []
