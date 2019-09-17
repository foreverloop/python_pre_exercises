"""
Exercise 20 (and Solution)
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest)
and another number. The function decides whether or not the given number is inside the list and returns (then prints)
an appropriate boolean.

Extras:
Use binary search.
"""


def find_sorted(ordered_list, guess_number):
    return guess_number in ordered_list


a = range(1, 11)
print(find_sorted(a, 10))

#extra
def bin_search(ordered_list,left,right,guess_number):
    while left <= right:
        centre = int(left + (right - 1)/2)
        if ordered_list[centre] == guess_number:
            return centre
        elif ordered_list[centre] < guess_number:
            left = centre + 1
        else:
            right = centre - 1
    return -1

