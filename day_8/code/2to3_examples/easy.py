# -*- coding: utf-8 -*-

class Test:  # note here
    def __str__(self):
        return 'self'

    def __unicode__(self):  # and here:
        return u'self'

    def __nonzero__(self):
        return True


if __name__ == '__main__':
    try:
        name = raw_input(u'Input something: ')
        print str(Test()), name, unicode(name)
        print 1, 2, long(2),
    except (ValueError, KeyError), ex:
        print ex.message  # note here
