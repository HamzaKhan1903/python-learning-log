print("--- Block 1: id() and is/== basics ---")
x = 5
y = x
print(id(x))
print(id(y))
print(x == y)
print(x is y)

print("--- Block 2: small int caching ---")
a = 1000
b = 1000
print(id(a))
print(id(b))
print(a is b)

print("--- Block 3: proving separate objects (literal vs function result) ---")
c = 1000
d = int("1000")
print(id(c))
print(id(d))
print(c is d)

print("--- Block 4: mutability - lists ---")
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)
print(list2)
print(list1 is list2)
print(id(list1))
print(id(list2))


print("--- Block 5: mutability verification - lists ---")
list1 = [1,2,3]
list2 = [1,2,3]
list2.append(4)
print(list1)
print(list2)
print(list1 is list2)
print(id(list1))
print(id(list2))

print("--- Block 6: separate lists, separate objects ---")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
#list2.append(4)
print(list1)
print(list2)
print(list1 is list2)
print(list1 == list2)
print(id(list1))
print(id(list2))


print("--- Block 7: truncation vs rounding ---")
a = 3.9
b = int(a)
c = round(a)
print(b)
print(c)

'''
print("--- Block 8: conversion failure ---")
d = "hello"
e = int(d)
print(e)
'''

print("--- Block 8: arithmetic operators ---")
print(7 + 3)
print(7 - 3)
print(7 * 3)
print(7 / 3)
print(7 // 3)
print(7 % 3)
print(7 ** 3)


print("--- Block 9: comparison and logical operators ---")
print(5 > 3)
print(5 < 3)
print(5 >= 5)
print(5 != 3)
print(5 > 3 and 2 < 4)
print(5 > 3 or 10 < 4)
print(not (5 > 3))
