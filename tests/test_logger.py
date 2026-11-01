from sentinel.logger import log_event
import json

def test_logger():
    out = log_event("info", "Scan started", target="api.test")
    data = json.loads(out)
    assert data["level"] == "INFO"
    assert data["target"] == "api.test"
