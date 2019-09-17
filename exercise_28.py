"""
Exercise 28 (and Solution)
Implement a function that takes as input three variables, and returns the largest of the three.
Do this without using the Python max() function!

The goal of this exercise is to think about some internals that Python normally takes care of for us.
All you need is some variables and if statements!
"""


def alt_greatest(one, two, three):
    numbers = [one, two, three]
    sort = sorted(numbers, reverse=True)
    return sort[0]


print("The largest number is {}. ".format(alt_greatest(10, 9, 6)))
