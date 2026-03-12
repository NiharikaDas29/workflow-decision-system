import json

from rule_engine import evaluate_rules
from state_manager import save_state, is_duplicate, get_state
from dependency_service import get_credit_score

with open("configs/workflow.json") as f:
    workflow_config = json.load(f)


def run_workflow(data):

    request_id = data["request_id"]

    # idempotency check
    if is_duplicate(request_id):
        return {
            "message": "duplicate request",
            "previous_state": get_state(request_id)
        }

    try:

        # simulate external dependency
        credit_score = get_credit_score()

        data["credit_score"] = credit_score

    except Exception:

        save_state(request_id, "retry")

        return {
            "request_id": request_id,
            "decision": "retry",
            "reason": "dependency failure"
        }

    decision = evaluate_rules(data, workflow_config["rules"])

    save_state(request_id, decision)

    return {
        "request_id": request_id,
        "decision": decision
    }
