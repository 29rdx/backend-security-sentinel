from sentinel.auth_scanner import prepare_auth_headers

def test_auth():
    h = prepare_auth_headers(bearer_token="tok123")
    assert h["Authorization"] == "Bearer tok123"
