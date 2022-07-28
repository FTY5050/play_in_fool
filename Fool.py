import time
import os
import random
cazir = []
rancase= []  
bita = []
stole = []
caloda_cart = [ 
    "2п", "3п", "4п", "5п",
    "6п", "7п", "8п", 
    "9п", "10п","Jп", 
    "Qп", "Kп", "Aп",#пики
    "2б", "3б", "4б", "5б",
    "6б", "7б", "8б", 
    "9б", "10б","Jб", 
    "Qб", "Kб", "Aб",#буби
    "2к", "3к", "4к", "5к",
    "6к", "7к", "8к", 
    "9к", "10к","Jк", 
    "Qк", "Kк", "Aк",#крести
    "2ч", "3ч", "4ч", "5ч",
    "6ч", "7ч", "8ч", 
    "9ч", "10ч","Jч", 
    "Qч", "Kч", "Aч",#черви
    "jockR", "jockB"
    ]
p_hod = 0
vol = 0
player_vol = "2"
num = ["1", "2",]
num1 = [1, 3, 5, 6]
p_1 = []
p_2 = []
p_3 = []
p_4 = []
p_5 = []
p_6 = []
p_7 = []
p_8 = []
p_9 = []
p_n_1 = "None"
p_n_2 = "None"
p_n_3 = "None"
p_n_4 = "None"
p_n_5 = "None"
p_n_6 = "None"
p_n_7 = "None"
p_n_8 = "None"
p_n_9 = "None"
class play_in_cart: 
    def razdacha():
        global p_1, caloda_cart
        er =0
        x = 0
        dasas = 0
        if dasas == 0:
            random_cart = random.choice(caloda_cart)
            cazir.append(random_cart)
        try:
            if vol == 1:
                for i in range(6):
                    random_cart = random.choice(caloda_cart)
                    p_1.append(random_cart)
                    caloda_cart.remove(random_cart)
            if vol == 2:
                for i in range(6):
                    random_cart = random.choice(caloda_cart)
                    p_1.append(random_cart)
                    caloda_cart.remove(random_cart)
                for i in range(6):
                    random_cart = random.choice(caloda_cart)
                    p_2.append(random_cart)
                    caloda_cart.remove(random_cart)
            if vol == 3:
                for i in range(6):
                    random_cart = random.choice(caloda_cart)
                    p_1.append(random_cart)
                    caloda_cart.remove(random_cart)
                for i in range(6):
                    random_cart = random.choice(caloda_cart)
                    p_2.append(random_cart)
                    caloda_cart.remove(random_cart)
                for i in range(6):
                    random_cart = random.choice(caloda_cart)
                    p_3.append(random_cart)
                    caloda_cart.remove(random_cart)
            if vol == 4:
                for i in range(6):
                    random_cart = random.choice(caloda_cart)
                    p_1.append(random_cart)
                    caloda_cart.remove(random_cart)
                for i in range(6):
                    random_cart = random.choice(caloda_cart)
                    p_2.append(random_cart)
                    caloda_cart.remove(random_cart)
                for i in range(6):
                    random_cart = random.choice(caloda_cart)
                    p_3.append(random_cart)
                    caloda_cart.remove(random_cart)
                for i in range(6):
                    random_cart = random.choice(caloda_cart)
                    p_4.append(random_cart)
                    caloda_cart.remove(random_cart)
        except IndexError:
            pass

    def razdacha1cart():
        global p_1, caloda_cart
        er =0
        try:
            if vol == 1:    
                for i in range(100):
                    q = random.randint(1, 54)
                for i in caloda_cart:
                    er+=1
                    if q == er:
                        p_1.append(i)
                        caloda_cart.remove(i)
        except ValueError:
            for i in range(6):
                for i in caloda_cart:
                    caloda_cart.append(i)
                    p_1.remove(i)
            play_in_cart.razdacha()
        global p_2
        er =0
        try:
            if vol == 1:    
                for i in range(100):
                    q = random.randint(1, 54)
                for i in caloda_cart:
                    er+=1
                    if q == er:
                        p_2.append(i)
                        caloda_cart.remove(i)
        except ValueError:
            for i in range(6):
                for i in caloda_cart:
                    caloda_cart.append(i)
                    p_2.remove(i)
            play_in_cart.razdacha()
        global p_3
        er =0
        try:
            if vol == 1:    
                for i in range(100):
                    q = random.randint(1, 54)
                for i in caloda_cart:
                    er+=1
                    if q == er:
                        p_3.append(i)
                        caloda_cart.remove(i)
        except ValueError:
            for i in range(6):
                for i in caloda_cart:
                    caloda_cart.append(i)
                    p_3.remove(i)
            play_in_cart.razdacha()
        global p_4
        er =0
        try:
            if vol == 1:    
                for i in range(100):
                    q = random.randint(1, 54)
                for i in caloda_cart:
                    er+=1
                    if q == er:
                        p_4.append(i)
                        caloda_cart.remove(i)
        except ValueError:
            for i in range(6):
                for i in caloda_cart:
                    caloda_cart.append(i)
                    p_4.remove(i)
            play_in_cart.razdacha()

    def c_p(var_name,var_value):
        global vol, p_n_1, p_n_2, p_n_3, p_n_4
        vol += 1
        globals()[var_name] = var_value
        if vol == 1:
            p_n_1 = var_name
        if vol == 2:
            p_n_2 = var_name
        if vol == 3:
            p_n_3 = var_name
        if vol == 4:
            p_n_4 = var_name

    def f_p():
        global vol
        player_vol = input("сколько игроков? \nmax-4: ")
        for i in ["1","2","3","4"]:
            var_name = input('имя игрока: ')
            play_in_cart.c_p(var_name, var_name)
            print(f'игрок {var_name} создан')
            if i == player_vol:
                player_vol = vol
                return play_in_cart.m_m()
    def m_m():
        global num, num1, p_hod, i13, hod, vol
        infoc = " "
        infcar = 6
        numb = 0
        for i in num:
            if p_hod != 0:
                p_hod += 1
            time.sleep(1)
            os.system('cls')
            num += num1
            caloda_i = 0
            for i in caloda_cart:
                caloda_i += 1
                if caloda_i == 1:
                    infoc = "а"
                else:
                    infoc = " "
            if p_hod <= 0:
                if vol == 1:
                    print(f"{p_n_1} {p_1}")
                if vol == 2:
                    print(f"{p_n_1} {p_1}")
                    print(f"{p_n_2} {p_2}")
                if vol == 3:
                    print(f"{p_n_1} {p_1}")
                    print(f"{p_n_2} {p_2}")
                    print(f"{p_n_3} {p_3}")
                if vol == 4:
                    print(f"{p_n_1} {p_1}")
                    print(f"{p_n_2} {p_2}")
                    print(f"{p_n_3} {p_3}")
                    print(f"{p_n_4} {p_4}")
            if p_hod >= 5:
                p_hod = 1
            if p_hod == 0:
                print(f"ход 0 \nРаздача")
                play_in_cart.razdacha()
                input("Press Enter\n")
                os.system('cls')
                p_hod += 1
                
            if p_hod == 1:
                print(f"Казырка {cazir} \nБита {bita} \nна столе{stole} \nВ колоде {caloda_i} Карт{infoc} \n")
                o1 = input(f"Ход {p_n_1} \n{p_1} \nДобавить карту на стол-1 \nЗабрать карту со стола-3 \nбита-2 \n(1/2/3): ")
                if o1 == "1":
                    print(f"{p_1}")
                    o = input("какую? ")
                    for i in p_1:
                        if o == i:
                            stole.append(i)
                            p_1.remove(i)
                if o1 == "2":
                    print(f"{stole} \nБита!")
                    for i1 in range(10):
                        for i in stole:
                            bita.append(i)
                            stole.remove(i)
                if o1 == "1":
                    play_in_cart.razdacha1cart()
                    print(f"{p_n_1}--Взял карту из колоды!")
                    time.sleep(1)
                if o1 == "3":
                    print(f"{p_n_1}--Беру!")
                    for i in stole:
                            stole.remove(i)
                            p_1. append(i)
            if p_hod == 2 and p_n_2 != "None":
                print(f"Казырка {cazir} \nБита {bita} \nна столе{stole} \nВ колоде {caloda_i} Карт{infoc} \n")
                o1 = input(f"Ход {p_n_2} \n{p_2} \nДобавить карту на стол-1 \nЗабрать карту со стола-3 \nбита-2 \n(1/2/3): ")
                if o1 == "1":
                    print(f"{p_2}")
                    o = input("какую? ")
                    for i in p_2:
                        if o == i:
                            stole.append(i)
                            p_2.remove(i)
                if o1 == "2":
                    print(f"{stole} \nБита!")
                    for i1 in range(10):
                        for i in stole:
                            bita.append(i)
                            stole.remove(i)
                if o1 == "1":
                    play_in_cart.razdacha1cart()
                    print(f"{p_n_2}--Взял карту из колоды!")
                    time.sleep(1)
                if o1 == "3":
                    print(f"{p_n_2}--Беру!")
                    for i in stole:
                            stole.remove(i)
                            p_2. append(i)
            if p_hod == 3 and p_n_3 != "None":
                print(f"Казырка {cazir} \nБита {bita} \nна столе{stole} \nВ колоде {caloda_i} Карт{infoc} \n")
                o1 = input(f"Ход {p_n_3} \n{p_3} \nДобавить карту на стол-1 \nЗабрать карту со стола-3 \nбита-2 \n(1/2/3): ")
                if o1 == "1":
                    print(f"{p_3}")
                    o = input("какую? ")
                    for i in p_3:
                        if o == i:
                            stole.append(i)
                            p_3.remove(i)
                if o1 == "2":
                    print(f"{stole} \nБита!")
                    for i1 in range(10):
                        for i in stole:
                            bita.append(i)
                            stole.remove(i)
                if o1 == "1":
                    play_in_cart.razdacha1cart()
                    print(f"{p_n_3}--Взял карту из колоды!")
                    time.sleep(1)
                if o1 == "3":
                    print(f"{p_n_3}--Беру!")
                    for i in stole:
                            stole.remove(i)
                            p_3. append(i)
            if p_hod == 4 and p_n_4 != "None":
                print(f"Казырка {cazir} \nБита {bita} \nна столе{stole} \nВ колоде {caloda_i} Карт{infoc} \n")
                o1 = input(f"Ход {p_n_4} \n{p_4} \nДобавить карту на стол-1 \nЗабрать карту со стола-3 \nбита-2 \n(1/2/3): ")
                if o1 == "1":
                    print(f"{p_4}")
                    o = input("какую? ")
                    for i in p_4:
                        if o == i:
                            stole.append(i)
                            p_4.remove(i)
                if o1 == "2":
                    print(f"{stole} \nБита!")
                    for i1 in range(10):
                        for i in stole:
                            bita.append(i)
                            stole.remove(i)
                if o1 == "1":
                    play_in_cart.razdacha1cart()
                    print(f"{p_n_4}--Взял карту из колоды!")
                    time.sleep(1)
                if o1 == "3":
                    print(f"{p_n_4}--Беру!")
                    for i in stole:
                            stole.remove(i)
                            p_4. append(i)

#    def create_global_variable(var_name, var_value):
#      if var_name in globals():
#        print('Such variable already exists')
#        return
#        globals()[var_name] = var_value
#
#    var_name = input('Enter variable name: ')
#    var_value = input('Enter variable value: ')
#
#    create_global_variable(var_name, var_value)
#
#    print(f'You have created variable {var_name}={eval(var_name)}')

if __name__ == '__main__':
    play_in_cart.f_p()