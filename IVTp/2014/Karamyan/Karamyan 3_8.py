# Задача 3, Вариант 8

# Напишите программу, которая выводит имя "Борис Николаевич Бугаев", и запрашивает его псевдоним. Программа должна сцеплять две эти строки и выводить полученную строку, разделяя имя и псевдоним с помощью тире.

# Карамян Н.Г.
# 17.05.2016


print ("Герой нашей сегодняшней программы — Борис Николаевич Бугаев")

p_name = input ("Под каким же псевдонимом он известен? Ваш ответ: ")

if (p_name) == ("Андрей Белый"):
	print ("Все верно Борис Николаевич Бугаев — " + p_name)

else:
	print ("Вы ошиблись, это не его псевдоним :(")

input ("Жмакни Enter, чтобы выйти.")