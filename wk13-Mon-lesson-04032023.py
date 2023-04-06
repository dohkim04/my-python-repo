# 13th week Python evening call review 
# date: 4/3/2023 (Monday)

# List data type example
var=[]
print(type(var)) 
var2 = [251, 386, 493]
print(var2)
# Output:
# <class 'list'>
# [251, 386, 493]

print("\nblank line intentionally\n")

# a list can contain different type of data type '009' is a string value below
print("a list data type can contain another type of data as element. '009' is a string value")
var3 = [251, 386, 493, '009']
print(var3)
var3.append(649) # append is an inplace function that directly update the vales of the var3 list.
print(var3)

# Output:
# [251, 386, 493, '009']
# [251, 386, 493, '009', 649]

print(dir(var3)) # show every function associated with the var3 list.
# Output:
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

numbers = [1,2,3,4,5]
print(numbers)
# Output:
# [1, 2, 3, 4, 5]

print("\nblank line intentionally\n")

# range data type
print("## Using range function to generate a list data type")
print(range(1, 101)) # print from 1 up to 100 (last number is not included)
r = range(1,101)
print(list(r)) # change the data type from range to list ==> typecasting

# Output:
# range(1, 101)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

print("\n## Another example using range to generate a list data type\n")

r=range(0,20)
print(r) # Output ==> range(0, 20)
print(list(r)) # Output ==> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# access each element by looping through a list 
numbers=[1,2,3,4,5]
for number in numbers: # number variable is an elemente of the numbers list.
    print(f"= Number is {number}") # access each single item by iterating through the numbers list
    print(f"= {number} multiply by 2 is", 2* number)
    print("==")

''' 
# Output:
= Number is 1
= 1 multiply by 2 is 2
==
= Number is 2
= 2 multiply by 2 is 4
==
= Number is 3
= 3 multiply by 2 is 6
==
= Number is 4
= 4 multiply by 2 is 8
==
= Number is 5
= 5 multiply by 2 is 10
==
'''

#  for loop with range
print("using for loop with a range")
for i in range(0,10):
    print(i)
'''
# Output:
using for loop with a range
0
1
2
3
4
5
6
7
8
9
'''

print("\nBlank line intentionally\n")
print("Redefine the var3 list with new elements below.")
var3 = [721, 649, '009', 493, 386, 251]
print(f"{var3}") 
# Output: [721, 649, '009', 493, 386, 251]

print(f"The element at index 1 in the var3 list has a number {var3[1]}")
# Output: The element at index 1 in the var3 list has a number 649

print(f"There are {len(var3)} elements in the var3 list")
for i in range(len(var3)):
    print(var3[i])

'''
# Output:
There are 6 elements in the var3 list
721
649
009
493
386
251
'''

# list comprehension
print("\n###########\nList Comprehension\n")
import random

print("This is 5 x 5 matrix:")
list_of_lists = [[random.randint(0,10) for j in range(5)] for i in range(5)]
print(list_of_lists)
# Output: [[2, 1, 8, 9, 6], [6, 9, 0, 10, 8], [9, 1, 10, 2, 7], [6, 8, 1, 6, 9], [5, 7, 4, 6, 5]]

print("This is 3 x 5 matrix:")
list_of_lists = [[random.randint(0,10) for j in range(5)] for i in range(3)]
print(list_of_lists)
# Output: [[0, 4, 9, 5, 7], [8, 4, 1, 0, 8], [9, 8, 7, 3, 4]]


# using list_of_lists with for loop
print("\nLet's use for loop with the list of lists")
for l in list_of_lists:
    print(l) # print each row
    for element in l:
        print(element) # print individual elements per each row
'''
Output:
[0, 4, 9, 5, 7]
0
4
9
5
7
[8, 4, 1, 0, 8]
8
4
1
0
8
[9, 8, 7, 3, 4]
9
8
7
3
4
'''

print("\nLet's express the above statements using for loop\n")
for i in range(len(list_of_lists)):
    print(list_of_lists[i])
    for j in range(len(list_of_lists[i])):
        print(list_of_lists[i][j])

'''
Output:
[0, 4, 9, 5, 7]
0
4
9
5
7
[8, 4, 1, 0, 8]
8
4
1
0
8
[9, 8, 7, 3, 4]
9
8
7
3
4
'''

# Dictionary examples
print("\n##############\nLet's review on Dictionary data types!\n")


var={}      
print(var)       # Output: {}
print(type(var)) # Output: <class 'dict'>

print("Let's define var2 dictionary")
var2 = {"number": 386} 
print(var2) # Output: {'number': 386}

print("let's add a new key-value pair in the dictionary")
var2["fruit"] = "apple"
print(var2) # Output: {'number': 386, 'fruit': 'apple'}

print("let's update a value associated with a key value")
var2["number"] = 493 
print(var2)      # Output: {'number': 493, 'fruit': 'apple'}
print(dir(var2)) # Output: ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

print("########")
print("Look at the keys only :")
print(var2.keys())   # Output: dict_keys(['number', 'fruit'])
print("Look at the values only :")
print(var2.values()) # Output: dict_values([493, 'apple'])

print("Let's iterate through the var2 dictionary:")
print("This is very important!!!!!")
for k,v in var2.items():
    print(k,v) # use tuple data type!!
'''
Output: 
number 493
fruit apple
'''

print("Let's clear the var2 dictionary")
var2.clear() 
# clear is an inplace function 
# because it directly change the content of the var2 dictionary
print(var2) # Output: {}


####
print("using random")
import random
dict_of_lists = {i:[random.randint(0,10) for j in range(5)] for i in range(3)}
# i integer number as a key and a list as a value per each row
# There are a total of 3 rows and each row is a list that contains 5 numbers.
for k, v in dict_of_lists.items(): 
    print(k,v) # key will be printed
    for element in v:
        print(element) # the value associated with the key will be printed

'''
Output: 
0 [5, 7, 6, 0, 9]
5
7
6
0
9
1 [6, 5, 8, 8, 2]
6
5
8
8
2
2 [6, 3, 2, 0, 9]
6
3
2
0
9
'''