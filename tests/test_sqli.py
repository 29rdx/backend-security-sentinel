from sentinel.sqli_detector import analyze_sqli_payload

def test_sqli_detection_true():
    res = analyze_sqli_payload("admin' OR 1=1--")
    assert res["vulnerable"] is True
    assert res["matched_rules"] >= 1

def test_sqli_detection_clean():
    res = analyze_sqli_payload("normal_user_profile_123")
    assert res["vulnerable"] is False
