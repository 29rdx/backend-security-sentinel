def parse_retry_after(header_val: str) -> int:
    try:
        return int(header_val)
    except (ValueError, TypeError):
        return 60
