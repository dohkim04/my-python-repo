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


