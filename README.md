# 🛡️ Backend Security Sentinel

[![Security CI](https://github.com/29rdx/backend-security-sentinel/actions/workflows/security-ci.yml/badge.svg)](https://github.com/29rdx/backend-security-sentinel/actions)
[![GitHub Stars](https://img.shields.io/github/stars/29rdx/backend-security-sentinel?style=social)](https://github.com/29rdx/backend-security-sentinel/stargazers)
[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OWASP Compliant](https://img.shields.io/badge/OWASP-API%20Security%20Top%2010-emerald)](https://owasp.org/)

**Production-ready Backend Security Audit & Vulnerability Scanner** designed for high-concurrency microservices, REST/GraphQL APIs, and zero-trust backend architectures.

Developed by [**Rupraj Datta (@29rdx)**](https://github.com/29rdx) • Software & Backend Systems Engineer.

---

## 🌟 Stargazers & Community
If you find this security toolkit useful for auditing or hardening your APIs, **please star this repository!** It helps the tool reach more engineers and supports open-source security research.

[![Star History Chart](https://api.star-history.com/svg?repos=29rdx/backend-security-sentinel&type=Date)](https://star-history.com/#29rdx/backend-security-sentinel&Date)

---

## 🚀 Key Security Modules

- 🔒 **HTTP Security Headers Auditor**: Benchmarks endpoints against OWASP recommended baseline (HSTS, CSP, X-Frame-Options, Permissions-Policy).
- 🔑 **JWT Security Inspector**: Detects algorithm confusion vulnerabilities (`alg: none`), weak signatures, and missing expiration constraints.
- 🌐 **CORS Origin Misconfiguration Tester**: Audits wildcard reflections and authenticated credential leaks.
- ⚡ **Zero External Dependencies**: Pure Python standard library implementation for zero-dependency CI/CD pipelines.

---

## 📦 Quickstart

```bash
# Clone the repository
git clone https://github.com/29rdx/backend-security-sentinel.git
cd backend-security-sentinel

# Audit HTTP security headers of an API endpoint
python3 -m sentinel.cli scan-headers https://api.github.com

# Inspect and verify a JWT token
python3 -m sentinel.cli inspect-jwt "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

### JSON Output for DevSecOps Pipelines:
```bash
python3 -m sentinel.cli scan-headers https://example.com --json > audit-report.json
```

---

## 🛡️ License
Released under the [MIT License](LICENSE). Built for the global open-source developer community.
