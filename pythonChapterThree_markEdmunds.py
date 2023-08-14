# Python Program One Data Types and if Statements
# "Largest of Three" Program
# Created by Mark Edmunds for CIT 95
# August 11, 2023.
#
# variables
# integers
num1 = 0
num2 = 0
num3 = 0
largest_number = 0
# double
division_result = 0.0

# strings
username = ""

# booleans
go_again = False

# output Types
print("\n username is of type: " + str(type(username)))
print("\n division_result is of type:" + str(type(division_result)))
print("\n num1 is of type: " + str(type(num1)))
print("\n num2 is of type: " + str(type(num2)))
print("\n num3 is of type: " + str(type(num3)))
print("\n go_again is of type: " + str(type(go_again)))


# validate user input


def divide_by_zero_check() -> str:
    if num2 != 0:
        return str("\n This result of division of number 1 by number 2 is: " + str(num1 / num2))
    else:
        return str("\n I'm not great with dvision but I don't think you can divide by zero!")


def validate_input(num: str) -> str:
    try:
        _ = int(num)
        return num
    except TypeError:
        return validate_input(input("\n Must be a numerical value try again: "))


# get user input
num1 = validate_input(input("\n please enter a whole (integer) number value for first number:"))
print("\n num1 = " + num1 + " and is of type: ", str(type(num1)))
num2 = validate_input(input("\n please enter a whole (integer) number value for second number:"))
print("\n num2 = " + num2 + " and is of type: ", str(type(num2)))
num3 = validate_input(input("\n please enter a whole (integer) number value for third number:"))
print("\n num3 = " + num3 + " and is of type: ", str(type(num3)))
# num1. num2. and num3 changed type when we used the input function to get their value from the user

# convert num1, num2, and num3 back to integers
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

# get and print username
username = input("\n please enter your name:")
print("\n Hello ", username)

# largest number nested if statements
if num1 > num2:
    if num1 > num3:
        largest_number = num1
    else:
        largest_number = num3
elif num2 > num3:
    largest_number = num2
else:
    largest_number = num3

print("\n The largest number (nested if solution) is: ", str(largest_number))

# Compound if statements
if num1 > num2 and num1 > num3:
    largest_number = num1
elif num2 > num3:
    largest_number = num2
else:
    largest_number = num3

print("\n The largest number (compound if solution) is: ", str(largest_number))


# ChatGPT solution
def find_largest(a, b, c):
    largest = max(a, b, c)
    return largest


largest_number = find_largest(num1, num2, num3)
print(f"\n The largest number (ChatGPT solution) is: {largest_number}")

# perform division calculation and display result
print(f"{divide_by_zero_check()}")
