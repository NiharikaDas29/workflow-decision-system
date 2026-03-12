import random

def get_credit_score():

    # simulate external dependency
    score = random.randint(300, 900)

    if score < 350:
        raise Exception("Credit service failure")

    return score
