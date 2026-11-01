from sentinel.benchmark import run_scanner_benchmark

def test_benchmark():
    res = run_scanner_benchmark(50)
    assert res["ops_per_second"] > 0
    assert res["elapsed_seconds"] < 5.0
