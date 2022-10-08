#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""

from random import random

sweets = 2021
max = 28
count = 0

Name1 = input('Введите имя 1го игрока: ')
Name2 = input('Введите имя 2го игрока: ')

x = random

if x == 1:
     lucky = Name1
     loser = Name2
else:
     lucky = Name2
     loser = Name1

print(f'{lucky} ходит первым')

while sweets > 0:
        if count == 0:
            step = int(input(f'Сколько конфет Вы возьмете, {lucky} ?'))
            if step > sweets or step > max:
                print('Можно взять не более 28 конфет. Попробуйте еще раз.')
            sweets -= step
        if sweets >= 0:
            count = 1
        else:
            print('Конфеты закончились.')
        if count == 1:
            step = int(input(f'Сколько конфет Вы возьмете, {loser} ?'))
            if step > sweets or step > max:
                print('Можно взять не более 28 конфет. Попробуйте еще раз.')
            sweets -= step
        if sweets >= 0:
            print(f'Осталось {sweets} конфет')
            count = 0
        else:
            print('Игра окончена.')
   
if count == 1:
        print(f'{loser} победитель!')
else:
        print(f'{lucky} победитель!')
        
