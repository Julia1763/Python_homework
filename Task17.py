# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randrange

New_list = []


number = int(input('Введите целое число: '))
a = [randrange(0, 10) for i in range(number)]
print(f'Вывод исходного списка: {a}')


def count_in_list(a):
    for i in a:
        if a.count(i) == 1:
            New_list.append(i)
    return New_list


print(count_in_list(a))
