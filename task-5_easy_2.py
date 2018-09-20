#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

def list_dir():
    if not dir_name:
        print("Укажите имя директории.")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        print("Вывод содержимого текущей директории...\n",dir_path)
        for idx in os.listdir(dir_path):
            print(idx)
    except PermissionError:
        print("Не хватает прав на чтение директории {}".format(dir_path))

# Вызов функции вывода содержимого текущей директории
dir_name = '.'
list_dir()