# Date: 04/06/2023
# Title: Define the `char_range` generator
def char_range(start, stop, step=1):
    initial_code = ord(start) # convert to int
    last_code = ord(stop)     # convert to int

    stop_modifier = 1

    # For Error #3 dealing with reversed unicode: multiply by -1 for step value
    if initial_code > last_code:
        step *= -1
        stop_modifier *= -1


    for number in range(initial_code, last_code + stop_modifier, step):
        yield chr(number) # convert int to chr
    # yield start

'''
Error Message #1
Traceback (most recent call last): create for loop
    assert list(char_range("a", "e")) == [
AssertionError: Expected ['a', 'b', 'c', 'd', 'e'] but got ['e']
'''
'''
Error Message #2: last code is not included: add 1 for last_code
    assert list(char_range("a", "e")) == [
AssertionError: Expected ['a', 'b', 'c', 'd', 'e'] but got ['a', 'b', 'c', 'd']
'''

'''
Error Message #3: deal with reversed code : let's multiply by -1
    assert list(char_range("e", "a")) == [
AssertionError: Expected ['e', 'd', 'c', 'b', 'a'] but got []
'''

'''
Error Message #4: multiply by -1 for stop modifier and step for reversed unicode, accordingly.
    assert list(char_range("e", "a")) == [
AssertionError: Expected ['e', 'd', 'c', 'b', 'a'] but got ['e', 'd', 'c']
'''

'''
No errors detected.
'''
# Tests to verify the implementation of char_range
# *Do not modify
##################################################

# Ensure that `char_range` is a generator function
from inspect import isgeneratorfunction

assert isgeneratorfunction(
    char_range
), f"Expected char_range to be a generator function but was not."

# Ensure that the result *does* includes the stop character
assert list(char_range("a", "e")) == [
    "a",
    "b",
    "c",
    "d",
    "e",
], f"Expected ['a', 'b', 'c', 'd', 'e'] but got {repr(list(char_range('a', 'e')))}"

# Iterate backwards if the start code point is higher than the stop code point

assert list(char_range("e", "a")) == [
    "e",
    "d",
    "c",
    "b",
    "a",
], f"Expected ['e', 'd', 'c', 'b', 'a'] but got {repr(list(char_range('e', 'a')))}"

# Properly step if a step value is provided

assert list(char_range("a", "e", 2)) == [
    "a",
    "c",
    "e",
], f"Expected ['a', 'c', 'e'] but got {repr(list(char_range('a', 'e', 2)))}"

# Step properly if the start code point is higher than the stop code point

assert list(char_range("e", "a", 2)) == [
    "e",
    "c",
    "a",
], f"Expected ['e', 'c', 'a'] but got {repr(list(char_range('e', 'a', 2)))}"