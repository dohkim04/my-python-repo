#!/usr/bin/env python3.7

# Date: 04/07/2023
# Title: practicing Python conditional statements using if-elif-else

# import all necessary libraries
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input("Enter your number: ").strip())

# If  is odd, print Weird
    if n % 2 == 1:
        print("Weird")
# If  is even,
    elif n % 2 == 0:
        if n in range(2,6): # and in the inclusive range of 2 to 5,
            print("Not Weird")
        elif n in range(6,21): # and in the inclusive of 6 to 20,
            print("Weird")
        else: # and great than 20,
            print("Not Weird")
            
            
'''
Output:

~/environment/my-python-repo (dkim-04072023-v1) $ ./py-if-elif-else.py 
Enter your number: 56
Not Weird
~/environment/my-python-repo (dkim-04072023-v1) $ ./py-if-elif-else.py 
Enter your number: 3
Weird
~/environment/my-python-repo (dkim-04072023-v1) $ ./py-if-elif-else.py 
Enter your number: 5
Weird
~/environment/my-python-repo (dkim-04072023-v1) $ ./py-if-elif-else.py 
Enter your number: 7
Weird
~/environment/my-python-repo (dkim-04072023-v1) $ ./py-if-elif-else.py 
Enter your number: 67
Weird
~/environment/my-python-repo (dkim-04072023-v1) $ ./py-if-elif-else.py 
Enter your number: 20
Weird
~/environment/my-python-repo (dkim-04072023-v1) $ ./py-if-elif-else.py 
Enter your number: 22
Not Weird
'''

