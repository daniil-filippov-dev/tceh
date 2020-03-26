# -*- coding: utf-8 -*-


# You can get type of an instance


inst_type = type(14)
print(inst_type)
print("But what is inst_type's type?", type(inst_type))


# You can get class from instances

class Test(object):
    pass

t = Test()

print(t.__class__)


# Simple example

print('instances are objects', isinstance(t, object))
print('classes are objects two!', isinstance(Test, object))

Test.some_value = 12

print(t.some_value)


# Difference between class attributes and instance attributes

class DemoClass(object):
    class_value = 'i belong to the CLASS'

    def __init__(self, inst_value):
        self.inst_value = inst_value


d = DemoClass('abc')
d1 = DemoClass('zzz')

d1.inst_value = 'xxx'
d1.class_value = 'yyy'
print(d.inst_value, d1.inst_value)
print(d.class_value, d1.class_value)

DemoClass.class_value = 'i am shared between all instances!'
print(d.class_value, d1.class_value)
