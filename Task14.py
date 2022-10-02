# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите целое число: '))

def convert_decimal_to_binary(number):
    B_number = ''
    while number > 0:
        B_number = str(number % 2) + B_number
        number //= 2
    return B_number

print(convert_decimal_to_binary(number))

