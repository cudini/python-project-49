'''Great common divisor game concrete logic'''
from math import gcd
from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'

LOWER_LIMIT = 2
UPPER_LIMIT = 50


def get_game_state():
    first_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    second_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    game_question = f'{first_number} {second_number}'
    correct_answer = str(gcd(first_number, second_number))
    return game_question, correct_answer
