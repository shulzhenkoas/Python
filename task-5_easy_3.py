#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil
import sys

#print(__file__)
#print("sys.argv = ", sys.argv[0])
file_path = sys.argv[0]

def copy_file():
    try:
        print("Создаем копию файла {}\n".format(file_path))
        shutil.copyfile(file_path, file_path + "_bkp")
    except Exception as e:
        print(e.__class__)

# Вызов функции создающей копию данного файла
copy_file()