# Задача 4. Вариант 20
#Напишите программу, которая бы при запуске случайным образом отображала имя одного из трех мушкетеров - товарищей д'Артаньяна.
# Рожко Ксения
# 23.05.2016


import random

print ("Программа случчайным образом отображает имя одного из трех мушкетеров - товарищей д'Артаньяна")

x = int (random.randint(1,3))

print ('\nОдин из мушкетеров - ', end = '')

if x == 1:
       print ('Атос')
elif x == 2:
    print ('Партос')
else:
    print ('Арамис')
    
input("\nДля выхода нажмите Enter.")
