from random import randint
from math import sqrt


DESCRIPTION = 'Answer "yes" if given is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 50


def is_prime(number):
    if number < 2 and number % 2 == 0:
        return False
    for devisor in range(2, int(sqrt(number)) + 1):
        if number % devisor == 0:
            return False
        return True


def get_game_data():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    game_question = number
    return game_question, correct_answer
