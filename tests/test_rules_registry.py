import unittest
from backend_security_sentinel.rules.registry import RuleRegistry

class TestRuleRegistry(unittest.TestCase):
    def test_registry_contains_all_10_rules(self):
        rules = RuleRegistry.list_rules()
        self.assertEqual(len(rules), 10)
        self.assertIn("API1", rules)
        self.assertIn("API7", rules)
