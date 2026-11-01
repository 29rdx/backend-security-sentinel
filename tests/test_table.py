from sentinel.table_formatter import render_summary_table

def test_table():
    table = render_summary_table([{"severity": "CRITICAL", "name": "Broken Auth", "status": "FAIL"}])
    assert "+----------+" in table
    assert "Broken Auth" in table
