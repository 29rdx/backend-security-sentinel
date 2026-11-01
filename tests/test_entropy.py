from sentinel.entropy import calculate_shannon_entropy, is_high_entropy_secret

def test_entropy_high():
    token = "ak_live_9f83a04b12c8479e0a2b4c8d1e3f"
    assert is_high_entropy_secret(token) is True

def test_entropy_low():
    token = "aaaaaaaaaaaaaaaa"
    assert is_high_entropy_secret(token) is False
