#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет



day = int(input('Введите цифру от 1 до 7 включительно: '))
if day == 6 or day == 7:
  print('Этот день является выходным')
elif day >= 1 and day <= 8:
  print('Это будний день')
else:
  print('Цифра введена некорректно')
