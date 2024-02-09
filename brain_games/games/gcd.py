'''Great common divisor game concrete logic'''
from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'

LOWER_LIMIT = 2
UPPER_LIMIT = 200


def get_gcd(number_1: int, number_2: int) -> int:
    while number_2:
        number_1, number_2 = number_2, number_1 % number_2
        return number_1


def get_game_state():
    first_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    second_number = randint(LOWER_LIMIT, UPPER_LIMIT)

    game_question = f'{first_number} {second_number}'
    correct_answer = get_gcd(first_number, second_number)

    return game_question, correct_answer
