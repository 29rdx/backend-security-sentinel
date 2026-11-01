from sentinel.xss_detector import scan_xss_vectors

def test_xss_detected():
    res = scan_xss_vectors("<img src=x onerror=alert(1)>")
    assert res["is_xss"] is True

def test_xss_clean():
    res = scan_xss_vectors("Hello world this is safe text")
    assert res["is_xss"] is False
