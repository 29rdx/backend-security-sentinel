from sentinel.reporter import export_report
def test_export():
    assert export_report({'test': 1})
