#!/usr/bin/env python3.7

# Python implementation.
#1. receive a message.
message = input("Enter a message: ")
#2. make all lowercase. 
print("Lowercase:", message.lower())
#3. make all uppercase.
print("Uppercase:", message.upper())

# Revo@UwordI:~/environment/my-python-repo (dkim-04012023-v3) $ chmod u+x variations.py 
# Revo@UwordI:~/environment/my-python-repo (dkim-04012023-v3) $ ./variations.py 
# Enter a message: sdggs
# Revo@UwordI:~/environment/my-python-repo (dkim-04012023-v3) $ ./variations.py 
# Enter a message: This is a testing message.
# Lowercase: this is a testing message.
# Uppercase: THIS IS A TESTING MESSAGE.
# ================================================

#4. make title case.
print("Title case:", message.title())
#5. capitalize all chracters.
print("Capitalized:", message.capitalize())

# Execute this Python file and see the results below:
# Revo@UwordI:~/environment/my-python-repo (dkim-04012023-v3) $ \
# > ./variations.py 
# Enter a message: This is a testing message.
# Title case: This Is A Testing Message.
# Traceback (most recent call last):
#   File "./variations.py", line 25, in <module>
#     print("Capitalized:", message.capitalized())
# AttributeError: 'str' object has no attribute 'capitalized'

# Used a wrong expression: capitalize() is correct. ==> execute the Python file again and see the output below:

# Revo@UwordI:~/environment/my-python-repo (dkim-04012023-v3) $ ./variations.py 
# Capitalized: This is a testing message.
#===============================================================================

#6. get a list of each word.
each_word_list = message.split()
print("Words:", each_word_list)

# Revo@UwordI:~/environment/my-python-repo (dkim-04022023-v1) $ ./variations.py 
# Enter a message: This is a testing Message                                                                    
# ['This', 'is', 'a', 'testing', 'Message']

#===============================================================================
#7. get the first and last word from a given string ==> sorted each word in alphabetical order first!

# Traceback (most recent call last):
#   File "./variations.py", line 67, in <module>
#     sorted_each_word_list = each_word_list.sorted()
# AttributeError: 'list' object has no attribute 'sorted'

# Used a wrong syntax. =>  Corrected the method expression below. 
sorted_each_word_list = sorted(each_word_list)

# print the first word from the sorted_each_word_list
print("Alphabetic First Word:", sorted_each_word_list[0])
# print the lsat word from the sorted_each_word_list
print("Alphabetic First Word:", sorted_each_word_list[len(sorted_each_word_list)-1])

#Revo@UwordI:~/environment/my-python-repo (dkim-04022023-v1) $ ./variations.py 
#Enter a message: ThIs iS a tEsTinG mEssAGe
#Lowercase: this is a testing message
#Uppercase: THIS IS A TESTING MESSAGE
#Title case: This Is A Testing Message
#Capitalized: This is a testing message
#Words: ['ThIs', 'iS', 'a', 'tEsTinG', 'mEssAGe']
#Alphabetic First Word: ThIs
#Alphabetic First Word: tEsTinG