#__author__ = 'Шульженко А.С.'
# Coding UTF-8

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

# Генерация произвольного числа (спасибо Google)
import random
numb = random.randint(0,1000000)
print("Random number from 0 to 1000000: ", numb)

# Вывод через цикл while
max_numb = 0
for a in str(numb):
	if int(a) > max_numb:
		max_numb = int(a)
print("В числе '", numb, "' максимальное число '", max_numb, "'")