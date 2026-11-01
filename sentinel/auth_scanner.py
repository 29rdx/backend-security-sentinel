def prepare_auth_headers(bearer_token: str = None, api_key: str = None) -> dict:
    headers = {"User-Agent": "BackendSecuritySentinel/1.2"}
    if bearer_token:
        headers["Authorization"] = f"Bearer {bearer_token}"
    if api_key:
        headers["X-API-Key"] = api_key
    return headers
