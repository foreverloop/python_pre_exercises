"""
Exercise 24 (and Solution)
This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.

Time for some fake graphics! Let’s say we want to draw game boards that look like this:
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
This one is 3x3 (like in tic tac toe).
Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw,
and draw it for them to the screen using Python’s print statement.
Remember that in Python 3, printing to the screen is accomplished by

print("Thing to show on screen")
Hint: this requires some use of functions,
as were discussed previously on this blog and elsewhere on the Internet,
like this TutorialsPoint link.
"""
import math

horizontal_bar = ' ---- '
vertical_bar = '|     '


def make_string(generate_number, horizontal):
    if horizontal:
        return horizontal_bar * generate_number
    else:
        return vertical_bar * (generate_number + 1)


def generate_grid(squares):
    required_bars = int(math.sqrt(squares))
    generated_horizontal_line = make_string(required_bars, True)
    generated_vertical_bar = make_string(required_bars, False)
    for i in range(0, required_bars):
        print(generated_horizontal_line)
        print(generated_vertical_bar)

    print(generated_horizontal_line)
    return 0


generate_grid(9)
