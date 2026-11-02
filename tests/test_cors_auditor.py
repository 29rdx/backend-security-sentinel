import unittest
from backend_security_sentinel.scanners.cors_auditor import CORSAuditor

class TestCORSAuditor(unittest.TestCase):
    def test_wildcard_with_credentials(self):
        res = CORSAuditor.evaluate_cors_policy("*", True)
        self.assertTrue(res["dangerous_credentials_wildcard"])
        self.assertEqual(res["severity"], "CRITICAL")
