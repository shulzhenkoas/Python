#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def func(unit):
    if unit > 0:
        return True
    else:
        return False


def new_filter(func_name, *args):
    new_args = []
    for value in args:
        if func_name(value):
            new_args.append(value)
    return new_args

digs = [-3, -1, 0, 3, 7, -5]
print(new_filter(func, *digs))

# Просьба пояснить почему вот это работает:
# print(new_filter(func, *[-3, -1, 0, 3, 7, -5]))
# а вот это нет:
# print(new_filter(func, [-3, -1, 0, 3, 7, -5]))
# Спасибо.