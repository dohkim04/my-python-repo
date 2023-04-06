#!/usr/bin/env python3.7
# accept an integer input from a user
user_input = int(input("Enter an integer number: "))

# create a range from 1 to the user's provided number
# and loop through it
for number in range(1, user_input+1): # the last number is not included in range, Thus need to plus 1
    if (number % 3 == 0) and (number % 5 == 0): 
        print("FizzBuzz")
# print Fizz if the value is a multiple of 3
    elif number % 3 == 0 and number % 5 !=0:
        print("Fizz")
# print Buzz if the value is a multiple of 5
    elif number % 3 != 0 and number % 5 == 0:
        print("Buzz")
# print the number as it is if nothing above applies.
    else:
        print(number)
    
# final revision: made this file executable in linux command prompt
    
'''
Checkpoint 1. Checking for looping through each number within the provided range - valid!.

Enter an integer number: 7
1
2
3
4
5
6
7

Checkpoint 2. Test whether this function is properly working or not.
Enter an integer number: 31
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
'''