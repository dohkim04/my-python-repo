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
    return "-".join(word_list) # join each word by a "-"

if __name__ == '__main__':
    line = input("Enter your string: ")
    result = split_and_join(line)
    print(result)
    