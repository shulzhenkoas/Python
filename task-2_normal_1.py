#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

from math import sqrt

sequence1_1 = [2, -5, 8, 9, -25, 25, 4]
sequence1_2 = []
for item1 in sequence1_1:
    if item1 == abs(item1):
#        id1_sqrt = item1 ** 0.5
        id1_sqrt = sqrt(item1)
        if id1_sqrt == int(id1_sqrt):
            sequence1_2.append(int(id1_sqrt))
print(sequence1_2)