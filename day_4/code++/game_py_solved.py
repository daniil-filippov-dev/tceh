# -*- coding: utf-8 -*-

# `random` module is used to shuffle field, see§:
# https://docs.python.org/3/library/random.html#random.shuffle
import random


# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of: 
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    field = list(range(1, 17))
    field[-1] = EMPTY_MARK
    random.shuffle(field)

    # possible_moves = list(MOVES.keys())
    # applied_moves = 0
    # while applied_moves < 100:
    #     random_move = random.choice(possible_moves)

    #     try:
    #         field = perform_move(field, random_move)
    #         applied_moves += 1
    #     except IndexError:
    #         continue

    return field


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    for i in range(0, 16, 4):
        print(field[i:i + 4])
    print('\n')


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    ideal = list(range(1, 16))
    ideal.append(EMPTY_MARK)

    return ideal == field


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    current_position = field.index(EMPTY_MARK)

    if key == 's' and current_position >= 12:
        raise IndexError('Cant move down')

    if key == 'd' and current_position % 4 == 3:
        raise IndexError('Cant move right')

    if key == 'w' and current_position < 4:
        raise IndexError('Cant move up')

    if key == 'a' and current_position % 4 == 0:
        raise IndexError('Cant move left')

    delta = MOVES[key]
    field[current_position], field[current_position + delta] = field[current_position + delta], field[current_position]
    return field

def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up, 
        's' - down,
        'a' - left, 
        'd' - right
    :return: <str> current move.
    """
    while True:
        user_move = input('Please, input your move: ')
        if user_move in MOVES.keys():
            return user_move


def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    field = shuffle_field()
    # field = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 'x', 15]

    while not is_game_finished(field):
        try:
            print_field(field)
            move = handle_user_input()
            field = perform_move(field, move)
        except IndexError as e:
            print(e)

    print('Game is finished!')


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do

    main()
