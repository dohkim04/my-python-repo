# Date: 04/06/2023 
# Title: Defining and Using Pythong Functions
# 1) Write a `split_name` function that takes a string and returns a dictionary with first_name and last_name
''' 1st Error message:

Traceback (most recent call last):
  File "/home/dohyungkim2023/my-python-repo/testing-functions.py", line 4, in <module>
    assert split_name("Kevin Bacon") == {
NameError: name 'split_name' is not defined
'''
# Solution to 1st Error Message:
def split_name(name):
    names = name.split() # split based on space
    first_name = names[0]
    last_name = names[len(names)-1]
    return {
        "first_name": first_name, 
        "last_name" : last_name,
    }


assert split_name("Kevin Bacon") == {
    "first_name": "Kevin",
    "last_name": "Bacon",
}, f"Expected {{'first_name': 'Kevin', 'last_name': 'Bacon'}} but received {split_name('Kevin Bacon')}"



# 2) Ensure that `split_name` can handle multi-word last names
''' 2nd Error Message: 

Traceback (most recent call last):
  File "/home/dohyungkim2023/my-python-repo/testing-functions.py", line 28, in <module>
    assert split_name("Victor Von Doom") == {
AssertionError: Expected {'first_name': 'Victor', 'last_name': 'Von Doom'} but received {'first_name': 'Victor', 'last_name': 'Doom'}
'''
# redefine split_name function
def split_name(name):
    first_name, last_name = name.split(maxsplit=1)
    # split a given string into 2 pieces based on the first space
    # then assign the first part to first_name
    # and the second part to last_name
    return  {"first_name": first_name,"last_name": last_name,}

assert split_name("Victor Von Doom") == {
    "first_name": "Victor",
    "last_name": "Von Doom",
}, f"Expected {{'first_name': 'Victor', 'last_name': 'Von Doom'}} but received {split_name('Victor Von Doom')}"


# 3) Write an `is_palindrome` function to check if a string is a palindrome (reads the same from left-to-right and right-to-left)
'''
3rd Error Message:

Traceback (most recent call last):
  File "/home/dohyungkim2023/my-python-repo/testing-functions.py", line 52, in <module>
    assert is_palindrome("radar") == True, f"Expected True but got {is_palindrome('radar')}"
NameError: name 'is_palindrome' is not defined
'''
# Solution to 3rd Error Message:
def is_palindrome(input_string):
    reversed_string = input_string[::-1]
    if reversed_string == input_string:
        result = True
    else:
        result = False
    return result
    # the short verion of the above block of codes is: 
    # return input_string == input_string[::-1]

assert is_palindrome("radar") == True, f"Expected True but got {is_palindrome('radar')}"
assert is_palindrome("stop") == False, f"Expected False but got {is_palindrome('stop')}"

# 4) Make `is_palindrome` work with numbers
'''
4th Error Message:

Traceback (most recent call last):
  File "/home/dohyungkim2023/my-python-repo/testing-functions.py", line 73, in <module>
    assert is_palindrome(101) == True, f"Expected True but got {is_palindrome(101)}"
  File "/home/dohyungkim2023/my-python-repo/testing-functions.py", line 61, in is_palindrome
    reversed_string = input_string[::-1]
TypeError: 'int' object is not subscriptable
'''
# Solution to 4th Error Message:
def is_palindrome(input_number):
    input_string = str(input_number) # typecast integer value to string value 
    reversed_string = input_string[::-1]
    if reversed_string == input_string:
        result = True
    else:
        result = False
    return result

assert is_palindrome(101) == True, f"Expected True but got {is_palindrome(101)}"
assert is_palindrome(10) == False, f"Expected False but got {is_palindrome(10)}"

# 5) Write a `build_list` function that takes an item and a number to include in a list
def build_list(string_value, number_default=1):
    create_list = []
    for _ in range(number_default):
        create_list.append(string_value)
    return create_list

assert build_list("Apple", 3) == [
    "Apple",
    "Apple",
    "Apple",
], f"Expected ['Apple', 'Apple', 'Apple'] but received {repr(build_list('Apple', 3))}"
assert build_list("Orange") == [
    "Orange"
], f"Expected ['Orange'] but received {repr(build_list('Orange'))}"

'''
Checked the error code shown below:   
~/my-python-repo$ echo $?
0
'''
