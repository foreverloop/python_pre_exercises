"""
Exercise 26 (and Solution)
Tic Tac Toe Winner

If a game of Tic Tac Toe is represented as a list of lists, like so:

game = [[1, 2, 0],[2, 1, 0],[2, 1, 1]]

where a 0 means an empty square, a 1 means that player 1 put their token in that space,
and a 2 means that player 2 put their token in that space.

Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
tell me whether anyone has won, and tell me which player won, if any.
A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal.
Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.

Here are some more examples to work with:

winner_is_2 = [[2, 2, 0],[2, 1, 0],[2, 1, 1]]
"""


def generate_horizontal_win():
    identities = []
    winner1 = [1, 1, 1]
    winner2 = [2, 2, 2]
    loser = [0, 0, 0]

    for x in range(0, 3):
        game1 = [loser, loser, loser]
        game1.pop(x)
        game1.insert(x, winner1)
        identities.append(game1)

        game2 = [loser, loser, loser]
        game2.pop(x)
        game2.insert(x, winner2)
        identities.append(game2)
    return identities


def generate_vertical_win():
    identities = []
    for x in range(0, 3):
        win_pattern = [0, 0, 0]
        win_pattern.pop(x)
        win_pattern.insert(x, 1)
        winning_game = [win_pattern, win_pattern, win_pattern]
        identities.append(winning_game)

        win_pattern2 = [0, 0, 0]
        win_pattern2.pop(x)
        win_pattern2.insert(x, 2)
        winning_game2 = [win_pattern2, win_pattern2, win_pattern2]
        identities.append(winning_game2)
    return identities


def generate_cross_win():
    identities = []

    for z in range(1, 3):
        winning_game = []
        win_pattern = [0, 0, 0]
        win_pattern.pop(0)
        win_pattern.insert(0, z)
        winning_game.append(win_pattern)

        win_pattern = [0, 0, 0]
        win_pattern.pop(1)
        win_pattern.insert(1, z)
        winning_game.append(win_pattern)

        win_pattern = [0, 0, 0]
        win_pattern.pop(2)
        win_pattern.insert(2, z)
        winning_game.append(win_pattern)

        identities.append(winning_game)

        winning_game = []
        win_pattern = [0, 0, 0]
        win_pattern.pop(2)
        win_pattern.insert(2, z)
        winning_game.append(win_pattern)

        win_pattern = [0, 0, 0]
        win_pattern.pop(1)
        win_pattern.insert(1, z)
        winning_game.append(win_pattern)

        win_pattern = [0, 0, 0]
        win_pattern.pop(0)
        win_pattern.insert(0, z)
        winning_game.append(win_pattern)

        identities.append(winning_game)

    return identities


def declare_winner(board):
    for game in generate_horizontal_win():
        for x in range(0, 3):
            if game[x] == board[x]:
                print(print('win horizontal for player {}. '.format(board[0][0])))

    for game in generate_vertical_win():
        for x in range(0, 3):
            if game[0][x] == board[0][x] and game[1][x] == board[1][x] and game[2][x] == board[2][x]:
                print('win vertical for player {}. '.format(board[0][0]))

    for game in generate_cross_win():
        if (game[0][0] == board[0][0] and game[1][1] == board[1][1] and game[2][2] == board[2][2]) \
                or (game[0][2] == board[0][2] and game[1][1] == board[1][1] and game[2][0] == board[2][0]):
            print('win_cross for player {}. '.format(board[0][0]))

    return 'winner'


winner_board = [[1, 0, 2], [1, 1, 2], [0, 1, 2]]

declare_winner(winner_board)
