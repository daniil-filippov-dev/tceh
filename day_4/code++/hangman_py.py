
import random


WORDS = [  # TODO: add more words
    'developer',
    'macos',
    'github',
]

MAX_ERRORS = 10


def return_random_word():
    return random.choice(WORDS)


def handle_user_input():
    # TODO: validate is letter
    user_input = input('Please, input letter: ')
    return user_input


def get_initial_statuses(word):
    statuses = []
    for letter in word:
        statuses.append(False)
    return statuses


def is_game_finished(statuses, current_errors):
    if current_errors >= MAX_ERRORS:
        return True

    for status in statuses:
        if not status:
            return False

    return True


def perfom_check_action(word, statuses, letter):
    # TODO: check for single action
    if letter not in word:
        return False

    for index, l in enumerate(word):
        if letter == l:
            statuses[index] = True

    return True


def print_word(word, statuses):
    for index, letter in enumerate(word):
        if statuses[index]:
            print(letter, end='')
        else:
            print('_', end=' ')
    print()


def main():
    word = return_random_word()
    statuses = get_initial_statuses(word)
    current_errors = 0

    while not is_game_finished(statuses, current_errors):
        print_word(word, statuses)
        print('Errors left: ', MAX_ERRORS - current_errors)
        letter = handle_user_input()
        result = perfom_check_action(word, statuses, letter)

        if not result:
            current_errors += 1

    if current_errors >= MAX_ERRORS:
        print('You lose!')
    else:
        print('You win!')


main()
