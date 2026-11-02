import unittest
from backend_security_sentinel.scanners.graphql_security_auditor import GraphQLSecurityAuditor

class TestGraphQLAuditor(unittest.TestCase):
    def test_introspection_query(self):
        q = "{ __schema { types { name } } }"
        res = GraphQLSecurityAuditor.audit_query(q)
        self.assertTrue(res["is_introspection"])
        self.assertEqual(res["risk_level"], "HIGH")
