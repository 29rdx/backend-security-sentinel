import json
import os

def load_owasp_rules(filepath: str = None) -> dict:
    if filepath is None:
        filepath = os.path.join(os.path.dirname(__file__), "rules", "owasp_top10.json")
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def evaluate_finding(rule_id: str, rules_db: dict) -> dict:
    return rules_db.get(rule_id, {
        "name": "Unknown Vulnerability",
        "severity": "LOW"
    })
