# Date: 04/06/2023
# Title: Define the `char_range` generator
def char_range(start, stop, step=1):
    initial_code = ord(start) # convert to int
    last_code = ord(stop)     # convert to int
    for number in range(initial_code, last_code, step):
        yield chr(number) # convert int to chr
    # yield start

'''
Error Message #1
Traceback (most recent call last):
  File "/home/dohyungkim2023/my-python-repo/using-generator.py", line 18, in <module>
    assert list(char_range("a", "e")) == [
AssertionError: Expected ['a', 'b', 'c', 'd', 'e'] but got ['e']
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