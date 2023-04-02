#!/usr/bin/env python3.7

# Python implementation
#1. receive a message
message = input("Enter a message: ")

#2. make all lowercase 
print("Lowercase:", message.lower())

#3. make all uppercase
print("Uppercase:", message.upper())

# Revo@UwordI:~/environment/my-python-repo (dkim-04012023-v3) $ chmod u+x variations.py 
# Revo@UwordI:~/environment/my-python-repo (dkim-04012023-v3) $ ./variations.py 
# Enter a message: sdggs
# Revo@UwordI:~/environment/my-python-repo (dkim-04012023-v3) $ ./variations.py 
# Enter a message: This is a testing message.
# Lowercase: this is a testing message.
# Uppercase: THIS IS A TESTING MESSAGE.

#4. title case
print("Title case:", message.title())

#5. capitalize
print("Capitalized:", message.capitalize())

# Execute this python file and see the results below:
# Revo@UwordI:~/environment/my-python-repo (dkim-04012023-v3) $ \
# > ./variations.py 
# Enter a message: This is a testing message.
# Lowercase: this is a testing message.
# Uppercase: THIS IS A TESTING MESSAGE.
# Title case: This Is A Testing Message.
# Traceback (most recent call last):
#   File "./variations.py", line 25, in <module>
#     print("Capitalized:", message.capitalized())
# AttributeError: 'str' object has no attribute 'capitalized'

