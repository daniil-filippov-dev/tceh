# -*- coding: utf-8 -*-

from jinja2 import Template




def simple_hello_world():
    t = Template('Hello {{ something }}!')
    result = t.render(something='World')

    print(result)


def for_example(iterable=None):
    if iterable is None:
        iterable = range(1, 11)

    t = Template("""
My favorite numbers: {% for n in array %}
{{ n }}{% endfor %}
"""
    )

    result = t.render(array=iterable)
    print(result)


def if_example(value):
    t = Template("""
{% if value %}
True!
{% else %}
False.
{% endif %}
"""
    )

    result = t.render(value=value)
    print(result)

if __name__ == '__main__':
    simple_hello_world()
    for_example()

    if_example(True)
    if_example('')
