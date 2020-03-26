# -*- coding: utf-8 -*-

class Calc(object):
    def __init__(self, value):
        print('Calc constructor is called')
        self.value = value

    def count(self):
        return self.value * 8 + 9


c = Calc(1.4)
print(c.count())


class ExtendedCalc(Calc):
    def __init__(self, value, k=1):
        super().__init__(value)
        print('Extender', self.value)

        self.k = k

    def count(self):
        previous = super().count()

        return -1 * self.k * previous

e = ExtendedCalc(8, k=1.2)
print(e.count())

print(ExtendedCalc.__mro__)