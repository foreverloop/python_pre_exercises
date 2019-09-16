"""
Exercise 6 (and Solution)
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""

user_word = input("Enter a word: ")

if user_word == user_word[::-1]:
    print('this word is a palindrome')
else:
    print('this word is not a palindrome')
