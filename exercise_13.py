"""
Exercise 13 (and Solution)
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in
the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""

number_to_generate = int(input("Fibonacci numbers to generate: "))
fibonacci_list = [0, 1]
for x in range(0, number_to_generate):
    fibonacci_list.append(fibonacci_list[x]+fibonacci_list[x+1])
print(fibonacci_list)
