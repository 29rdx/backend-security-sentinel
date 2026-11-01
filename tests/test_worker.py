from sentinel.worker import ScanWorker

def test_worker():
    w = ScanWorker(["https://t1.com", "https://t2.com"])
    assert w.process_next() == "https://t1.com"
    assert w.process_next() == "https://t2.com"
    assert w.process_next() is None
