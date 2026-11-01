from sentinel.rule_engine import load_owasp_rules, evaluate_finding

def test_load_rules():
    rules = load_owasp_rules()
    assert "API1:2023" in rules
    assert "API2:2023" in rules

def test_evaluate_finding():
    rules = load_owasp_rules()
    res = evaluate_finding("API2:2023", rules)
    assert res["severity"] == "CRITICAL"
