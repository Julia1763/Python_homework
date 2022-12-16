# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Введите число: '))

Number = []


def devider(number):
    i = 2
    while i <= number:
        if number % i == 0:
            Number.append(i)
            number //= i
        else:
            i += 1
    return Number


print(devider(number))
