# Задача 7. Вариант 12
#
#Разработайте систему начисления очков для задачи 6,
#в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.
# Курятников П.В
# 25.05.2016 

import random
print ("Программа загадывает название одного из восьми соборов Московского кремля, а игрок должен его угадать. У игрока есть 3 попытки ")


ge= random.randint(1,8)


if ge == 1:
    s="Архангельский собор"
elif ge == 2:
    s="Храм преподобного Иоанна"
elif ge == 3:
    s="Благовещенский собор "
elif ge == 4:
    s="Верхоспасский собор"
elif ge == 5:
    s="Церковь 12 апостолов"
elif ge == 6:
    s="Крестовоздвиженская церковь"
elif ge == 7:
    s="Церковь Ризоположения"
elif ge == 8:
    s="Успенский собор"
a="Вы угадали!"
b= "Вы ошиблись! Попробуйте еще раз!"

trying = 3
bonus = 30
while trying > 0:
    otvet = input("Введите название одного из соборов:")
    if otvet == s:
        print(a)
        break
    else:
        print(b)
        trying = trying - 1
        bonus = bonus - 10
        
        
        

input("Нажмите Enter для выхода.")


