state_db = {}

def save_state(request_id, state):
    state_db[request_id] = state


def get_state(request_id):
    return state_db.get(request_id)


def is_duplicate(request_id):
    return request_id in state_db
