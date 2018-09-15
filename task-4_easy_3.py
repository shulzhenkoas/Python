#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

def lucky_ticket(ticket_number):
    string_ticket = str(ticket_number)
    len_half = len(string_ticket) // 2
    str1 = string_ticket[:len_half:]
    str2 = string_ticket[:0-len_half-1:-1]
    sum1 = 0
    sum2 = 0
    for a in str1:
        sum1 += int(a)

    for b in str2:
        sum2 += int(b)

    if sum1 == sum2:
        return 'Билет счастливый!'
    else:
        return 'Билет не счастливый :('

print("P.S.: При нечетном количестве цифр, цифра по середине опускается")
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(4367518))
print(lucky_ticket(1234567890987654321))