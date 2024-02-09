'''Even game concrete logic'''
from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 100


def get_game_state():

    number = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'no' if number % 2 != 0 else 'yes'

    return number, correct_answer
