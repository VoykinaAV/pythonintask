#������ 10 ������� 9
#�������� ��������� "��������� ����������" ��� ����. ������������ ������ ���� ������������� 30 �������, ������� ����� ������������ ����� �������� ����������������: ����, ��������, �������� � ��������. ���� ������� ���, ����� ������������ ��� �� ������ ����� ��� ������ �� ������ "����", �� � ���������� �� ���� �� �������������, ������� �� ����� ��������� ������ ��������.
#Voykina A.V.
#01.11.16
print("��������� ���������")
points = 30
character = {"����" : 8, "��������" : 8, "��������" : 8, "��������" : 8}
for i in character:
	print(character[i])
values = character.keys()
atr = input("������� �������, ������� �� ������ ��������: ")
num = int(input("������� ���������� ����� (\"-\" ��� ��������� �����): "))
print(num)
points -= num
for value in character:
	if attr == value:
		print(atr)

class Character:
	def __init__(self, points):
		self.atrib = ("����", "��������", "��������", "��������")
		self.values = [8, 8, 8, 8]
		self.ppool = points
	def update(self, chrt, num):
		print()
		for i in range (len(self.atrib)):
			if chrt.capitalize() == self.atrib[i]:
				self.ppool -= num
				if self.ppool < 0:
					num += self.ppool
					self.ppool = 0
				self.values[i] += num
			print(self.atrib[i], end = ' : ')
			print(self.values[i])
		print("\n����:", self.ppool)

pers = Character(30)
chrt, num = "some", 0
while chrt != "":
	pers.update(chrt, num)
	chrt = input("\n��������������: ").strip()
	temp = input("���� (\"-\" ��� ����������, Enter ��� ������): ").strip()
	if len(temp):
		if temp.isdigit() or temp[0] == '-':
			num = int(temp)
print("�������� ��������� ���������...")
input("\n������� Enter ��� ������")



