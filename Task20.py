#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

words = input('Введите текст: ')

print(words.translate({ord(i): None for i in 'абв'}))





