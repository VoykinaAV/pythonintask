#Напишите программу, которая бы при запуске случайным образом отображала название одной из трех стран, 
#входящих в военно-политический блок "Антанта".

#Voykina A.V.  
#22.09.2016

import random
choice=random.randint(1,3)
random="Одной из стран блока 'Атланта' является "
if choice ==1:
	print(random+"Россия.")
elif choice ==2:
	print(random+"Англия.")
elif choice ==3:
	print(random+"Франция.")
input("Нажмите ENTER для продолжения")