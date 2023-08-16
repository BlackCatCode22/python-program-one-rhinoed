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
print("\n username is of type: ", str(type(username)))
print("\n division_result is of type:", str(type(division_result)))
print("\n num1 is of type: ", str(type(num1)))
print("\n num2 is of type: ", str(type(num2)))
print("\n num3 is of type: ", str(type(num3)))
print("\n go_again is of type: ", str(type(go_again)))


# validate user input


def divide_by_zero_check() -> bool:
    if num2 != 0:
        return True
    else:
        return False

# Check to see if the user input can be converted into an integer.
# Fixed error now works properly
def validate_input(num: str) -> str:
    try:
        _ = int(num)
        return num
    except ValueError:
        return validate_input(input("\n Must be a numerical value try again: "))


# get user input
num1 = validate_input(input("\n please enter a whole (integer) number value for first number:"))
print("\n num1 = ", num1, " and is of type: ", str(type(num1)))
num2 = validate_input(input("\n please enter a whole (integer) number value for second number:"))
print("\n num2 = ", num2, " and is of type: ", str(type(num2)))
num3 = validate_input(input("\n please enter a whole (integer) number value for third number:"))
print("\n num3 = ", num3, " and is of type: ", str(type(num3)))
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
# *** I don't have a num2 > num1 condition check in the else -if because
# at this point in the code  we already know from the first compound condition that num1 is not thee largest
# if the first compound condition failed because num1 was smaller than num3
# that would mean num1 is in the middle and if it failed because num2 > num1
# then the condition I have will determine the largest ***
if num1 >= num2 and num1 >= num3:
    largest_number = num1
elif num2 >= num3:
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
if divide_by_zero_check():
    division_result = num1/num2
    print("\n The results of the division is: ", division_result)
else:
    print("I may not be the best at division ")

