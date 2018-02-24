import random

print("Tic Tac Toe Game")
p1 = input("Podaj imię pierwszego gracza: ")
p2 = input("Podaj imię drugiego gracza: ")

x = "X"
o = "O"

items_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def who_first():
    players = [p1, p2]
    random.shuffle(players)
    pl1 = players[0]
    pl2 = players[1]
    print()
    print("{} zaczyna grę!".format(players[0]).capitalize())
    print("Wasze oznaczenia: ")
    print("{}: {}".format(pl1.capitalize(), x))
    print("{}: {}".format(pl2.capitalize(), o))
    print()
    return pl1, pl2


def print_board(board):
    print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | " + "\n"
          + " | " + board[3] + " | " + board[4] + " | " + board[5] + " | " + "\n"
          + " | " + board[6] + " | " + board[7] + " | " + board[8] + " | " + "\n")


def check_columns(board, symbol):
    if board[0] == symbol and board[3] == symbol and board[6] == symbol \
            or board[1] == symbol and board[4] == symbol and board[7] == symbol \
            or board[2] == symbol and board[5] == symbol and board[8] == symbol:
        print("win")
    else:
        print("not win")


def check_rows(board, symbol):
    if board[0] == symbol and board[1] == symbol and board[2] == symbol \
            or board[3] == symbol and board[4] == symbol and board[5] == symbol \
            or board[6] == symbol and board[7] == symbol and board[8] == symbol:
        print("win")
    else:
        print("not win")


def check_diagonals(board, symbol):
    if board[0] == symbol and board[4] == symbol and board[8] == symbol \
            or board[2] == symbol and board[4] == symbol and board[6] == symbol:
        print("win")
    else:
        print("not win")


def start():
    steps = 0
    play = True
    players = who_first()
    print_board(items_board)
    while play:
        if steps < 9:
            position = input("Podaj pozycję: ")
            for n, i in enumerate(items_board):
                if i == position:
                    items_board[n] = x
            print_board(items_board)
            check_columns(items_board, x)
            steps += 1
        else:
            print("REMIS")
            play = False


start()
