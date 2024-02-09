'''Even game concrete logic'''
from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 100


def is_even(random_number: int) -> bool:
    return random_number & 1


def get_game_state():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    game_question = number
    return game_question, correct_answer
