#!/usr/bin/python3
def best_score(a_dictionary):
    best = {"name": None, "score": None}
    if a_dictionary is not None:
        for name, score in a_dictionary.items():
            if best["score"] is None or score >= best["score"]:
                best["name"] = name
                best["score"] = score
    return best["name"]
