import unittest
from backend_security_sentinel.scanners.csp_evaluator import CSPEvaluator

class TestCSPEvaluator(unittest.TestCase):
    def test_unsafe_inline_flagged(self):
        res = CSPEvaluator.evaluate_policy("default-src 'self'; script-src 'unsafe-inline'")
        self.assertTrue(res["has_unsafe_inline"])
        self.assertEqual(res["posture"], "HIGH")
