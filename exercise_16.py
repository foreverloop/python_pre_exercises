"""
Exercise 16 (and Solution)
Write a password generator in Python.
Be creative with how you generate passwords
- strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your run-time code in a main method.

Extra:
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

my Solution:
using ascii character 33 to 127, generate a random 12 letter password
#then convert it to character using the chr() function
"""
import random
import time

start_time = time.time()

words_one = ['red', 'blue', 'green', 'pink', 'yellow', 'grey', 'cyan', 'magenta']
words_two = ['cow', 'chicken', 'pig', 'sheep', 'dog', 'turkey', 'cat', 'rabbit']

password_strength = input('Type \'strong\' for a strong password, or \'weak\' for a weak password: ')

if password_strength == 'strong':
    password = [random.randint(33, 127) for _ in range(0, 13)]
    password = ''.join(chr(i) for i in password)
else:
    password = words_one[random.randint(0, 7)] + words_two[random.randint(0, 7)]

print(password)
print("--- %s seconds ---" % (time.time() - start_time))
