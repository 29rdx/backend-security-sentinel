import json
import time

def log_event(level: str, message: str, **kwargs) -> str:
    payload = {
        "timestamp": int(time.time()),
        "level": level.upper(),
        "message": message,
        **kwargs
    }
    return json.dumps(payload)
