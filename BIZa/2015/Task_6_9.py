#������ 6 ������� 9
#�������� ����, � ������� ��������� ���������� ��� ������ �� ���� �������, � ����� ������ ��� �������.
#Voykina A.V.
#29.10.16
import random
pigs=("���-���","���-���","���-���")
choice=random.choice(pigs)
pg=input("�������� ������ �� ���� �������: ")
while pg != choice:
	pg=input("�� �������. ���������� ���: ")
print("�� �������. ���",choice)
input("������� ENTER ��� �����������")


