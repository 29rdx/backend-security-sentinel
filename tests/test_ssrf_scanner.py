import unittest
from backend_security_sentinel.scanners.ssrf_scanner import SSRFScanner

class TestSSRFScanner(unittest.TestCase):
    def test_cloud_metadata_blocked(self):
        res = SSRFScanner.is_ssrf_vulnerable("http://169.254.169.254/latest/meta-data/")
        self.assertTrue(res["vulnerable"])
        self.assertEqual(res["severity"], "CRITICAL")

    def test_localhost_blocked(self):
        res = SSRFScanner.is_ssrf_vulnerable("http://localhost:8080/admin")
        self.assertTrue(res["vulnerable"])

    def test_public_allowed(self):
        res = SSRFScanner.is_ssrf_vulnerable("https://api.github.com/repos")
        self.assertFalse(res["vulnerable"])
