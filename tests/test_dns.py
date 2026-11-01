from sentinel.dns_validator import check_security_dns_records

def test_dns_records():
    res = check_security_dns_records("github.com")
    assert res["dnssec_active"] is True
    assert res["dmarc_status"] == "ENFORCED"
