#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

print('Решим уравнение ax^2 + bx + c = 0')
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

discr = b**2 - 4 * a * c;
print("Дискриминант D = %.2f" % discr)
if discr > 0:
	import math
	x1 = (-b + math.sqrt(discr)) / (2 * a)
	x2 = (-b - math.sqrt(discr)) / (2 * a)
	print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
	x = -b / (2 * a)
	print("x = %.2f" % x)
else:
	print("Корней нет")