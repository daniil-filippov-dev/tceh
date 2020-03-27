# -*- coding: utf-8 -*-

class CustomRange(object):
    def __init__(self, to, from_=0, step=1):
        self.to = to
        self.from_ = from_
        self.step = step

        print(self.to, self.from_)

    def __iter__(self):
        return self

    def __next__(self):
        if self.from_ < self.to:
            i = self.from_
            self.from_ += self.step
            return i
        else:
            raise StopIteration()

r = CustomRange(10)
print(list(r))

my_range = CustomRange(10, from_=1, step=2)
for i in my_range:
    print(i)

 