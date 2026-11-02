import unittest
import asyncio
from sentinel.engine import AsyncAuditEngine

class TestAsyncEngine(unittest.TestCase):
    def test_async_engine(self):
        engine = AsyncAuditEngine(concurrency=5)
        urls = ["https://site1.com", "https://site2.com", "https://site3.com"]
        results = asyncio.run(engine.batch_audit(urls))
        self.assertEqual(len(results), 3)
        self.assertTrue(all(r["secure"] for r in results))

if __name__ == "__main__":
    unittest.main()
