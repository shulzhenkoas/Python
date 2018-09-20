#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import sys
import os

#print('sys.path = ',sys.path)
#print("Текущая директория:",os.getcwd())
#print("sys.argv = ", sys.argv)

def make_dir():
    if not dir_name:
        print("Укажите имя директории.")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print("Директория {} создана".format(dir_name))
    except FileExistsError:
        print("Директория {} уже существует".format(dir_name))

def rm_dir():
    if not dir_name:
        print("Укажите имя директории.")
        return
    dir_path =  os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print("Директория {} удалена".format(dir_name))
    except FileNotFoundError:
        print("Директорию {} не найдена".format(dir_name))

# Создаем директории dir1 - dir9
print("Создаем директории в текущем каталоге...\n{}:".format(os.getcwd()))
dir_name = ''
str_dir = ['dir' + str(dr) for dr in range(1, 10)]
for dir_name in str_dir:
    make_dir()

# Удаляем директории dir1 - dir9
input("\nНажмите любую клавишу, чтобы удалить только что созданные директории...")
for dir_name in str_dir:
    rm_dir()