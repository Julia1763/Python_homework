# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform

n = int(input('Введите количество элементов: '))
a = [round(uniform(-99.999, 100), 2) for i in range(n)]
print(f'Вывод сгенерированного списка: {a}')


def max_of_a(a):
    Max = abs(a[0]%100)
    for i in range(len(a)):
        if abs(a[i])%100 > Max:
            Max = abs(a[i])
    return Max

print(f'Вывод максимального элемента: {max_of_a(a)}')

def min_of_a(a):
    Min = a[0]
    for i in range(len(a)):
        if a[i] < Min:
            Min = a[i]
    return Min

print(f'Вывод минимального элемента: {min_of_a(a)}')

delta = max_of_a(a) - min_of_a(a)

print(f'Вывод минимального элемента: {delta}')