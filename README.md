# 🛡️ Backend Security Sentinel
### Production-grade OWASP API Security Auditor & Vulnerability Scanner

[![PyPI Version](https://img.shields.io/badge/pypi-v1.3.0-blue.svg)](https://github.com/29rdx/backend-security-sentinel)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OWASP Coverage](https://img.shields.io/badge/OWASP-API%20Top%2010-red.svg)](https://owasp.org/www-project-api-security/)

## 🚀 Security Scanners Included

- **BOLA / IDOR Scanner**: Detects sequential numeric references and predicts authorization bypass vectors.
- **SSRF & Cloud Metadata Auditor**: Prevents internal network and cloud provider credential endpoint probing (`169.254.169.254`).
- **JWT Confusion Auditor**: Detects \`alg: none\` attacks and key confusion vulnerabilities.
- **RFC 6585 Rate Limiting Evaluator**: Enforces \`Retry-After\` and \`429\` throttling standards.
- **GraphQL Depth & Introspection Auditor**: Flags production schema exposure and recursive circular queries.
- **CORS Misconfiguration Analyzer**: Blocks wildcard credentials combinations.
- **Shannon Entropy Secret Scanner**: Analyzes API response streams for exposed high-entropy secrets and private keys.

## 📦 Installation & Usage
```bash
pip install -e .
sentinel --audit-ssrf http://169.254.169.254/latest/meta-data/
sentinel --audit-bola /api/v1/users/42/billing
```
