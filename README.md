# Backend Security Sentinel 🛡️

[![CI/CD Security Pipeline](https://github.com/29rdx/backend-security-sentinel/actions/workflows/security-ci.yml/badge.svg)](https://github.com/29rdx/backend-security-sentinel/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://python.org)

An enterprise-grade DevSecOps vulnerability scanner and security posture auditor for backend APIs and distributed endpoints.

## 🚀 Key Modules
- **OWASP Header Auditor**: Verifies CSP, HSTS, X-Content-Type-Options, Referrer-Policy, Permissions-Policy.
- **CORS Leakage Detector**: Checks wildcard reflection, null origin bypass, and credentialed cross-origin leakage.
- **JWT Inspector**: Audits algorithm confusion, weak symmetric keys, expired claims, and signature validity.
- **Shannon Entropy Detector**: Detects leaked API credentials and authorization tokens in payload streams.
- **Executive HTML Reporter**: Compiles automated audit reports for security compliance teams.

## 💻 Installation & Usage
```bash
pip install -r requirements.txt
python -m sentinel.cli https://target-api.com --fail-on-high --html report.html
```
