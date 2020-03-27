# -*- coding: utf-8 -*-


l = [f for f in '123']
s = (c for c in '123')  # show in pythontutor

print(l == s)
print(type(l), type(s))
print(l, s)

for i in s:
    print(i)

for i in l:
    print(i)
