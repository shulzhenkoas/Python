#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    n = 1
    while n < len(origin_list):
        for i in range(len(origin_list)-n):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        n += 1
    return origin_list

print(sort_to_max([3, 11, -7, 3, 3.7, -11, 0, 5, -11]))