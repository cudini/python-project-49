from random import randint


MIN_NUMBER = 1
MAX_NUMBER = 100


def is_even(random_number):
    return random_number & 1


def get_game_data():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    game_question = number
    return game_question, correct_answer
