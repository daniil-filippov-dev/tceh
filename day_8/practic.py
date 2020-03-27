# -*- coding: utf-8 -*-

# генератор, возвращающий новое случайное значаение
import random 

def rand_num():
    while True:
        yield random.random()

r = rand_num()
for i in range(5):
    print(i, next(r))



# генератор range()
def castom_range(stop, start=0, step=1):
    i = start 
    while i< stop:
        yield i
        i += step

a = castom_range(10)
while True:
    try:
        print(next(a))
    except:
        break

# генератор map()
def my_map(func, my_list):
    for i in my_list:
        yield func(i)

my_list_1 = [3, 4, 5]
test_map = my_map(float, my_list_1)
while True:
    try:
        print(next(test_map))
    except StopIteration:
        break

#генератор  enumerate()
def my_enumerate(my_list):
    i=0
    while i != len(my_list):
        yield (i, my_list[i])
        i += 1

# генератор  zip()
def my_zip(l_1, l_2):
    for i in range(len(l_1)):
        yield (l_1[i], l_2[i])

zip_zap = my_zip((1,2,3,4),(2,3,4,5))
while True:
    try:
        print(next(zip_zap))
    except StopIteration:
        break

