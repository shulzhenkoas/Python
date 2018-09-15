#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Все задачи текущего блока решите с помощью генераторов списков!
# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

lst_one = ['яблоко', 'банан', 'киви', 'слива', 'персик', 'груша', 'абрикос', 'банан']
lst_two = ['киви', 'абрикос', 'хурма', 'чернослив', 'нектарин', 'королек', 'банан']

# Можно и так, set - чтобы вывести только уникальные элементы списка
#lst_new2 = set([fr2 for fr2 in lst_two for fr1 in lst_one if fr1 == fr2])
lst_new2 = [fr1 for fr1 in lst_one for fr2 in lst_two if fr1 == fr2]
print("lst_new2 = ", lst_new2)
print(type(lst_new2))