# -*- coding: utf-8 -*-

class Test:  # note here
    def __str__(self):
        return 'self'

    def __unicode__(self):  # and here:
        return 'self'

    def __bool__(self):
        return True


if __name__ == '__main__':
    try:
        name = input('Input something: ')
        print(str(Test()), name, str(name))
        print(1, 2, int(2), end=' ')
    except (ValueError, KeyError) as ex:
        print(ex.message)  # note here
