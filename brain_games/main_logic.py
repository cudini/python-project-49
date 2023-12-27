import prompt


GAME_SCORE = 3


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game.DESCRIPTION)
    game_try = 0
    while game_try < GAME_SCORE:
        question, correct_answer = game.get_data()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")
            print(f'Let\'s try again, {name}!')
            return
        game_try += 1
    print(f'Congratulanions, {name}!')
