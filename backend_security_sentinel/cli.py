import argparse
import sys
from .scanners.ssrf_scanner import SSRFScanner
from .scanners.bola_scanner import BOLAScanner
from .rules.registry import RuleRegistry

def main():
    parser = argparse.ArgumentParser(description="Backend Security Sentinel CLI")
    parser.add_argument("--audit-ssrf", help="Audit destination URL for SSRF vulnerabilities")
    parser.add_argument("--audit-bola", help="Audit API path for BOLA / IDOR risks")
    parser.add_argument("--list-rules", action="store_true", help="List OWASP API Top 10 rules")
    args = parser.parse_args()

    if args.list_rules:
        for k, v in RuleRegistry.list_rules().items():
            print(f"[{k}] {v}")
    elif args.audit_ssrf:
        res = SSRFScanner.is_ssrf_vulnerable(args.audit_ssrf)
        print(f"SSRF Target: {res['target_url']} | Vulnerable: {res['vulnerable']} | Severity: {res['severity']}")
    elif args.audit_bola:
        res = BOLAScanner.analyze_endpoint(args.audit_bola)
        print(f"Endpoint: {res['endpoint']} | Risk: {res['risk_level']} | Type: {res['reference_type']}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
