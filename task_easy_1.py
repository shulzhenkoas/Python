#__author__ = 'Шульженко А.С.'
# Coding UTF-8

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# Генерация произвольного числа (спасибо Google)
import random
numb = random.randint(0,1000000)
print("Random number from 0 to 1000000: ", numb)

# Вывод через цикл for
print("Output FOR...")
for a in str(numb):
	print(a)

# Вывод через цикл while
print("Output WHILE...")
while numb != 0:
	print(numb % 10)
	numb = numb // 10