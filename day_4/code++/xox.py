import random


EQ_X = "X"
EQ_O = "O"
EMPTY = " "
COUNT = 9


def add_board():
    """
    Создание игральной доски
    :return: доска для игры
    """
    board = []
    for i in range(COUNT):
        board.append(EMPTY)
    return board


def write_board(board):
    """
    Отрисовка игральной доски
    :param board: доска
    :return: None
    """
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


def pieces():
    """
    Определяет, кто будет играть крестиками, кто - ноликами
    :return: значения крестика и нолика
    """
    ans = None
    while ans not in("y","n"):
        ans = input("Хотите начинать первым? (y/n): \n")
    if ans == "y":
        human = EQ_X
        computer = EQ_O
    else:
        human = EQ_O
        computer = EQ_X
    return human, computer


def human_step(board):
    """
    Получение хода человека
    :param board: доска
    :return: поле
    """
    step = None
    moves = legal_moves(board)
    while step not in moves:
        step = int(input("Ваш ход. Одно из полей [0-8]: \n"))
        if step not in moves:
            print("Это поле уже занято, попробуйте выбрать другое")
    return step


def computer_step(board, computer, human):
    """
    Получение хода компьютера
    :param board: доска
    :return: поле
    """
    board = board[:]
    print("Ход компьютера: ")
    for s in legal_moves(board):
        board[s] = computer
        if winner(board) == computer:
            print(s)
            return s
        board[s] = EMPTY
    for s in legal_moves(board):
        board[s] = human
        if winner(board) == human:
            print(s)
            return s
        board[s] = EMPTY
    step = random.choice(legal_moves(board))
    print(step)
    return step


def winner(board):
    """
    Определение победителя
    :param board: доска
    :return: победитель
    """
    WAYS_WIN = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    )
    for i in WAYS_WIN:
        if board[i[0]] == board[i[1]] == board[i[2]] != EMPTY:
            winner = board[i[0]]
            return winner
    if EMPTY not in board:
        s = "Ничья"
        return s


def legal_moves(board):
    """
    Создает список доступных ходов
    :param board: доска
    :return: список ходов
    """
    res = []
    for i in range(COUNT):
        if board[i] == EMPTY:
            res.append(i)
    return res


def next_turn(turn):
    """
    Переход хода
    :param turn: значение хода
    :return:
    """
    if turn == EQ_X:
        return EQ_O
    else:
        return EQ_X


def main():
    """
    Основной алгоритм запуска игры
    :return: None
    """
    print("""Игра крестики-нолики, противостояние с компьютером\n
    Чтобы сделать ход, необходимо ввести число от 0 до 8. Число однозначно соответствует
    полям доски, как показано на рисунке ниже:
    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8
    """)
    human, computer = pieces()
    turn = EQ_X
    board = add_board()
    write_board(board)
    while not winner(board):
        if turn == human:
            step = human_step(board)
            board[step] = human
        else:
            step = computer_step(board, computer, human)
            board[step] = computer
        write_board(board)
        turn = next_turn(turn)
        theWinner = winner(board)
    if theWinner == computer:
        print("Победитель компьютер")
    elif theWinner == "Ничья":
        print("Победителей нет")
    else:
        print("Вы победили. Поздравляем")


if __name__ == '__main__':
    main()
    input("Нажмите Enter, чтобы выйти")