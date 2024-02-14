'''Main game logic interface'''
import prompt


GAME_CONTINUES = 3


def start_game(game):

    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.DESCRIPTION)

    for _ in range(GAME_CONTINUES):
        game_question, correct_answer = game.get_quest_and_answer()
        print(f'Question: {game_question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
        print('Correct!')

    print(f'Congratulations, {user_name}!')
