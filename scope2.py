print("\n############") # have a separation line
print("Let's look at global scope.")

abc = 40
xxx = 100

print("Before calling set_x function,")
print(f"the outer scope abc: {abc}")
print(f"the outer scope xxx: {xxx}")
print("################")
def set_x(aaa):
    xxx = aaa # aaa is a parameter passing a value of 10 upon the function call below    
    print("This is the inner scope - within the function set_x.")
    print(f"the argument of the parameter aaa is {aaa}.")
    print("The value is now passed onto xxx variable:", xxx)    
    # simply pass the value of global abc value to new local value within this function
    xxx = abc # we can omit the keyword 'global' as it is implicitly defined as global value.

    # abc = abc + 30 # However, we cannot update the value of the abc variable here.
    # UnboundLocalError: local variable 'abc' referenced before assignment

    print (f"the inner scope for abc variable: {abc}")
    print ("The value of abc variable is now passed onto variable xxx.")
    print ("Inner scope for updated xxx:", xxx)

set_x(10) # pass 10 to set_x function above

print("#################")
print("After completing set_x function call,")
# print ("Outer scope for xxx:", xxx) ==> NameError: name 'xxx' is not defined
print (f"Outer scope for new global abc: {abc}")
print (f"Outer scope for updated xxx: {xxx}")
print ("Conclusion: the value of global variables are still accessible in outer scope.")