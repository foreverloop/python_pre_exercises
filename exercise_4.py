"""
Exercise 4 and solution:
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

user_number = int(input("Enter a number: "))

#multiple line
divisors = []
for x in range(1, user_number+1):
    if user_number % x == 0:
        divisors.append(x)

#as a single line
o_div = [x for x in range(1, user_number+1) if user_number % x == 0]

print("Divisors of {} :".format(user_number), divisors)
print("Divisors of {} :".format(user_number), o_div)
