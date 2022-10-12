#Дана последовательность чисел. Получить список уникальных элементов заданной последовательности, список повторяемых и убрать дубликаты из заданной последовательности.
#Пример:
#[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]


from random import randrange


number = int(input('Введите целое число: '))
a = [randrange(0, 10) for x in range(number)]
unique=list(filter(lambda x: a.count(x) == 1, a))
duplicate=list(set(filter(lambda x: a.count(x) > 1, a)))
uniq_list=list(set(a))
print(a)
print(unique)
print(duplicate)
print(uniq_list)
