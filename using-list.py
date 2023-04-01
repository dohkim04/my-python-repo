"""
using-list.py
"""
# 1) Set the users variable to be an empty list

# assign an empty list to users list variable
users = []
assert users == [], f"Expected `users` to be [] but got: {repr(users)}"

# > python3.7 using-list.py 
# Traceback (most recent call last):
#  File "using-list.py", line 13, in <module>
#    assert users == ['kevin', 'bob', 'alice'], f"Expected `users` to be ['kevin', 'bob', 'alice'] but got: {repr(users)}"
# AssertionError: Expected `users` to be ['kevin', 'bob', 'alice'] but got: []

# 2) Add 'kevin', 'bob', and 'alice' to the users list in that order without reassigning the variable.
# Let's add all three new values into the users list.
users.append('kevin')
users.append('bob')
users.append('alice')

assert users == ['kevin', 'bob', 'alice'], f"Expected `users` to be ['kevin', 'bob', 'alice'] but got: {repr(users)}"

# > python3.7 using-list.py 
# Traceback (most recent call last):
#   File "using-list.py", line 27, in <module>
#     assert users == ['kevin', 'alice'], f"Expected `users` to be ['kevin', 'alice'] but got: {repr(users)}"
# AssertionError: Expected `users` to be ['kevin', 'alice'] but got: ['kevin', 'bob', 'alice']

# 3) Remove 'bob' from the users list without reassigning the variable.
del users[1]

assert users == ['kevin', 'alice'], f"Expected `users` to be ['kevin', 'alice'] but got: {repr(users)}"


# > python3.7 using-list.py 
# Traceback (most recent call last):
#  File "using-list.py", line 37, in <module>
#    assert rev_users == ['alice', 'kevin'], f"Expected `rev_users` to be ['alice', 'kevin'] but got: {repr(rev_users)}"
# NameError: name 'rev_users' is not defined

# 4) Reverse the users list and assign the result to `rev_users`
# created rev_users list using reversed function
rev_users = list(reversed(users))

assert rev_users == ['alice', 'kevin'], f"Expected `rev_users` to be ['alice', 'kevin'] but got: {repr(rev_users)}"

# 5) Add the user 'melody' to users where 'bob' used to be.

assert users == ['kevin', 'melody', 'alice'], f"Expected `users` to be ['kevin', 'melody', 'alice'] but got: {repr(users)}"

# 6) Add the users 'andy', 'wanda', and 'jim' to the users list using a single command

assert users == ['kevin', 'melody', 'alice', 'andy', 'wanda', 'jim'], f"Expected `users` to be ['kevin', 'melody', 'alice', 'andy', 'wanda', 'jim'] but got: {repr(users)}"

# 7) Slice the users lists to return the 3rd and 4th items and assign the result to `center_users`

assert center_users == ['alice', 'andy'], f"Expected `users` to be ['alice', 'andy'] but got: {repr(center_users)}"