import random as j
import random as attack
import tkinter

def printParameters():
    print("{0} хп, {1} денежек и {2} урона.".format(hp, coins, damage))


def Bebra(Hp, Coins, Dmg):
    global hp
    global coins
    global damage

hp = Hp = 100
coins = Coins = 2
damage = Dmg = 1

print("Бебра отправилась гулять!")
printParameters()




def gameLoop():
    situation = j.randint(0, 10)
    k = attack.randint(1, 10)
    if situation == 0:
        a = input("Вы попали в магазин! Хотите что то купить или пройдете мимо?(меч'15д'(лук'20д' или зелье'5д') /мимо)")
        global coins
        global damage
        global hp
        if (a == "меч" and coins>=15):
            coins = coins - 15
            damage = damage + 5
        elif (a == "лук" and coins>=20):
            coins = coins - 20
            damage = damage + 8
        elif (a == "зелье" and coins>=5):
            coins = coins - 5
            hp = hp + 5
        else:print("У вас не хватает денег на", a)
    elif situation == 1:
        print("Monster с силой ", (k))
        coins = coins + k
        if damage<k:
           hp = hp - k
    else:
     input("Блуждаю...")

while True:
    gameLoop()
    if hp > 0:
        print("жизней", hp, "Денег", coins, "Дамаг", damage)
    if hp <= 0:
        if input("Хочешь начать сначала(да/нет)").lower() == "да":
            coins = 2
            damage = 1
            hp = 100
        else:
            break
