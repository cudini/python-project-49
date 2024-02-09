'''Main game logic interface'''
import prompt


GAME_CONTINUE = 3


def start_game(game):

    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.DESCRIPTION)
    game_try = 0

    while game_try < GAME_CONTINUE:
        game_question, correct_answer = game.get_game_state()
        print(f'Question: {game_question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let 's try again, {user_name}!")
            return

        game_try += 1

    print(f'Congratulanions, {user_name}!')
