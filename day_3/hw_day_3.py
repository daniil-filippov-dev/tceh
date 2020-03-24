# Задачи на закрепление типов аргументов:
# Написать функцию, которая принимает любое количество аргументов чисел.
# Среди них она находит максимальное и минимальное. И возвращает оба
print('Домашнее задание. День 3. Типы аргументов. Задание 1\n')
def extremum_func(*numbers):
    lst = [i for i in numbers]
    lst.sort()
    print('Min', lst[0], '\nMax', lst[len(lst)-1])

extremum_func(1,2,3,4,5,6,7,8,9,0,-12,-1)


# Написать функцию, которая принимает два аргумента: строка и булевый флаг case по-умолчанию равный True.
# Если флаг действителен: возвращаем новую строку, где каждый символ входной приведен к верхнему регистру, иначе - к нижнему
print('\n\nДомашнее задание. День 3. Типы аргументов. Задание 2\n')
def case_switcher(string, case):
    if isinstance(string, str):
        if case:
            return string.upper()
        else:
            return string.lower()

print(case_switcher('I\'m your father Luke!',True))


# Написать функцию, которая принимает любое количество позиционных аргументов - строк
# и один парматер по-умолчанию glue, который равен ':'.
# Соединить все строки таким образом, чтобы в результат попали все строки, длинее 3 символов.
# Для соединения между любых двух строк вставлять glue
print('\n\nДомашнее задание. День 3. Типы аргументов. Задание 3\n')
def smart_concat(*text, glue=':'):
    result_string = ''
    for s in text:
        if len(s) > 3:
            result_string += glue + s

    return result_string

print(smart_concat('abc','metallica','may','unforgiven 2'))
