'''Progression game concrete logic'''
from random import randint


DESCRIPTION = 'What number is missing in the progression?'

PROGRESSION_LENGTH = 10
LOWER_BOUND = 1
UPPER_BOUND = 50
DELTA_LIMIT = 10


def get_quest_and_answer():

    delta = randint(LOWER_BOUND, DELTA_LIMIT)
    first_number = randint(LOWER_BOUND, UPPER_BOUND)
    missing_number = randint(0, PROGRESSION_LENGTH - 1)
    last_number = first_number + (PROGRESSION_LENGTH * delta)

    progression = []
    for number in range(first_number, last_number, delta):
        progression.append(str(number))

    correct_answer = progression[missing_number]
    progression[missing_number] = '..'
    game_question = ' '.join(map(str, progression))

    return game_question, correct_answer
