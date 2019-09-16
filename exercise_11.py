"""
Exercise 11 (and Solution)
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.
"""
def get_number(question="enter an integer greater than 2:"):
    n = 0
    while n < 3: n = int(input(question))
    return n

def get_divisors(n):
    x = list(range(2,n))
    divisors = [i for i in x if n % i == 0]
    return divisors

n = get_number()
divisors = get_divisors(n)
if divisors == []:
    print("{} is a prime number".format(n))
else:
    print("{} is not a prime number, it's divisors are {}".format(n,divisors))