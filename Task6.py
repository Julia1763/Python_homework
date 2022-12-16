#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Пример:
#6782 -> 23
#0,56 -> 11


Number = input('Введите число: ')

def sum_of_digits(Number):

  result = 0
  Number = abs(Number)
  for digits in Number:
    if digits != '.':
      result += Number % 10
      Number = Number // 10
  return result

print(sum_of_digits(Number))



