'''Calculator game concrete logic'''
from random import randint, choice
from operator import add, sub, mul


DESCRIPTION = 'What is the result of the expression?'

MIN_NUMBER = 0
MAX_NUMBER = 50
OPERATORS = [('+', add), ('-', sub), ('*', mul)]


def get_quest_and_answer():

    operand_1 = randint(MIN_NUMBER, MAX_NUMBER)
    operand_2 = randint(MIN_NUMBER, MAX_NUMBER)
    description, operation = choice(OPERATORS)

    game_question = f'{operand_1} {description} {operand_2}'
    correct_answer = str(operation(operand_1, operand_2))

    return game_question, correct_answer
