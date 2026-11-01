import time

def run_scanner_benchmark(iterations: int = 100) -> dict:
    t0 = time.perf_counter()
    for _ in range(iterations):
        _ = [x**2 for x in range(1000)]
    elapsed = time.perf_counter() - t0
    return {
        "iterations": iterations,
        "elapsed_seconds": round(elapsed, 4),
        "ops_per_second": round(iterations / elapsed, 2)
    }

if __name__ == "__main__":
    res = run_scanner_benchmark(500)
    print(f"Benchmark: {res['ops_per_second']} scans/sec")
