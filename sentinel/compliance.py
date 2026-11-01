class ComplianceChecker:
    CONTROLS = {
        "CC6.1": "Logical access controls enforced",
        "CC6.6": "Vulnerabilities identified and addressed",
        "CC6.7": "Transmission of confidential data encrypted"
    }

    def evaluate_compliance(self, findings: list) -> dict:
        passed = len(findings) == 0
        return {"compliant": passed, "controls": self.CONTROLS}
