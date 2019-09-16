"""
Exercise 8 (and Solution)
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""

#dictionary of dictionaries
game_dict = {'rock':{'paper':'loses','scissors':'wins','rock':'draws'},
'paper':{'scissors':'loses','rock':'wins','paper':'draws'},
'scissors':{'rock':'loses','paper':'wins','scissors':'draws'}}

while(True):
    try:
        player1 = input("Enter 'rock','paper', or 'scissors': ")
        if player1 == 'end':
            print('Game Has Ended')
            break
        player2 = input("Enter 'rock','paper', or 'scissors': ")
        print("Player 1 {}".format(game_dict[player1][player2]))
    except(KeyError):
        print('invalid input')
    finally:
        print('type \'end\' to stop playing or')