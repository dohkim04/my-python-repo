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
print("\n#############") # have a separation line

print("Outer scope for x:", x)
y=5 # define y variable and set to an integer number 5.
print("Outer scope for y:", y)


def set_x(y): # define set_x function
    print("Inner scope for y before adding 3 within set_x function:", y)
    x=y+3 # this x is inner scope variable x, not outer scope variable. 
          # y is a parameter that receives an argument by the function call from outer scope
    print("Inner scope for x after adding 3 to y within set_x function:", x)
        # try to update the value of the y variable
    y=x # this y is inner scope variable y, not outer scope variable. 
    print("Inner scope for y after updating the value of y within set_x function:", y)

set_x(10) # call the function above

print("Outer scope for x after set_x function:",x)
print("Outer scope for y after set_x function:",y)

print("The variable defined within the function does not affect the variables in the outer scope.")

#####
print("\n############") # have a separation line
print("Let's look at global scope.")

abc = 40
print(f"the outer scope abc: {abc}")
print("################")
def set_x(aaa):
    xxx = aaa # aaa is a parameter passing a value of 10 upon the function call below    

    global abcd # explicitly define global abcd variable within this function
    abcd = xxx + 70 # add 30 to abc value and assign to abcd variable
    
    # simply pass the value of global abc value to new local value within this function

    global abc # this abc is the abc defined in outer scope (See the statement above: abc=40)
    abc = abc + 70 # the value of global abc variable is updated within this function, inner scope.

    # xxx = abc
    print ("Inner scope for new global abcd:", abcd)
    print ("Inner scope for updated abc:", abc)

set_x(10) # pass 10 to set_x function above

print("#################")
print("After completing set_x function call,")
# print ("Outer scope for xxx:", xxx) ==> NameError: name 'xxx' is not defined
print ("Outer scope for new global abcd:", abcd)
print ("Outer scope for updated abc:", abc)
print ("Conclusion: the value of global variables are still accessible in outer scope.")
