'''Even game concrete logic'''
from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_state():

    number = randint(0, 100)
    correct_answer = 'no' if number % 2 else 'yes'

    return number, correct_answer
