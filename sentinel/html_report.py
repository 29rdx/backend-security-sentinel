import html

def build_executive_html(report_data: dict) -> str:
    target = html.escape(report_data.get("target", "N/A"))
    score = report_data.get("score", 100)
    findings = report_data.get("findings", [])
    
    rows = ""
    for f in findings:
        sev = html.escape(f.get("severity", "LOW"))
        name = html.escape(f.get("name", "Issue"))
        desc = html.escape(f.get("desc", ""))
        rows += f"<tr><td><span class='badge {sev.lower()}'>{sev}</span></td><td>{name}</td><td>{desc}</td></tr>"
        
    return f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Security Audit Report - {target}</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0d1117; color: #c9d1d9; padding: 40px; }}
    .container {{ max-width: 900px; margin: 0 auto; background: #161b22; padding: 30px; border-radius: 8px; border: 1px solid #30363d; }}
    h1 {{ color: #58a6ff; }}
    .score {{ font-size: 48px; font-weight: bold; color: {'#3fb950' if score >= 80 else '#f85149'}; }}
    table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
    th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #21262d; }}
    .badge {{ padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold; }}
    .badge.critical {{ background: #f85149; color: white; }}
    .badge.high {{ background: #d29922; color: black; }}
  </style>
</head>
<body>
  <div class="container">
    <h1>Backend Security Sentinel - Executive Audit</h1>
    <p>Target: <strong>{target}</strong></p>
    <div>Security Posture Score: <span class="score">{score}/100</span></div>
    <table>
      <thead><tr><th>Severity</th><th>Vulnerability</th><th>Details</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>
  </div>
</body>
</html>"""
