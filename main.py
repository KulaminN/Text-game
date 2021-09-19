import random as j
import random as attack


def printParameters():
    print("{0} хп, {1} денежек и {2} урона.".format(hp, coins, damage))

def printHp():
    print("У тебя", hp, "жизней.")

def printCoins():
    print("У тебя", coins, "денег.")

def printDamage():
    print("У тебя", damage, "урона.")

def meetShop():
    global hp
    global coins
    global damage

    def buy(cost):
        global coins
        if coins >= cost:
            coins -= cost
            printCoins()
            return True
        print("У тебя мало денег")
        return False

    weaponLVL = j.randint(1, 4)
    weaponDmg = j.randint(1, 5) * weaponLVL
    weapons = ["меч", "Лук"]
    weaponRarities = ["Ипорченный", "Обычный", "Редкий", "Легендарный"]
    weaponRarity = weaponRarities[weaponLVL - 1]
    weaponCost = j.randint(3, 10) * weaponLVL
    weapon = j.choice(weapons)

    Hppotion = 5

    print("На пути тебе встретился торговец!")
    printParameters()

    while input("Что ты будешь делать (зайти/уйти): ").lower() == "зайти":
        print("1) зелье здоровья - ", Hppotion, "монет;")
        print("2)  {0} {1} - {2} денег.".format(weaponRarity, weapon, weaponCost))

        choice = input("Что хочешь приобрести: ")
        if choice == "1":
            if buy(Hppotion):
                hp += 5
                printHp()
        elif choice == "2":
            if buy(weaponCost):
                damage = weaponDmg
                printDamage()
        else:
            print("Я такое не продаю")


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
    global coins
    global hp
    global damage

    situation = j.randint(0, 10)
    k = attack.randint(1, 10)
    if situation == 0:
        meetShop()
    elif situation == 1:
        print("Monster с силой ", (k))
        coins = coins + k
        printParameters()
        if damage < k:
            hp = hp - k
    else:
        input("Блуждаю...")


while True:
    gameLoop()
    if hp <= 0:
        if input("Хочешь начать сначала(да/нет)").lower() == "да":
            coins = 2
            damage = 1
            hp = 100
        else:
            break
