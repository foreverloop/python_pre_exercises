"""
Exercise 29 (and Solution)
The next step is to put all these three components together to make a two-player Tic Tac Toe game!
Your challenge in this exercise is to use the functions from those previous exercises
all together in the same program to make a two-player game that you can play with a friend.
There are a lot of choices you will have to make when completing this exercise,
so you can go as far or as little as you want with it.

Here are a few things to keep in mind:
You should keep track of who won - if there is a winner, show a congratulatory message on the screen.
If there are no more moves left, don’t ask for the next player’s move!
As a bonus, you can ask the players if they
want to play again and keep a running tally of who won more - Player 1 or Player 2.
"""

import math

horizontal_bar = '---'
vertical_bar = '|     '


def close_down():
    print('game complete, ending')
    exit()
    return


def check_rows(matrix):
    for row in matrix:
        if len(set(row)) == 1:
            print(("player {} won.".format(row[0])))
            close_down()


def check_columns(matrix):
    matrix_transposed = [[row[index] for row in matrix] for index in range(len(matrix))]
    for row in matrix_transposed:
        if len(set(row)) == 1:
            print("player {} won.".format(row[0]))
            close_down()


def check_diagonals(matrix):
    major_diagonal = []
    minor_diagonal = []
    for index in range(len(matrix)):
        major_diagonal.append(matrix[index][index])
        minor_diagonal.append(matrix[index][2 - index])
    if len(set(major_diagonal)) == 1:
        print("player {} won.".format(major_diagonal[0]))
        close_down()
    elif len(set(minor_diagonal)) == 1:
        print("player {} won.".format(minor_diagonal[0]))
        close_down()


def check_total(matrix):
    check_rows(matrix)
    check_columns(matrix)
    check_diagonals(matrix)


def make_string(generate_number):
    return horizontal_bar * (generate_number + 1)


def generate_grid(squares):
    required_bars = int(math.sqrt(squares))
    generated_horizontal_line = make_string(required_bars)

    # start printing the board

    print(generated_horizontal_line)
    row1 = ''
    for marker_point in marker_history:
        if marker_point[0] == 0:
            row1 += '|  ' + marker_point[2]
    print(row1 + '|')

    print(generated_horizontal_line)
    row2 = ''
    for marker_point in marker_history:
        if marker_point[0] == 1:
            row2 += '|  ' + marker_point[2]
    print(row2 + '|')

    print(generated_horizontal_line)
    row3 = ''
    for marker_point in marker_history:
        if marker_point[0] == 2:
            row3 += '|  ' + marker_point[2]
    print(row3 + '|')

    print(generated_horizontal_line)

    return 0


player = 0
game = [[99, 88, 77], [66, 55, 44], [33, 22, 11]]
rounds = 0
marker = ''
p_marker = ' '  # placeholder marker
marker_history = [[0, 0, p_marker], [0, 1, p_marker], [0, 2, p_marker],
                  [1, 0, p_marker], [1, 1, p_marker], [1, 2, p_marker],
                  [2, 0, p_marker], [2, 1, p_marker], [2, 2, p_marker]]

while True:
    rounds += 1
    if rounds % 2 == 0:
        marker = "O"
        player = 2
    else:
        marker = "X"
        player = 1

    co_ord1 = int(input("Enter co-ordinates row: "))
    co_ord2 = int(input("Enter co-ordinate column: "))
    marker_history[marker_history.index([co_ord1, co_ord2, p_marker])] = [co_ord1, co_ord2, marker]
    generate_grid(9)
    game[co_ord1][co_ord2] = player  # add logic for 1 or 0 later
    check_total(game)
