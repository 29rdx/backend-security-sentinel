# Frequently Asked Questions

### How does Sentinel verify OWASP API Security?
Sentinel performs non-destructive passive and active HTTP heuristic inspection on endpoints.

### What exit code is returned on vulnerability detection?
When `--fail-on-high` is provided, Sentinel returns code `1` if Critical or High severity findings are uncovered.
