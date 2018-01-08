"""For all-purpose tools"""

import random


def weighted_choice(choices, probability):
    """Chooses randomly based on given weight

    :type choices: list
    :type probability: list
    """

    total_probability = 0
    choice_positions = {}
    index = 0
    for choice in choices:
        if probability[index] > 0:
            choice_positions[total_probability] = choice
            total_probability += probability[index]
            index += 1

    choice_pos = random.uniform(0, total_probability)

    choice = None
    for choice_num in choice_positions:
        if choice_pos >= choice_num:  # Continue to find closest choice
            choice = choice_positions[choice_num]
        if choice_pos < choice_num:  # Until too high
            break

    return choice


def cap_all_words(phrase, seps):
    ind = 0
    phrase = phrase.capitalize()
    while ind < len(phrase):
        if len(phrase) - 1 > ind and phrase[ind] in seps:
            # If one char longer than index and index is a sep
            phrase = phrase[:ind + 1] + phrase[ind + 1].capitalize() \
                     + phrase[ind + 2:]
        ind += 1
    return phrase