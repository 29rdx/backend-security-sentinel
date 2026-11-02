import unittest
from backend_security_sentinel.scanners.bola_scanner import BOLAScanner

class TestBOLAScanner(unittest.TestCase):
    def test_numeric_id_high_risk(self):
        res = BOLAScanner.analyze_endpoint("/api/v1/users/42/settings")
        self.assertEqual(res["risk_level"], "HIGH")
        self.assertEqual(res["reference_type"], "sequential_integer")

    def test_uuid_medium_risk(self):
        res = BOLAScanner.analyze_endpoint("/api/v1/orders/123e4567-e89b-12d3-a456-426614174000")
        self.assertEqual(res["risk_level"], "MEDIUM")

    def test_clean_endpoint(self):
        res = BOLAScanner.analyze_endpoint("/api/v1/auth/login")
        self.assertEqual(res["risk_level"], "LOW")
