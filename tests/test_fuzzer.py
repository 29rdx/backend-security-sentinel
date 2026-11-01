from sentinel.fuzzer import generate_fuzz_urls

def test_generate_fuzz():
    urls = generate_fuzz_urls("https://example.com/api", {"id": "1", "q": "test"})
    assert len(urls) > 10
    assert any("alert(1)" in u or "svg" in u for u in urls)
