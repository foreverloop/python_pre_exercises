"""
Exercise 2:
Ask the user for a number.
Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""
user_number = int(input("Enter a number: "))

if user_number % 2 == 0:
    if user_number % 4 == 0:
        print('this is a multiple of 4')
    else:
        print("this is an even number")
else:
    print("this is an odd number")

print('Provide two numbers: the 1st number will be divided by the second ')
check_number = int(input("Enter a number to be divided: "))
div_number = int(input("Enter a number to divide by: "))

if check_number % div_number == 0:
    print('these numbers divide evenly')
else:
    print('these numbers do NOT divide evenly')
