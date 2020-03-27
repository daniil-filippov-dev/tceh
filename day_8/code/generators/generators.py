# -*- coding: utf-8 -*-


def cities():
    arr = [
        'Moscow',
        'Novosibirsk',
        'Perm',
        'Irkutsk',
        'Tula',
    ]
    return iter(arr)


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    cities_gen = cities()

    while True:
        try:
            print(next(cities_gen))
        except StopIteration:
            break

    try:
        print(next(cities_gen))  # create new cities()
    except StopIteration:
        print('Will not work')

    new_cities = cities()
    print(next(new_cities))
    print(list(new_cities))

    fib_gen = fib()
    for index, _ in enumerate(range(10)):
        print(index, next(fib_gen))
