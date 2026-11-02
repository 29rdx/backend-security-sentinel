class RuleRegistry:
    """Centralized registry of OWASP API Top 10 rules."""
    RULES = {
        "API1": "Broken Object Level Authorization",
        "API2": "Broken Authentication",
        "API3": "Broken Object Property Level Authorization",
        "API4": "Unrestricted Resource Consumption",
        "API5": "Broken Function Level Authorization",
        "API6": "Unrestricted Access to Sensitive Business Flows",
        "API7": "Server Side Request Forgery",
        "API8": "Security Misconfiguration",
        "API9": "Improper Inventory Management",
        "API10": "Unsafe Consumption of APIs"
    }

    @classmethod
    def list_rules(cls) -> dict:
        return cls.RULES.copy()
