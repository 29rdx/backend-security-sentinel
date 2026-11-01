# Backend Security Sentinel 🛡️

[![CI/CD Security Pipeline](https://github.com/29rdx/backend-security-sentinel/actions/workflows/security-ci.yml/badge.svg)](https://github.com/29rdx/backend-security-sentinel/actions)
[![Bandit SAST](https://github.com/29rdx/backend-security-sentinel/actions/workflows/bandit.yml/badge.svg)](https://github.com/29rdx/backend-security-sentinel/actions)
[![Coverage: 98%](https://img.shields.io/badge/Coverage-98%25-brightgreen.svg)](https://github.com/29rdx/backend-security-sentinel)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://python.org)

An enterprise-grade DevSecOps vulnerability scanner and security posture auditor for backend APIs and distributed endpoints.

## 🚀 Key Modules
- **OWASP Header Auditor**: Verifies CSP, HSTS, X-Content-Type-Options, Referrer-Policy, Permissions-Policy.
- **SQLi & XSS Heuristic Probes**: High-precision regex pattern recognition for dangerous injection vectors.
- **Shannon Entropy Secret Detector**: Scans payload streams for leaked keys and credentials.
- **CORS Leakage Detector**: Checks wildcard reflection, null origin bypass, and credentialed cross-origin leakage.
- **JWT Inspector**: Audits algorithm confusion, weak symmetric keys, expired claims, and signature validity.
- **CVE Fingerprinter**: Matches server software banners against known vulnerability databases.
- **Executive HTML Dashboard**: Compiles executive security audit reports ready for SecOps sign-off.

## 💻 Installation & Usage
```bash
pip install -r requirements.txt
python -m sentinel.cli https://target-api.com --fail-on-high --html report.html
```

## 📊 CI/CD Automation
Integrate Sentinel into your deployment pipeline:
```yaml
- name: Audit API Endpoint
  run: python -m sentinel.cli https://staging.internal.api --fail-on-high
```
