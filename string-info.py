#!/usr/bin/env python3.7

message = input("Enter a message: ")

# print the first and the last character
print("Fist character:", message[0])
print("Last character:", message[-1])

# print the middle character.
# for a stinrg that has even-number characters, 
# grab what is just past the actual center point
# for "bac", 
# int((len('bac')/2) => int (1.5) => 1 => "bac"[1] => a
# for "bacd",  
# int(len('bacd')/2) => int(2.0) => 2 => "bacd"[2] => c
# for bacde",
# int(len('bacde")/2) => int(2.5) => 2 => "bacde"[2] => c
#  cast into integer to drop off remaining decimal number.

print("Middle character:", message[int(len(message) / 2)])

# even-index characters
print("Even index characters:", message[0::2])

# odd-index characters
print("Odd index characters:", message[1::2])

# reverse a string
print("Reversed message:", message[::-1])

#extra practice using negative index and negative steps
print("Slicing:", message[:int(-len(message)-1):-3]) 
# outcome: esMX
#  T   e   x  t [ ]  M  e  s  s  a  g  e
#-12 -11 -10 -9  -8 -7 -6 -5 -4 -3 -2 -1
# first index is -1 in slicing function: 'e'
# next index is  -4: 's'
# next index is  -7: 'M'
# next index is -11: "x"
# leng(message) is -12 
# so, int(-len(message)-1) is -13, that is String index out of the range
# still no error occured
# Revo@UwordI:~/environment/my-python-repo (dkim-03312023) $ echo $?
# 0 => no error occurred

print("Slicing before reaching index at -12:", message[:int(-len(message)):-3])

# check whether index -14 is considered as out of the range.
print("Slicing before reaching index at -14:", message[:int(-len(message)-2):-3])

# set up last negative index out of the range and check again
print("Slicing with -1 negative step", message[:int(-len(message)-2):-1])


'''
Enter a message: Text Message
Fist character: T
Last character: e
Middle character: e
Even index characters: Tx esg
Odd index characters: etMsae
Reversed message: egasseM txeT
Slicing: esMx
Slicing before reaching index at -12: esMx # No error!
Slicing before reaching index at -14: esMx # No error!
'''


