#!/usr/bin/env python3.7
# Python String Split and Join
'''
Example:
>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']
Joining a string is simple:
>>> a = "-".join(a)
>>> print a
this-is-a-string 
'''
def split_and_join(line):
    # write your code here
    word_list = line.split(" ")  # split each word by a space, " "
    print("Word list:", word_list)
    return "-".join(word_list) # join each word by a "-" to create a new string and return it.
    # Previous wrong statements below:
    # word_list = line.split(" ").join("-")
    # Error message:
    # AttributeError: 'list' object has no attribute 'join'
    
if __name__ == '__main__':
    line = input("Enter your string: ")
    result = split_and_join(line)
    print("Split and join statement:", result)
    
# Revo@UwordI:~/environment/my-python-repo (dkim-04022023-python-string-split-and-join) $ ./split\&join.py 
# Enter your string: I am going to test this split and join function.
# Word list: ['I', 'am', 'going', 'to', 'test', 'this', 'split', 'and', 'join', 'function.']
# 
# Split and join statement: I-am-going-ot-test-this-split-and-join-function.

# Comments: made a mistake in deleteing this file from main branch in local repository.
# had to commit the delete status on the local repository and git push to the main branch on the remote GitHub repository.
# now I'm creating this pythong file gain on a branch in my local repository and will push it to remote GitHub repository again.

#============================================================
# changed the python file name as split&join_again.py

# Revo@UwordI:~/environment/my-python-repo (dkim-04022023-split&join-function-rewrite) $ ./split\&join_again.py 
#Enter your string: This is a testing message
#Word list: ['This', 'is', 'a', 'testing', 'message']
# Split and join statement: This-is-a-testing-message
