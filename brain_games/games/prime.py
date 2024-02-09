'''Prime game concrete logic'''
from random import randint
from math import sqrt


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 50


def is_prime(number: int) -> bool:

    if number < 2 or number % 2 == 0:
        return False

    for devisor in range(2, int(sqrt(number)) + 1):
        if number % devisor == 0:
            return False

    return True


def get_game_state():

    number = randint(MIN_NUMBER, MAX_NUMBER)

    correct_answer = 'yes' if is_prime(number) else 'no'
    game_question = number

    return game_question, correct_answer
