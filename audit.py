audit_logs = []

def log_audit(request_id, rule_name, result):

    audit_logs.append({
        "request_id": request_id,
        "rule": rule_name,
        "result": result
    })


def get_audit_logs():
    return audit_logs
