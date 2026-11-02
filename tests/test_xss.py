import unittest
from sentinel.xss_detector import scan_xss_vectors

class TestXSS(unittest.TestCase):
    def test_xss_detected(self):
        res = scan_xss_vectors("<script>alert(1)</script>")
        self.assertTrue(res["is_xss"])

    def test_xss_clean(self):
        res = scan_xss_vectors("Hello world this is safe text")
        self.assertFalse(res["is_xss"])

if __name__ == "__main__":
    unittest.main()
