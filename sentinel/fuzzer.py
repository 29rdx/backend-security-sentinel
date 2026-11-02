from typing import Generator

def generate_fuzz_urls(base_url: str, payloads: list[str]) -> Generator[str, None, None]:
    for p in payloads:
        yield f"{base_url.rstrip('/')}/{p}"
