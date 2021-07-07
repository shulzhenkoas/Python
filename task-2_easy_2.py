#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

sequence2_1 = [7, '8', 1, 4, 'ab', 'bc', 'cd', 4, 'a', 'ef', '8']
sequence2_2 = ['dc', 2, 4, 'e', 'b', 'cd', 'a', '1']
for item2 in sequence2_2:
	idx2 = sequence2_1.count(item2)
	if idx2:
		n = 0
		while n < idx2:
			sequence2_1.remove(item2)
			n += 1
print(sequence2_1)