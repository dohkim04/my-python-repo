# Date: 04/06/2023
# Let's look at the scope of variable x
# if and while conditionals does not create their inner scope
if 1 < 2:
    x = 5 

while x < 6:
    print(x)
    x += 1

print(x)

#####
print("\n") # have a new line 

print("Outer scope for x:", x)
y=5 # define y variable and set to an integer number 5.
print("Outer scope for y:", y)


def set_x(y): # define set_x function
    print("Inner scope for y within set_x function:", y)
    x=y
    y=x

set_x(10) # call the function above

print("Outer scope for x after set_x function:",x)
print("Outer scope for y after set_x function:",y)
