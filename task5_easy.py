#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import sys
import os

def make_dir(dir_name):
    if not dir_name:
        print("Укажите имя директории.")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print("Директория '{}' создана".format(dir_name))
    except FileExistsError:
        print("Директория '{}' уже существует".format(dir_name))
    except Exception as e:
        print(e.__class__)

def rm_dir(dir_name):
    if not dir_name:
        print("Укажите имя директории.")
        return
    dir_path =  os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print("Директория '{}' удалена".format(dir_name))
    except FileNotFoundError:
        print("Директорию '{}' не найдена".format(dir_name))
    except Exception as e:
        print(e.__class__)

def list_dir(dir_name):
    if not dir_name:
        print("Укажите имя директории.")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        print("Вывод содержимого текущей директории...{}'{}'".format("\n", dir_path))
        for idx in os.listdir(dir_path):
            print(idx)
    except PermissionError:
        print("Не хватает прав на чтение директории '{}'".format(dir_path))
    except Exception as e:
        print(e.__class__)

