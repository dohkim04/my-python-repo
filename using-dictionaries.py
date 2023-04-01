
# Revo@UwordI:~/environment/my-python-repo (dkim-04012023-v2) $ python3.7 using-dictionaries.py 
# Traceback (most recent call last):
#   File "using-dictionaries.py", line 2, in <module>
#     assert emails == {}, f"Expected `emails` to be {{}} but got: {repr(emails)}"
# NameError: name 'emails' is not defined

# 1) Set the emails variable to be an empty dictionary
# assign an empty dictionary to emails variable below
emails = {}

assert emails == {}, f"Expected `emails` to be {{}} but got: {repr(emails)}"

# Revo@UwordI:~/environment/my-python-repo (dkim-04012023-v2) $ \
# > python3.7 using-dictionaries.py 
# Traceback (most recent call last):
#   File "using-dictionaries.py", line 20, in <module>
#     }, f"Expected `emails` to be {{'ashley': 'ashley@example.com', 'craig': 'craig@example.com', 'elizabeth': 'elizabeth@example.com'}} but got: {repr(emails)}"
# AssertionError: Expected `emails` to be {'ashley': 'ashley@example.com', 'craig': 'craig@example.com', 'elizabeth': 'elizabeth@example.com'} but got: {}

# 2) Add 'ashley', 'craig', and 'elizabeth' to the emails dictionary without reassigning the variable.
emails['ashley'] = 'ashley@example.com'
emails['craig'] = 'craig@example.com'
emails['elizabeth'] = 'elizabeth@example.com'


assert emails == {
    "ashley": "ashley@example.com",
    "craig": "craig@example.com",
    "elizabeth": "elizabeth@example.com",
}, f"Expected `emails` to be {{'ashley': 'ashley@example.com', 'craig': 'craig@example.com', 'elizabeth': 'elizabeth@example.com'}} but got: {repr(emails)}"

# 3) Remove 'craig' from the emails dictionary without reassigning the variable.
del emails['craig']

assert emails == {
    "ashley": "ashley@example.com",
    "elizabeth": "elizabeth@example.com",}, f"Expected `emails` to be {{'ashley': 'ashley@example.com', 'elizabeth': 'elizabeth@example.com'}} but got: {repr(emails)}"

# Revo@UwordI:~/environment/my-python-repo (dkim-04012023-v2) $ python3.7 using-dictionaries.py 
# Traceback (most recent call last):
#   File "using-dictionaries.py", line 46, in <module>
#     }, f"Expected `emails` to be {{'ashley': 'ashley@example.com', 'elizabeth': 'elizabeth@example.com', 'dalton': 'dalton@example.com'}} but got: {repr(emails)}"
# AssertionError: Expected `emails` to be {'ashley': 'ashley@example.com', 'elizabeth': 'elizabeth@example.com', 'dalton': 'dalton@example.com'} but got: {'ashley': 'ashley@example.com', 'elizabeth': 'elizabeth@example.com'}


# 4) Add 'dalton' to the emails dictionary without reassigning the variable.
emails['dalton'] = 'dalton@example.com'

assert emails == {
    "ashley": "ashley@example.com",
    "elizabeth": "elizabeth@example.com",
    "dalton": "dalton@example.com",
}, f"Expected `emails` to be {{'ashley': 'ashley@example.com', 'elizabeth': 'elizabeth@example.com', 'dalton': 'dalton@example.com'}} but got: {repr(emails)}"

# Revo@UwordI:~/environment/my-python-repo (dkim-04012023-v2) $ python3.7 using-dictionaries.py 
# Traceback (most recent call last):
#   File "using-dictionaries.py", line 58, in <module>
#     assert users == [
# NameError: name 'users' is not defined


# 5) Return a list of keys from the emails dictionary as `users`
users = list(emails.keys())

#Traceback (most recent call last):
#  File "using-dictionaries.py", line 70, in <module>
#    ], f"Expected `users` to be ['ashley', 'elizabeth', 'dalton'] but got: {repr(users)}"
#AssertionError: Expected `users` to be ['ashley', 'elizabeth', 'dalton'] but got: dict_keys(['ashley', 'elizabeth', 'dalton'])
# Solution: I have to convert dict_keys to a list type

assert users == [
    "ashley",
    "elizabeth",
    "dalton",
], f"Expected `users` to be ['ashley', 'elizabeth', 'dalton'] but got: {repr(users)}"


# Revo@UwordI:~/environment/my-python-repo (dkim-04012023-v2) $ python3.7 using-dictionaries.py 
# Traceback (most recent call last):
#   File "using-dictionaries.py", line 80, in <module>
#     assert email_list == [
# NameError: name 'email_list' is not defined

# 6) Return a list of values from the emails dictionary as `email_list`
email_list = list(emails.values())

#Traceback (most recent call last):
#  File "using-dictionaries.py", line 92, in <module>
#    ], f"Expected `email_list` to be ['ashely@example.com', 'elizabeth@example.com', 'dalton@example.com'] but got: {repr(email_list)}"
#AssertionError: Expected `email_list` to be ['ashely@example.com', 'elizabeth@example.com', 'dalton@example.com'] but got: dict_values(['ashley@example.com', 'elizabeth@example.com', 'dalton@example.com'])
# Solution: convert dict_values to a list type

assert email_list == [
    "ashley@example.com",
    "elizabeth@example.com",
    "dalton@example.com",
], f"Expected `email_list` to be ['ashely@example.com', 'elizabeth@example.com', 'dalton@example.com'] but got: {repr(email_list)}"

# Revo@UwordI:~/environment/my-python-repo (dkim-04012023-v2) $ python3.7 using-dictionaries.py 
# Revo@UwordI:~/environment/my-python-repo (dkim-04012023-v2) $ echo $?
# 0
# Revo@UwordI:~/environment/my-python-repo (dkim-04012023-v2) $ 


# Below is a missing task to be completed.
# 7) Return a list of tuples called `pairs` representing the key/value pairs in `emails`.

# upon executing this script, there was an error below.
# Revo@UwordI:~/environment/my-python-repo (dkim-0401-2023-v2-missing-task-added) $ \
#> python3.7 using-dictionaries.py 
#Traceback (most recent call last):
#  File "using-dictionaries.py", line 107, in <module>
#    assert pairs == [
# NameError: name 'pairs' is not defined


# Solution: define pairs dictionary
pairs = list(emails.items())

# Revo@UwordI:~/environment/my-python-repo (dkim-0401-2023-v2-missing-task-added) $ \
# > python3.7 using-dictionaries.py 
# Traceback (most recent call last):
#   File "using-dictionaries.py", line 119, in <module>
#     pairs = list(email.items())
# NameError: name 'email' is not defined
# Solution: correct a typo in the name: email --> emails
assert pairs == [
    ("ashley", "ashley@example.com"),
    ("elizabeth", "elizabeth@example.com"),
    ("dalton", "dalton@example.com"),], f"Expected `pairs` to be [('ashley', 'ashley@example.com'), ('elizabeth', 'elizabeth@example.com'), ('dalton', 'dalton@example.com')] but got: {repr(pairs)}"

# Revo@UwordI:~/environment/my-python-repo (dkim-0401-2023-v2-missing-task-added) $ \
# > python3.7 using-dictionaries.py 
# Revo@UwordI:~/environment/my-python-repo (dkim-0401-2023-v2-missing-task-added) $ \
# > echo $?
# 0
# Revo@UwordI:~/environment/my-python-repo (dkim-0401-2023-v2-missing-task-added) $ 
# All errors were corrected! 