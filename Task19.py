# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('1.txt', 'w') as data:
    data.write('16*x^2 + 3*x^5')
with open('2.txt', 'w') as data:
    data.write('23*x^4 + 7*x^3')

with open('1.txt', 'r') as data:
    poly_1 = data.readline()
    list_1 = poly_1.split()


with open('2.txt', 'r') as data:
    poly_2 = data.readline()
    list_2 = poly_2.split()

print(f'{list_1} + {list_2}')
sum = list_1 + list_2

with open('sum.txt', 'w') as data:
    data.write(f'{sum}')
