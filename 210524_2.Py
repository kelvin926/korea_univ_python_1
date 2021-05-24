def frequency(toeicScores):
    counters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for toeicScore in toeicScores:
        counters[toeicScore//100] += 1
    return counters