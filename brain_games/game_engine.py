'''Main game logic interface'''
import prompt


GAME_CONTINUE = 3


def start_game(game):

    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.DESCRIPTION)
    tries_left = GAME_CONTINUE

    while tries_left > 0:
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

        tries_left -= 1

    print(f'Congratulations, {user_name}!')
