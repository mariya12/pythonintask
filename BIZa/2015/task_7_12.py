#Задача 7 Вариант 12
#Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.
#Иванова Мария Дмитриевна
#10.10.16
import random
print("Игра Угадай собор Московского кремля\n Игрок загадывает один из соборов наугад, а именно:\n Успенский собор,Архангельский собор,колокольня Ивана Великого,церковь Положения Ризы Божьей Матери,пятиглавый собор Двенадцати апостолов, домовые церкви,собор Василия Блаженного, Собор Казанской Иконы Божией Матери\nВам необходимо угадать один из них:")
answer = random.choice(['Успенский собор','Архангельский собор','колокольня Ивана Великого','церковь Положения Ризы Божьей Матери','пятиглавый собор Двенадцати апостолов',' домовые церкви','собор Василия Блаженного', 'Собор Казанской Иконы Божией Матери'])
statbonus = 0
bonus = 12
attempts = 6
startatt = 7
print(answer)
while attempts >= 0:
	if attempts == 0: 
		print("К сожалению вы исчерпали свои попытки. Вы проиграли :(, ваши бонусы:"+str(statbonus))
		break
	birds = input("Введите загаданного писателя: ")
	if answer == birds:
		statbonus = statbonus + bonus
		print("Поздравляю! Вы угадали писателя с "+ str(startatt - attempts) +" раза, ваши очки: "+str(statbonus))
		response = input("Хотите продолжить игру? (Y/N):")
		if response == "Y":
			print("Отлично, продолжаем! Ваши очки: "+str(statbonus))
			bonus = 12
			attempts = 6
			answer = random.choice(['Успенский собор','Архангельский собор','колокольня Ивана Великого','церковь Положения Ризы Божьей Матери','пятиглавый собор Двенадцати апостолов',' домовые церкви','собор Василия Блаженного', 'Собор Казанской Иконы Божией Матери'])
			print(answer)
			continue
		elif response == "N":
			print("Спасибо за игру, ваши очки: "+str(statbonus))
			break
		else:
			response = input("Вы не ввели ответ. Хотите продолжить игру? (Y/N):")
	else:
	 attempts = attempts - 1
	 bonus = bonus - 2
	 print("Неправильно, попробуйте еще раз, осталось попыток: "+str(attempts))
input("Нажмите Enter для выхода.")	 
