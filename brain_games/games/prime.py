from random import randint
from math import sqrt


DESCRIPTION = 'Answer "yes" if given is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 50


def get_random_number():
    return randint(MIN_NUMBER, MAX_NUMBER)


def is_prime(random_number):
    if random_number < 2 & 1:
        return False
    for devisor in range(2, int(sqrt(get_random_number)) + 1):
        if random_number % devisor == 0:
            return False
        return True


def check_answer():
    if is_prime(get_random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    name_of_game = prime_number
    return name_of_game, correct_answer
