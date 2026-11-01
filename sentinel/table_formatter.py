def render_summary_table(findings: list) -> str:
    out = ["+----------+--------------------------------+------------+",
           "| Severity | Vulnerability Name             | Status     |",
           "+----------+--------------------------------+------------+"]
    for f in findings:
        sev = f.get('severity', 'LOW')[:8].ljust(8)
        name = f.get('name', 'Issue')[:30].ljust(30)
        status = f.get('status', 'FAIL')[:10].ljust(10)
        out.append(f"| {sev} | {name} | {status} |")
    out.append("+----------+--------------------------------+------------+")
    return "\n".join(out)
