#!/usr/bin/env python3.7
# accept an integer input from a user
user_input = input("Enter an integer number: ")

# create a range from 1 to the user's provided number
# and loop through it
for number in range(1, user_input+1): # the last number is not included in range, Thus need to plus 1
    print(number)
    
# print FizzBuzz if the value is a multiple of 3 and 5
elif number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
# print Fizz if the value is a multiple of 3
elif number % 3 == 0:
    print("Fizz")
# print Buzz if the value is a multiple of 5
elif number % 5 == 0:
    print("Buzz")
# print the number as it is if nothing above applies.
else:
    print(number)
