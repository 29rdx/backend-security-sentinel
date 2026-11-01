from sentinel.cve_matcher import check_cve_fingerprint

def test_heartbleed_match():
    cves = check_cve_fingerprint("Server: OpenSSL/1.0.1f")
    assert any("Heartbleed" in c for c in cves)

def test_clean_banner():
    cves = check_cve_fingerprint("Server: Cloudflare")
    assert len(cves) == 0
