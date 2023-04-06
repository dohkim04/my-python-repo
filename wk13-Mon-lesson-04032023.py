# 13th week Python evening call review

var=[]
print(type(var)) 
var2 = [251, 386, 493]
print(var2)
# output
# ~/my-python-repo$ python3.10 wk13-Mon-lesson-04032023.py 
# <class 'list'>
# [251, 386, 493]
print("\nblank line intentionally\n")

var3 = [251, 386, 493, '009']
print(var3)
var3.append(649) 
# append is an inplace function: directly update the vales of the var3 list.
print(var3) 
print(dir(var3))

numbers = [1,2,3,4,5]
print(numbers)

print("\nblank line intentionally\n")
# range 
print(range(1, 101)) # print from 1 up to 100 (last number is not included)
r = range(1,101)
print(list(r))

print("\nblank line intentionally\n")