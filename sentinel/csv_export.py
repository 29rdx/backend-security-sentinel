import csv
import io

def export_findings_csv(findings: list) -> str:
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(["Severity", "Rule ID", "Description"])
    for f in findings:
        writer.writerow([f.get("severity", ""), f.get("id", ""), f.get("desc", "")])
    return buf.getvalue()
