#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

lst_orig = [1, 2, 4, 0, -2, 3, 7]
lst_new1 = [_**2 for _ in lst_orig]
print("lst_new1 = ", lst_new1)
print(type(lst_new1))

# Доброго времент суток
# ПРосьба ответить на вопрос почему
# lst_new = [_**2 for _ in lst_orig] --> type <class 'list'>, а
# lst_new = (_**2 for _ in lst_orig) --> type <class 'generator'>
# с выводом lst_new =  <generator object <genexpr> at 0x0000002FC94A9B88>
# Спасибо.