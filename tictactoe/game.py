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
    print("Losuje kolejność...")
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


def check_columns(board, symbol, player):
    if board[0] == symbol and board[3] == symbol and board[6] == symbol \
            or board[1] == symbol and board[4] == symbol and board[7] == symbol \
            or board[2] == symbol and board[5] == symbol and board[8] == symbol:
        print("{} jesteś zwycięzcą".format(player))
        return False
    else:
        return True


def check_rows(board, symbol, player):
    if board[0] == symbol and board[1] == symbol and board[2] == symbol \
            or board[3] == symbol and board[4] == symbol and board[5] == symbol \
            or board[6] == symbol and board[7] == symbol and board[8] == symbol:
        print("{} jesteś zwycięzcą".format(player))
        return False
    else:
        return True


def check_diagonals(board, symbol, player):
    if board[0] == symbol and board[4] == symbol and board[8] == symbol \
            or board[2] == symbol and board[4] == symbol and board[6] == symbol:
        print("{} jesteś zwycięzcą".format(player))
        return False
    else:
        return True


def check_position(board, position):
    if board[int(position) - 1] == 'X' or board[int(position) - 1] == "O":
        return False
    else:
        return True


def start():
    steps = 0
    game_in_progress = True
    change = True
    players = who_first()
    player1 = players[0].capitalize()
    player2 = players[1].capitalize()
    print_board(items_board)
    while game_in_progress:
        if steps < 9:
            if change:
                position = input("{} podaj pozycję: ".format(player1))
                print()
                engaged_position = check_position(items_board, position)
                if engaged_position:
                    for n, i in enumerate(items_board):
                        if i == position:
                            items_board[n] = x
                    print_board(items_board)
                    end_by_columns = check_columns(items_board, x, player1)
                    end_by_rows = check_rows(items_board, x, player1)
                    end_by_diagonals = check_diagonals(items_board, x, player1)
                    if end_by_columns and end_by_diagonals and end_by_rows:
                        steps += 1
                        change = False
                    else:
                        game_in_progress = False
                else:
                    print("To pole jest już zajęte. Wybierz jeszcze raz")
            else:
                position = input("{} podaj pozycję: ".format(player2))
                print()
                check_position(items_board, position)
                engaged_position = check_position(items_board, position)
                if engaged_position:
                    for n, i in enumerate(items_board):
                        if i == position:
                            items_board[n] = o
                    print_board(items_board)
                    end_by_columns = check_columns(items_board, x, player1)
                    end_by_rows = check_rows(items_board, x, player1)
                    end_by_diagonals = check_diagonals(items_board, x, player1)
                    if end_by_columns and end_by_diagonals and end_by_rows:
                        steps += 1
                        change = True
                    else:
                        game_in_progress = False
                else:
                    print("To pole jest już zajęte. Wybierz jeszcze raz")
        else:
            print("REMIS")
            game_in_progress = False


start()
