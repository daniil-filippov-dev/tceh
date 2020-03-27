# -*- coding: utf-8 -*-

# What are the differences?
s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
r = range(0, 21)

for i in s:
    print(i)

for i in r:
    print(i)


# What if we want to create a really big list for iteration?
import sys

print(0, sys.getsizeof([]))
print(1, sys.getsizeof([1]))
print(2, sys.getsizeof([1, 2]))
print(3, sys.getsizeof([1, 2, 3]))

x = list(range(0, 1000000))
print(len(x), sys.getsizeof(x))


# What is range() actually?
r = range(0, 10)
print(r, type(r))


# Can we measure range() size?
print('range(0, 10)', sys.getsizeof(range(0, 10)))
print('range(0, 100)', sys.getsizeof(range(0, 100)))
print('range(0, 1000000)', sys.getsizeof(range(0, 1000000)))
