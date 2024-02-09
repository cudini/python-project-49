'''Progression game concrete logic'''
from random import randint


DESCRIPTION = 'What number is missing in the progression?'

PROGRESSION_LENGTH = 10
LOWER_BOUND = 1
UPPER_BOUND = 50
DELTA_LIMIT = 10


def get_game_state():

    delta = randint(LOWER_BOUND, DELTA_LIMIT)
    first_number = randint(LOWER_BOUND, UPPER_BOUND)
    missing_number = randint(LOWER_BOUND, PROGRESSION_LENGTH)
    progression = to_string(make_progression(first_number, delta))

    correct_answer = progression[missing_number]
    progression[missing_number] = '..'
    game_question = ' '.join(progression)

    return game_question, correct_answer


def make_progression(first_number: int, delta: int) -> range:
    last_number = first_number + (PROGRESSION_LENGTH * delta)
    return range(first_number, last_number, delta)


def to_string(progression) -> str:
    result = []
    for index in progression:
        result.append(str(index))
    return result
