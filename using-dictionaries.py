# 1) Set the emails variable to be an empty dictionary
assert emails == {}, f"Expected `emails` to be {{}} but got: {repr(emails)}"

# 2) Add 'ashley', 'craig', and 'elizabeth' to the emails dictionary without reassigni
ng the variable.

assert emails == {
    "ashley": "ashley@example.com",
    "craig": "craig@example.com",
    "elizabeth": "elizabeth@example.com",
}, f"Expected `emails` to be {{'ashley': 'ashley@example.com', 'craig': 'craig@example
.com', 'elizabeth': 'elizabeth@example.com'}} but got: {repr(emails)}"

# 3) Remove 'craig' from the emails dictionary without reassigning the variable.

assert emails == {
    "ashley": "ashley@example.com",
    "elizabeth": "elizabeth@example.com",}, f"Expected `emails` to be {{'ashley': 'ashley@example.com', 'elizabeth': 'elizabeth
@example.com'}} but got: {repr(emails)}"

# 4) Add 'dalton' to the emails dictionary without reassigning the variable.

assert emails == {
    "ashley": "ashley@example.com",
    "elizabeth": "elizabeth@example.com",
    "dalton": "dalton@example.com",
}, f"Expected `emails` to be {{'ashley': 'ashley@example.com', 'elizabeth': 'elizabeth
@example.com', 'dalton': 'dalton@example.com'}} but got: {repr(emails)}"

# 5) Return a list of keys from the emails dictionary as `users`

assert users == [
    "ashley",
    "elizabeth",
    "dalton",
], f"Expected `users` to be ['ashley', 'elizabeth', 'dalton'] but got: {repr(users)}"

# 6) Return a list of values from the emails dictionary as `email_list`

assert email_list == [
    "ashley@example.com",
    "elizabeth@example.com",
    "dalton@example.com",
], f"Expected `email_list` to be ['ashely@example.com', 'elizabeth@example.com', 'dalt
on@example.com'] but got: {repr(email_list)}"