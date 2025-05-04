CLEANLINESS_SCALE = ['Messy', 'Moderate', 'Clean']

MATCH_WEIGHTS = {
    'sleep_time': 25,
    'cleanliness': 25,
    'work_schedule': 25,
    'food_habits': 25
}

def score_profiles(p1, p2):
    score = 0
    for key in MATCH_WEIGHTS:
        if p1[key] == p2[key]:
            score += MATCH_WEIGHTS[key]
        elif key == 'cleanliness':
            try:
                idx1 = CLEANLINESS_SCALE.index(p1[key])
                idx2 = CLEANLINESS_SCALE.index(p2[key])
                if abs(idx1 - idx2) == 1:
                    score += MATCH_WEIGHTS[key] // 2
            except ValueError:
                pass
    return score