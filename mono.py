import os
numb_player = input('сколько игроков?\n')
Global_Player = []
def PyDay(Array):
	money = 0
	for i in Array:
		if i == "вода":
			money+=100
		elif i == "лес":
			money+=300
		elif i == "дом":
			money+=500
		elif i == "сталь":
			money+=1000
		elif i == "нефть":
			money+=5000
		elif i == "золото":
			money+=7000
	return money
class Player():
	def __init__(self):
		self.Array=[]
		self.name ="None"
		self.money1=0
if numb_player == "2":
	Player1 = Player()
	Player2 = Player()
	Global_Player.append(Player1)
	Global_Player.append(Player2)
	for i in Global_Player:
		i.name = input(f"изменить ник игрока {i} на \n")
elif numb_player == "3":
	Player1 = Player()
	Player2 = Player()
	Player3 = Player()
	Global_Player.append(Player1)
	Global_Player.append(Player2)
	Global_Player.append(Player3)
	for i in Global_Player:
		i.name = input(f"изменить ник игрока {i} на \n")
input("Настройка игры окончена\nНажмите 'Enter' чтобы продолжить")
#############################################################################################################
while True:
	try:
		
	
		
		all_player = 0
		for i in Global_Player:
			#os.system('clear')
			os.system('cls')
			all_player+=1
			a3 = str(i.Array) 
			str_1 = a3.replace('[', '')
			str_2 = str_1.replace("'", '')
			str_4 = str_2.replace(' ', '')
			str_5 = str_4.replace(']', '')
			print(f"""
Игрок №{all_player}
Ник-{i.name}
Баланс-{i.money1}
Бизнес-{str_5}

1.Добавить бизнес
2.Убрать бизнес
3.Получить Деньги за бизнес
4.Отнять денег
			""")
			a =int(input("Выберите действие:\n"))
			if a == 1:
				ss = input("Добавить-вода,лес,дом,сталь,нефть,золото\n")
				i.Array.append(ss)
			if a == 2:
				s1 = input("Убрать-вода,лес,дом,сталь,нефть,золото\n")
				i.Array.remove(s1)
			if a == 3:
				m = PyDay(i.Array)
				i.money1+=m
			if a == 4:
				sss = int(input("Сколько денег отнять?\n"))
				if sss < 0:
					print("ERROR")
					input()
				else:
					i.money1-=sss
			input("Готова")
	except Exception:
		print("ERROR")
		input()


