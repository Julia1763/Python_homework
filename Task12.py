#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

from random import randrange
import math



number = int(input('Введите целое число: '))
a = [randrange(0, 10) for i in range(number)]
print(f'Вывод исходного списка: {a}')
Multy = []
size = math.ceil(number / 2)

def product_of_list(a):
    for i in range(size):
            Multy = [a[i] * a[-1-i] for i in range(0,i+1)]
    return Multy       

print(product_of_list(a))


