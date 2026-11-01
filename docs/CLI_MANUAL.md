# Sentinel CLI Reference Manual

### Basic Scan
```bash
python -m sentinel.cli https://target.domain
```

### Full Enterprise Audit with HTML Output
```bash
python -m sentinel.cli https://api.target.com --html executive_summary.html --fail-on-high
```

### Output Format Flags
- `--json`: Machine-readable structured JSON for CI pipelines.
- `--html <path>`: Generates visual executive dashboard.
- `--fail-on-high`: Non-zero exit code if high or critical issues exist.
