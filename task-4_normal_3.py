#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import re
from os import getcwd,path
from random import randrange

line_3 = ""
# Длина строки может быть max 2501, но это не принципиально
while len(line_3) < 2500:
    line_3 = ''.join([line_3, str(randrange(0, 100))])
# Можно и так, но повторяющиеся последовательности цифр будут короткими
#for _ in range(0, 2500):
#    line_3 = ''.join([line_3, str(randint(0, 9))])

print("Длина строки: ",len(line_3))
print("Получившаяся строка...")
print(line_3)

# Записываем строку (ровно 2500 символов) в новый файл и закрываем его
path = path.join(getcwd(), "Big_num.txt")
with open(path, 'w', encoding='UTF-8') as file_write:
    file_write.write(line_3[:2500])

# Читаем данные из файла и находим самую длинную последовательность
line_3 = ""
print("\nПеременная в которую читаем из файла должна быть пустой:", line_3)
with open(path, 'r', encoding='UTF-8') as file_read:
    line_3 = file_read.read()
print("\nПрочитанная строка...")
print(line_3)
print("Длина прочитанной строки:",len(line_3))
lst6_new = []
for i in range(0, 9):
    pattern3 = ''.join([str(i), '+'])
    lst6_new.append(int(max(re.findall(pattern3, line_3))))
#print(lst6_new)
print("Самая длинная последовательность: ",max(lst6_new))