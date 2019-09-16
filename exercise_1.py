name = input("Give me your name: ")
print("Your name is " + name)

age = int(input("Enter your age: "))
year = (2019 - age) + 100
out_message = "Hello {}, you're {} now so you should be 100 in the year {}".format(name, age, year)
print(out_message)
