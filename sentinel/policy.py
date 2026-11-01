import os

class PolicyEngine:
    def __init__(self, policy_name: str = "default"):
        self.policy_name = policy_name

    def is_header_enforced(self, header: str) -> bool:
        enforced = ["Strict-Transport-Security", "Content-Security-Policy", "X-Frame-Options"]
        return header in enforced
