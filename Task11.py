# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randrange

n = int(input('Введите количество элементов: '))
a = [randrange(0, 10) for i in range(n)]
print(f'Вывод сгенерированного списка: {a}')

# Тут первый вариант просто с шагом
def sum_of_position(a):
    sum = 0
    for i in range(len(a)):
        if i % 2 != 0:
            sum = sum + a[i]
    return sum


print(f'Сумма элементов на нечетных позициях равна: {sum_of_position(a)}')

# Тут второй вариант без условия нечетности
def sum_of_position2(a):
    sum = 0
    for i in range(1, len(a), 2):
        sum = sum + a[i]
    return sum


print(f'Сумма элементов на нечетных позициях равна: {sum_of_position2(a)}')
