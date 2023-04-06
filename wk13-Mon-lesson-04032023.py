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


print("\nBlank line intentionally\n")
print("Redefine the var3 list with new elements below.")
var3 = [721, 649, '009', 493, 386, 251]
print(f"{var3}")
print(f"The element at index 1 in the var3 list has a number {var3[1]}")
print(f"There are {len(var3)} elements in the var3 list")
for i in range(len(var3)):
    print(var3[i])

# list comprehension
print("\n###########\nList Comprehension\n")
import random
print("This is 5 x 5 matrix:")
list_of_lists = [[random.randint(0,10) for j in range(5)] for i in range(5)]
print(list_of_lists)
print("This is 3 x 5 matrix:")
list_of_lists = [[random.randint(0,10) for j in range(5)] for i in range(3)]
print(list_of_lists)

# using for loop with list_of_lists
print("\nLet's use for loop with the list of lists")
for l in list_of_lists:
    print(l) # print each row
    for element in l:
        print(element) # print individual elements per each row

print("\nLet's express the above statements using for loop\n")
for i in range(len(list_of_lists)):
    print(list_of_lists[i])
    for j in range(len(list_of_lists[i])):
        print(list_of_lists[i][j])

# Dictionary examples
print("\n##############\nLet's review on Dictionary data types!\n")

var={}
print(var)
print(type(var))

print("Let's define var2 dictionary")
var2 = {"number": 386}
print(var2)
print("let's add a new key-value pair in the dictionary")
var2["fruit"] = "apple"
print(var2)
print("let's update a value associated with a key value")
var2["number"] = 493 
print(var2)
print(dir(var2))



