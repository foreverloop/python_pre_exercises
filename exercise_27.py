"""
Exercise 27 (and Solution)

The next logical step is to deal with handling user input.
When a player (say player 1, who is X) wants to place an X on the screen, they can’t just click on a terminal.
So we are going to approximate this clicking simply by asking the user
for a coordinate of where they want to place their piece.

And ask Player 2 for their move, printing an O in that place.
"""

import math

horizontal_bar = '---'
vertical_bar = '|     '


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


game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
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
    else:
        marker = "X"

    co_ord1 = int(input("Enter co-ordinates row: "))
    co_ord2 = int(input("Enter co-ordinate column: "))
    marker_history[marker_history.index([co_ord1, co_ord2, p_marker])] = [co_ord1, co_ord2, marker]
    generate_grid(9)
    game[co_ord1][co_ord2] = 1  # add logic for 1 or 0 later
