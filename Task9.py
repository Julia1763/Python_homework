#4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

index = open('file.txt','w')
for line in index:
    print(line)
index.close()

from random import randrange

n = 100
a = [randrange(-n,n, 100) for i in range(n)]
print(f'Вывод сгенерированного списка: {a}')