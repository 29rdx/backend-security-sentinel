class GraphQLSecurityAuditor:
    """Inspects GraphQL queries for recursive depth and introspection risks."""
    @staticmethod
    def audit_query(query_string: str) -> dict:
        is_introspection = "__schema" in query_string or "__type" in query_string
        depth = query_string.count("{")
        excessive_depth = depth > 7
        return {
            "is_introspection": is_introspection,
            "query_depth": depth,
            "excessive_depth": excessive_depth,
            "risk_level": "HIGH" if (is_introspection or excessive_depth) else "LOW"
        }
