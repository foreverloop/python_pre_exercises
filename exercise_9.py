"""
Exercise 9 (and Solution)
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
import random

a = random.randint(0, 9)
games = []
while(True):
    try:
        player1 = input("Enter an integer between 0 and 9 (or type \'exit\' to exit): ")
        games.append(1)
        if player1 == 'exit':
            print('Game Has Ended')
            break
        else:
            player1 = int(player1)
            if player1 < a:
                print('your guess was too low,try higher')
            if player1 > a:
                print('your guess was too high, try lower')
            if player1 == a:
                print('your guess was correct')
                break
    except(KeyError):
        print('invalid input')
    finally:
        print('type \'exit\' to stop playing or')

print("you took {} guesses to finish the game".format(sum(games)))
