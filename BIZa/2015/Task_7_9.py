#������ 7 ������� 9
#������������ ������� ���������� ����� ��� ������ 6, � ������������ � ������� ����� ������� �� 
#������� ���������� ������ �� ������� ���������� �������.
#Voykina A.V.
#29.10.16
import random
pigs=("���-���","���-���","���-���")
choice=random.choice(pigs)
pg=input("�������� ������ �� ���� �������: ")
points=1000
while pg != choice:
	pg=input("�� �������. ���������� ���: ")
	points-=100
	if points <=0:
		break
if points <=0:
	print("� ���������, � ��� 0 �����, � �� ���������. � ��� ��� ��������� �� �����",choice)
else: print("�� �������. ���",choice,"! � ���",points,"�����!")
input("������� ENTER ��� �����������")


