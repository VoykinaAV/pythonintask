#������ 8 ������� 9
# ����������� ���� "���������" (��. �.������ ������������� �� Python. ��.4) ���, ����� � ������� ����� ���������� ���������. 
# ����� ������ �������� ����� �� ��������� � ��� ������, ���� � ���� ��� ������� �������������. 
# ������������ ������� ���������� �����, �� ������� �� ������, ���������� ����� ��� ���������, �������� ������ ���, ��� �������� ���������.
#Voykina A.V.
#30.10.16
import random
points = 1000
words =("�����","�����","����","�������","������","����������","������")
choice=random.choice(words)
check = choice
i=0
anagramma = ""
while choice:
	symbol = random.randrange(len(choice))
	anagramma += choice[symbol]
	choice = choice[:symbol] + choice[(symbol+1):]
print("������. ����� ������� � ���������!")
print("� ������� �����: ", anagramma)
vibor = input ("���� �����: ")
while (vibor != check):
	if(vibor == ""):
		print(i,"�����: ",check[i])
		i+=1
	if points <= 0:
		break
	vibor=input("�����������. �������� ��� ���: ")
	points-=100
if vibor == check: 
	print("\n���������! ��� �����:", check)
	print("�� ������",points,"�����! �������!")
else: 
	print("� ���������, � ���� 0 �����, � �� ��������. ���������� �����:",check)
input ("������� ENTER ��� �����������")



