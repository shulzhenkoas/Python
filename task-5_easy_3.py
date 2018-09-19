#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

lst_orig = [9, 2, 4, 15, -3, 3, 1, 12, 0, -12, 36]
lst_new3 = [idx for idx in lst_orig if idx % 3 == 0 and idx > 0 and idx % 4 != 0]
print("lst_new3 = ", lst_new3)
print(type(lst_new3))