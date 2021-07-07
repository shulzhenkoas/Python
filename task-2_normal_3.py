#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

from random import randint
sequence3 = []
range = randint(0, 30)
i = 0
while i < range:
    sequence3.append(randint(-100, 100))
    i += 1
print("В списке ниже {} элементов:".format(range))
print(sequence3)