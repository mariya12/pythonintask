﻿#Задача 3. Вариант 2.
#Напишите программу, которая выводит имя "Мария Луиза Чеччарелли", и запрашивает его псевдоним. Программа должна сцеплять две эти строки и выводить полученную строку, разделяя имя и псевдоним с помощью тире.

#Григорьев А.О.
#23.05.2016

print ("Герой нашей сегоднящней программы - Мария Луиза Чеччарелли")
psev=input("Под каким же именем мы знаем этого человека? Ваш ответ:")
if (psev)==("Моника Витти"):
	print ("Всё верно:  Мария Луиза Чеччарелли - "+psev)
else:
	print ("Вы ошиблись, это не её псевдоним.")
input("нажмите Enter для выхода") 