# -*- coding: utf-8 -*-


def logger(function):
    def inner(x, y):
        result = function(x, y)
        print('Result is', result)
        return result
    return inner


def sum(x, y):
    return x + y


def mult(x, y):
    return x * y


s = logger(sum)
s_result = s(9, 12)
print(s_result)

m = logger(mult)
m(2, 5)

print(s, m)
