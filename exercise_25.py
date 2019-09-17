"""
Guessing Game Two
Exercise 25 (and Solution)
In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.

This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100.
The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses it took to get your number.

As the writer of this program, you will have to choose how your program will strategically guess.
A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number.
But that’s not an optimal guessing strategy.
An alternate strategy might be to guess 50 (right in the middle of the range),
and then increase / decrease by 1 as needed.
After you’ve written the program, try to find the optimal strategy!
(We’ll talk about what is the optimal one next week with the solution.)
"""
import random

MINIMUM = 0
MAXIMUM = 100
NUMBER = random.randint(MINIMUM, MAXIMUM)
TRY = 0
RUNNING = True
ANSWER = None

while RUNNING:
    ANSWER = input('is {} your number (yes or no): '.format(NUMBER))
    if "no" in ANSWER.lower() and "lower" in ANSWER.lower():
        NUMBER -= random.randint(1, 4)
    elif "no" in ANSWER.lower() and "higher" in ANSWER.lower():
        NUMBER += random.randint(1, 4)
    elif ANSWER.lower() == "no":
        ANSWER = input('Enter if your number was higher or lower: ')
        if ANSWER.lower() == "higher":
            NUMBER += random.randint(1, 4)
        elif ANSWER.lower() == "lower":
            NUMBER -= random.randint(1, 4)
    elif ANSWER.lower() == "yes":
        if TRY < 2:
            print("Yes! It only took me {} try!".format(str(TRY)))
        elif TRY < 2 and TRY < 10:
            print("Pretty well for a robot, {} tries.".format(TRY))
        else:
            print("That's so bad, {} tries.".format(str(TRY)))
        RUNNING = False
    TRY += 1

print("Thanks for the game!")
