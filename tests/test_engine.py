import pytest
import asyncio
from sentinel.engine import AsyncAuditEngine

def test_async_engine():
    engine = AsyncAuditEngine(concurrency=5)
    urls = ["https://site1.com", "https://site2.com", "https://site3.com"]
    results = asyncio.run(engine.batch_audit(urls))
    assert len(results) == 3
    assert all(r["secure"] for r in results)
