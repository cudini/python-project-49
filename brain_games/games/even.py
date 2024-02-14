'''Even game concrete logic'''
from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 100


def get_quest_and_answer():

    game_question = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'no' if game_question % 2 != 0 else 'yes'

    return game_question, correct_answer
