from sentinel.html_report import build_executive_html

def test_html_generation():
    html_out = build_executive_html({
        "target": "https://api.staging.internal",
        "score": 92,
        "findings": [{"severity": "HIGH", "name": "Missing CSP", "desc": "No Content-Security-Policy"}]
    })
    assert "<title>Security Audit Report" in html_out
    assert "https://api.staging.internal" in html_out
    assert "badge high" in html_out
