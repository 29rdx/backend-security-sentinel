#!/usr/bin/env python3
import sys
import argparse
import json
from sentinel.headers_scanner import scan_headers
from sentinel.jwt_analyzer import analyze_jwt

def print_banner():
    banner = """
    ╔══════════════════════════════════════════════════════╗
    ║   🛡️  BACKEND SECURITY SENTINEL • OWASP AUDITOR   ║
    ║        Author: Rupraj Datta (github.com/29rdx)        ║
    ╚══════════════════════════════════════════════════════╝
    """
    print(banner)

def main():
    parser = argparse.ArgumentParser(description="Backend Security Sentinel - Production Security CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Headers scan
    headers_parser = subparsers.add_parser("scan-headers", help="Audit HTTP security headers against OWASP guidelines")
    headers_parser.add_argument("url", help="Target URL (e.g. https://api.example.com)")
    headers_parser.add_argument("--json", action="store_true", help="Output raw JSON")

    # JWT analyzer
    jwt_parser = subparsers.add_parser("inspect-jwt", help="Inspect and audit JWT token for security weaknesses")
    jwt_parser.add_argument("token", help="Raw JWT string")
    jwt_parser.add_argument("--json", action="store_true", help="Output raw JSON")

    args = parser.parse_args()

    if not args.command:
        print_banner()
        parser.print_help()
        sys.exit(0)

    if args.command == "scan-headers":
        result = scan_headers(args.url)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_banner()
            if "error" in result:
                print(f"❌ Scan failed: {result['error']}")
                sys.exit(1)
            print(f"🎯 Target URL: {result['url']} (Status: {result['status_code']})")
            print(f"🛡️  Security Compliance Score: {result['security_score']}%")
            print(f"📊 Present: {result['present_headers']} | Missing: {result['missing_headers']}\n")
            print("Audit Findings:")
            for f in result["findings"]:
                mark = "✅" if f["status"] == "PRESENT" else "⚠️"
                print(f"  {mark} {f['header']:<28} [{f['status']}] - {f['description']}")

    elif args.command == "inspect-jwt":
        result = analyze_jwt(args.token)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_banner()
            if "error" in result:
                print(f"❌ Analysis failed: {result['error']}")
                sys.exit(1)
            print(f"🔑 Algorithm: {result['algorithm']}")
            print(f"🚨 Vulnerabilities Detected: {result['vulnerability_count']}\n")
            for v in result["vulnerabilities"]:
                print(f"  [{v['severity']}] {v['vuln']}: {v['impact']}")

if __name__ == "__main__":
    main()
