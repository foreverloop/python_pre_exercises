"""
This is an alternative solution to exercise 26.

THIS IS NOT MY OWN SOLUTION.
THIS IS NOT MY OWN SOLUTION.
THIS IS NOT MY OWN SOLUTION.

But it is much better than my solution, so I have it here for reference.
"""


def check_rows(matrix):
    for row in matrix:
        if len(set(row)) == 1:
            print(("player {} won.".format(row[0])))


def check_columns(matrix):
    matrix_transposed = [[row[index] for row in matrix] for index in range(len(matrix))]
    for row in matrix_transposed:
        if len(set(row)) == 1:
            print("player {} won.".format(row[0]))


def check_diagonals(matrix):
    major_diagonal = []
    minor_diagonal = []
    for index in range(len(matrix)):
        major_diagonal.append(matrix[index][index])
        minor_diagonal.append(matrix[index][2 - index])
    if len(set(major_diagonal)) == 1:
        print("player {} won.".format(major_diagonal[0]))
    elif len(set(minor_diagonal)) == 1:
        print("player {} won.".format(minor_diagonal[0]))


def check_total(matrix):
    check_rows(matrix)
    check_columns(matrix)
    check_diagonals(matrix)


winner_board = [[1, 0, 2],
                [1, 1, 2],
                [0, 1, 2]]
check_total(winner_board)
