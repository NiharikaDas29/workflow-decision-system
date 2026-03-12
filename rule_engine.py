from audit import log_audit


def evaluate_rules(data, rules):

    for rule in rules:

        field = rule["field"]
        value = rule["value"]
        name = rule["name"]

        if data.get(field, 0) < value:

            log_audit(data["request_id"], name, "FAILED")

            return rule["on_fail"]

        log_audit(data["request_id"], name, "PASSED")

    return "approved"
