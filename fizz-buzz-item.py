#!/usr/bin/env python3.7

# Date : 04/04/2023
# Title: Fizz-Buzz problem
"""
A typical Fizz-Buzz problem goes like this:

Write a program that prints the numbers from 1 - 100. 
For each multiple of three print "Fizz" instead of the number. 
For multiples of five print "Buzz" instead of the number. 
If a number is a multiple of three and five then print "FizzBuzz".

Solving this problem requires 2 key components: 
looping and conditionals. 
We're going to write a simplified program 
only using the conditional portion that will take 
any given number that we provide 
and print the Fizz-Buzz value. Here's how it will work:

$ ./fizz-buzz-item.py
Enter an integer value: 15
FizzBuzz
$ ./fizz-buzz-item.py
Enter an integer value: 21
Fizz
$ ./fizz-buzz-item.py
Enter an integer value: 17
17
"""
# Python coding implementation

# Get an integer input from a user
int_value = int(input("Enter an integer value: "))

# In case that the integer is evenly divisible by 3 and 5,
if int_value % 5 == 0 and int_value % 3 ==0:
    print("FizzBuzz")
elif int_value % 5 != 0 and int_value % 3 == 0:
    print("Fizz")
elif int_value % 5 ==0 and int_value % 3 != 0:
    print("Buzz")
else:
    print(int_value)



