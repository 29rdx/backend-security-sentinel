import unittest
from backend_security_sentinel.scanners.rate_limit_auditor import RateLimitAuditor

class TestRateLimitAuditor(unittest.TestCase):
    def test_compliant_headers(self):
        headers = {"X-RateLimit-Limit": "100", "X-RateLimit-Remaining": "99"}
        res = RateLimitAuditor.evaluate_headers(headers)
        self.assertTrue(res["has_rate_limiting_headers"])
        self.assertEqual(res["status"], "COMPLIANT")
