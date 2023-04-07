#!/usr/bin/env python3.7

# Date: 04/07/2023
# Title: find a string

# the user enters a string and a substring. 
# print the number of times that the substring occurs in the given string. 
# String traversal will take place from left to right, not from right to left.

# NOTE: String letters are case-sensitive.


# Sample Input:
# ABCDCDC
# CDC

# Sample Output:
# 2 

def count_substring(string, sub_string):
    count = 0
    for i in range(0,len(string)-len(sub_string)+1):
        sliced_string = string[i:len(sub_string)+i]
        if sub_string == sliced_string:
            count += 1
    
    return count

if __name__ == '__main__':
    string = input("Enter your string: ").strip()
    sub_string = input("Enter your sub string: ").strip()
    
    count = count_substring(string, sub_string)
    print(count)

"""
~/environment/my-python-repo (dkim-04072023-v1) $ ./find_string.py 
Enter your string: ABCDCDC
Enter your sub string: CDC
2
~/environment/my-python-repo (dkim-04072023-v1) $ 
"""
