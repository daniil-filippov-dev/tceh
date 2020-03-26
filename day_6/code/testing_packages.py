# -*- coding: utf-8 -*-

from normal_package.normal_file import MyClass, my_function, GLOBAL_VAR

my_function()


try:
    from not_a_package.my_module import print_info

    # why does it happen:
    # http://stackoverflow.com/questions/16981921/relative-imports-in-python-3
    print_info()
except ImportError as e:
    print(e)
