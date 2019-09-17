"""
Exercise 12 (and Solution)
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""
a = [5, 10, 15, 20, 25]
print([x for x in a if a.index(x) == (len(a) - 1) or a.index(x) == 0])
