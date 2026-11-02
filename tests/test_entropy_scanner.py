import unittest
from backend_security_sentinel.scanners.entropy_scanner import EntropyScanner

class TestEntropyScanner(unittest.TestCase):
    def test_high_entropy_token(self):
        token = "synthetic_entropy_token_9xK8mP2vL4qW7zR1tY6uI0oP"
        self.assertTrue(EntropyScanner.is_likely_secret(token))

    def test_low_entropy_word(self):
        token = "standard_plaintext_word"
        self.assertFalse(EntropyScanner.is_likely_secret(token))
