# Задача 7. Вариант 13.
# Создайте игру, в которой компьютер загадывает название одного из двух спутников Марса, а игрок должен его угадать.
# Добавление начисления очков

# Костарев А. И.
# 21.03.2015

import random
print ("Программа случайным образом загадывает название одного из двух спутников Марса, вы должны угадать этот спутник.")
spytniki = ("Фобос", "Деймос")
spytnik = random.randint(0,1)
rand = spytniki[spytnik]
ochki=100
otvet=0
while (otvet)!=(rand):
        otvet=input('Ваше название спутника:\t')
        if (otvet)!=(rand):
                print ('Вы не угадали. Поробуйте ещё.')
                ochki/=2
        elif (otvet)==(rand):
                print('Вы угадали')
                print('Ваши очки: '+str(ochki))
                break

        
input ("Нажмите Enter для выхода.")
