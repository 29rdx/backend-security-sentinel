from sentinel.retry import parse_retry_after

def test_retry_after():
    assert parse_retry_after("30") == 30
    assert parse_retry_after(None) == 60
