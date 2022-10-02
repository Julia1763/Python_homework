#5. Реализуйте алгоритм перемешивания списка.

from random import randrange

n = 10
a = [randrange(1, 10) for i in range(n)]
def mix_list(a):
 for i in range(1, len(a)-1):
    if (a[i] > a[i+1]):
     a[i], a[i+1] = a[i+1], a[i]       
 return a



print(f'Вывод сгенерированного списка: {a}')
print(f'Вывод перемешанного списка: {mix_list(a)}')