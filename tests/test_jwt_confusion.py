import unittest
import base64
import json
from backend_security_sentinel.scanners.jwt_confusion_auditor import JWTConfusionAuditor

class TestJWTConfusion(unittest.TestCase):
    def test_none_algorithm_detected(self):
        header = base64.urlsafe_b64encode(json.dumps({"alg": "none"}).encode()).decode().rstrip("=")
        payload = base64.urlsafe_b64encode(json.dumps({"sub": "admin"}).encode()).decode().rstrip("=")
        token = f"{header}.{payload}."
        res = JWTConfusionAuditor.inspect_token_header(token)
        self.assertTrue(res["has_none_algorithm"])
        self.assertEqual(res["risk_level"], "CRITICAL")
