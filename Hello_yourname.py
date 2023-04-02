# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
# Output:
# Hello firstname lastname! You just delved into python.
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

# Sample Input 0
#
# Ross
# Taylor
#
# Sample Output 0
#
# Hello Ross Taylor! You just delved into python.
#
# Use a format function to pass first and last string value to each placeholder {} 

def print_full_name(first, last):
    # Write your code here
    return ("Hello {} {}! You just delved into python.".format(first, last))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print(print_full_name(first_name, last_name))