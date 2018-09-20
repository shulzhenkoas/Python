#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import task5_easy as easy

def change_dir():
    try:
        dir_name = input("Введите директорию для перехода:")
        os.chdir(dir_name)
        print("Текущая директория: '{}'".format(os.getcwd()))
    except FileNotFoundError:
        print("Невозможно перейти в директорию: '{}'".format(dir_name))
    except Exception as e:
        print(e.__class__)

def read_dir():
    dir_name = "."
    easy.list_dir(dir_name)
    print("---------------------------------------------\n")

def remove_dir():
    dir_name = input("Введите директорию для удаления:")
    easy.rm_dir(dir_name)

def create_dir():
    dir_name = input("Введите директорию для создания:")
    easy.make_dir(dir_name)

def user_action(numb):
    print("action = ", numb)
    if numb == 1:
        change_dir()
    elif numb == 2:
        read_dir()
    elif numb == 3:
        create_dir()
    elif numb == 4:
        remove_dir()

def main_prog():
    while True:
        choice = int(input("Выберите пункт:\n"
                           "1. Перейти в директорию\n"
                           "2. Просмотреть содержимое текущей директории\n"
                           "3. Создать директорию\n"
                           "4. Удалить директорию\n"
                           "0. Выход\n"
                           "---------------------------------------------\n"
                           "Ваш выбор: "))
        if choice == 0:
            break
        else:
            user_action(choice)
main_prog()

