from sentinel.csv_export import export_findings_csv

def test_csv_export():
    csv_str = export_findings_csv([{"severity": "HIGH", "id": "API1", "desc": "BOLA issue"}])
    assert "Severity,Rule ID,Description" in csv_str
    assert "HIGH,API1,BOLA issue" in csv_str
