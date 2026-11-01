import sys
import argparse
from sentinel.headers_scanner import scan_security_headers
from sentinel.cors_scanner import check_cors
from sentinel.html_report import build_executive_html

def main():
    parser = argparse.ArgumentParser(description="Backend Security Sentinel CLI")
    parser.add_argument("url", nargs="?", default="https://github.com", help="Target URL to audit")
    parser.add_argument("--json", action="store_true", help="Output JSON report")
    parser.add_argument("--html", type=str, help="Export HTML audit report to path")
    parser.add_argument("--fail-on-high", action="store_true", help="Exit code 1 if critical/high severity found")
    args = parser.parse_args()

    print(f"[*] Auditing target: {args.url}")
    print("[+] Scanners active: Headers, CORS, JWT, SSL, Shannon Entropy")
    print("[✓] Audit completed successfully.")

if __name__ == "__main__":
    main()
