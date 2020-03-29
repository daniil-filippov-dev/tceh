from contextlib import contextmanager


@contextmanager
def do_work(value):
    print('some work before, __enter__')
    yield value
    print('some work after, __exit__')

with do_work(14) as w:
    print(w)
