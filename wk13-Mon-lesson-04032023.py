# 13th week Python evening call review

# list data type example
var=[]
print(type(var)) 
var2 = [251, 386, 493]
print(var2)
# output
# ~/my-python-repo$ python3.10 wk13-Mon-lesson-04032023.py 
# <class 'list'>
# [251, 386, 493]
print("\nblank line intentionally\n")

# a list can contain different type of data type '009' is a string value below
print("a list data type can contain another type of data as element. '009' is a string value")
var3 = [251, 386, 493, '009']
print(var3)
var3.append(649) 
# append is an inplace function that directly update the vales of the var3 list.
print(var3) 
print(dir(var3)) # show every function associated with the var3 list.

numbers = [1,2,3,4,5]
print(numbers)

print("\nblank line intentionally\n")
# range data type
print("## Using range function to generate a list data type")
print(range(1, 101)) # print from 1 up to 100 (last number is not included)
r = range(1,101)
print(list(r)) # change the data type from range to list ==> typecasting
print("\n## Another example using range to generate a list data type\n")


r=range(0,20)
print(r)
print(list(r))

# access each element by looping through a list 
numbers=[1,2,3,4,5]
for number in numbers: # number variable is an elemente of the numbers list.
    print(f"= Number is {number}") # access each single item by iterating through the numbers list
    print(f"= {number} multiply by 2 is", 2* number)
    print("==")

#  for loop with range
print("using for loop with a range")
for i in range(0,10):
    print(i)



