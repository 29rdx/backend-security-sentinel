import json
def export_report(data, fmt='json'):
    return json.dumps(data, indent=2)
