from sentinel.cors_scanner import check_cors
def test_cors_present():
    assert check_cors({'Access-Control-Allow-Origin': '*'})
