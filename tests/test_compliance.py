from sentinel.compliance import ComplianceChecker

def test_compliance():
    cc = ComplianceChecker()
    res = cc.evaluate_compliance([])
    assert res["compliant"] is True
