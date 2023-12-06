#!/usr/bin/python3


def best_score(a_dictionary):
    # Check if the dictionary is empty
    if not a_dictionary:
        return None

    # key with the max value
    best_key = max(a_dictionary, key=a_dictionary.get)

    return best_key
