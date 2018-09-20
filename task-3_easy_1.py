#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

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