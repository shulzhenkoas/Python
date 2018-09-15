#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

def my_round(number, ndigits):
    int_dig = int(number)
    float_dig1 = (number - int_dig) * (10 ** ndigits)
    float_dig2 = int(float_dig1)
    float_dig3 = float_dig1 - float_dig2
#    print("int_dif=",int_dig)
#    print("float_dig1=",float_dig1)
#    print("float_dig2=",float_dig2)
#    print("float_dig3=",float_dig3)
    if float_dig3 > 0.5:
        float_dig2 += 1
    return int_dig + float_dig2 / (10 ** ndigits)

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print("Проверка через функцию round...")
print(round(2.1234567, 5))
print(round(2.1999967, 5))
print(round(2.9999967, 5))