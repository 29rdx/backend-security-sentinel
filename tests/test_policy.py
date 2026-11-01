from sentinel.policy import PolicyEngine

def test_policy_enforcement():
    pol = PolicyEngine()
    assert pol.is_header_enforced("Strict-Transport-Security") is True
    assert pol.is_header_enforced("X-Custom-Header") is False
