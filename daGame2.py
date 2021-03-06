import random
class City: 
    shops = ["NOWHERE!"]
    name = "None"
    weapons = ["NADA!"]
    #description = None
    def __init__(self, name):    
        self.name = name

class Gabrieapolis(City):
    weapons = []
    name = "Gabrieapolis"
    def __init__(self):
        self.weapons = [titaniumElectricSpear(),  LongSword(), silverPoisonDoubleSidedAxe(), lightningBolt(), machineGun(), lightSaber()]
        print "Welcome to the city of Gabrieapolis, the city of blacksmithing, where weapons are made."

    
class Boston(City):  
    weapons = []
    name = "Boston"
    def __init__(self):
        print("Welcome to Boston")
        self.weapons = [LongSword(), Bow(), Chestpiece(), Helmet()]

class Zschorlau(City):
    name = "Zschorlau"
    def __init__(self):
        print "Welcome to the city of mining and craftsmanship. Here you can find the finest metals, coals and gemstones. \nIn addition to this you will find finely crafted wooden sculptures, \nWeihnachtspyramide and instruments."
        self.weapons = [guildedRapier(), jadedPoisonDagger(), goldMinigun(), uraniumScythe()]
class Fidgura(City):
    weapons = []
    name = "Fidgura"
    def __init__(self):    
        print("Welcome to Fidgura; the city filled with unusual weapons. Pick one and fight the monsters.")
        self.weapons = [flamingBaseball(), atomicSpinner()]
class PotionShop:
    def __init__(self):
        potion = None
        inpt = raw_input ("Welcome to the potion shop, what do you want to buy?\n1. Health Potion ($55)\n2. Mana Potion($50)\n3. Suicide potion($15)\n")

        if inpt == "None" or inpt == "none":
            print "Then why did you come here? Get out! I'm disgusted!"
            return
        else:
            if inpt == "1":
                if mainCharacter.money < 55:
                    print "What! You don't have enough money! Cheapskate! you only have", mainCharacter.money, "money! Don't try to be all smart with me! I'm too smart for you!"
                    return
                else:
                    potion = Healthpotion()
                    mainCharacter.money = mainCharacter.money - Healthpotion.cost


            if inpt == "2":
                if mainCharacter.money < 50:
                    print "What! You don't have enough money! Cheapskate! you only have", mainCharacter.money, "money! Don't try to be all smart with me! I'm too smart for you!"
                    return
                else:
                    potion = Manapotion()
                    mainCharacter.money = mainCharacter.money - Manapotion.cost

            if inpt == "3":
                if mainCharacter.money < 15:
                    print "What! You don't have enough money! Cheapskate! you only have", mainCharacter.money, "money! Don't try to be all smart with me! I'm too smart for you!"
                    return
                else:
                    potion = Suicidepotion()
                    mainCharacter.money = mainCharacter.money - Suicidepotion.cost

            inpt = raw_input ('Would you like to buy this?\n')
            if inpt == "yes" or inpt == "Yes":
                if mainCharacter.Inventory.Addtobag(potion):
                    print "Your new potion has been placed in your inventory. Just dont kill yourself!"
                else:
                    print "You don't have enough space! Wackjob"
                print "Thanks, come again!"
            else:
                print "really?"
                return
class WeaponShop:
    def __init__(self):
        print mainCharacter.city.name, "weapon shop:"
        print "Welcome to the weapon shop"
        index = 1
        for weapon in mainCharacter.city.weapons:
            print index, 
            print weapon.name, "$",weapon.cost
            index = index + 1

        item = None 
        inpt = raw_input('What would you like to buy?\n')
        if inpt == "none" or inpt == "None":
            print "Then why did you come here? Get out! I'm disgusted!"
            return
        inpt = int(inpt)
        item = mainCharacter.city.weapons[inpt - 1]
        if mainCharacter.money < item.cost:
            print "you don't have enough money to buy that weapon!"
        else:
            if mainCharacter.Inventory.Addtobag(item):
                print "Your new weapon has been placed in your Inventory, make sure to equip it!"
                mainCharacter.money = mainCharacter.money - item.cost
            else: 
                print "You don't have enough space!"

            print "Thanks, come again!"
            print "This item cost", item.cost, "dollars"
class Inventory:
    bag = {1: None, 2: None,3: None,4: None,5: None,6: None,7: None,8: None,9: None,10: None,11: None,12: None,13: None,13: None,14: None,15: None}
    def Addtobag(self, item):
        for slot in self.bag:
            if self.bag[slot] == None:
                self.bag[slot] = item
                return True
            else:
                print "Wah, wah, wah..."
        return False
            
    def Openbag(self):
        for key in self.bag:
            print key
            print self.bag[key].__class__.__name__
        inpt = raw_input("What item would you like to take from your endless bag of junk: ")
        key = int(inpt)
        if self.bag[key] == Manapotion:
            Manapotion.equip()
        elif self.bag[key] == Healthpotion:
            Healthpotion.equip()
        elif self.bag[key] == Suicidepotion:
            Suicidepotion.equip()
        elif self.bag[key] != None:
            self.bag[key].equip(key)
        elif inpt == "":
            print "Pick again! There's no item in that spot!"
        else:
            print "Pick again! There's no item in that spot!"
        
class Potion:
    def equip(self, key):
        pass 

class Manapotion(Potion):
    cost = 50
    def equip(self, key):
        mainCharacter.mana = mainCharacter.mana + 100
        Inventory.bag[key] = None

class Healthpotion(Potion):
    cost = 55
    def equip(self, key):
        mainCharacter.health = mainCharacter.health + 100
        Inventory.bag[key] = None

class Suicidepotion():
    cost = 15
    def equip(self, key):
        inpt = raw_input ('would you like to die?\n 1. Yes\n 2. No\n')
        if inpt == "yes" or inpt == "1":
            while True:
                inpt = raw_input ('you Died!!!Please exit TERMINAL and come back to play again')
        if inpt == "no" or inpt == "2":
            print "I'm glad you didn't kill yourself!"

class Armor():
    impactpower = 0
    cost = 0
    def equip(self, key):
        mainCharacter.equip(self)

class Helmet(Armor):
    impactpower = 10
    cost = 30
    name = "Helmet"

class Chestpiece(Armor):
    impactpower = 7
    cost = 30
    name = "Chestpiece"

class Weapon:
    crit = 0
    cost = 0
    name = "Nothing yet"
    damage = 0      
    def equip(self, key):
        mainCharacter.equip(self)
class titaniumElectricSpear(Weapon):
    damage = 140
    cost = 205
    crit = 5
    name = "Titanium Electric Spear"
class silverPoisonDoubleSidedAxe(Weapon):
    damage = 135
    cost = 200
    crit = 5
    name = "Silver Poison Double Sided Axe"
class LongSword(Weapon):
    damage = 50
    cost = 50
    crit = 10
    name = "Longsword"

class flamingBaseball(Weapon):
    damage = 80
    cost = 120
    crit = 8
    name = "Flaming Baseball"

class atomicSpinner(Weapon):
    damage = 250
    cost = 450
    crit = 10
    name = "Atomic Spinner"

class Bow(Weapon):
    damage = 75
    cost = 80
    crit = 1
    name = "Bow"

class lightningBolt(Weapon):
    damage = 250
    cost = 450
    crit = 20
    name = "Lightning Bolt"

class machineGun(Weapon):
    damage = 150
    cost = 200
    crit = 1/2
    name = "Machine Gun"

class lightSaber(Weapon):
    damage = 190
    cost = 265
    crit = 15
    name = "Light Saber"

class guildedRapier(Weapon):
    damage = 150
    cost = 200
    crit = 25
    name = "Guilded Rapier"

class jadedPoisonDagger(Weapon):
    damage = 200
    cost = 275
    crit = 1
    name = "Jaded Posion Dagger"
class goldMinigun(Weapon):
    damage = 150
    cost = 200
    crit = 5
    name = "Gold Minigun"
class uraniumScythe(Weapon):
    damage = 175
    cost = 225
    crit = 10
    name = "Uranium Scythe"
class GoldenRetriever():
    damage = 15
    cuteness = 14
    cost = 75
class germanShepard():
    damage = 20
    cuteness = 15
    cost = 97
class belgianMalinios():
    damage = 25
    cuteness = 15
    cost = 100
class Battle:
    def chooseEnemy(self, allEnemies):
        enemyNum = 0
        index = 1         
        for enemy in allEnemies:
            print index,
            print enemy.__class__.__name__, enemy.health
            index = index + 1

        enemyNum = raw_input("What enemey(s) would you like to fight? Enter a number based on the info from above:\n")

        try:
            enemyNum = int(enemyNum)
        except:
            print "Incorrect Input - Defaulting to Enemy No. 1"
            return allEnemies[0]
        return allEnemies[enemyNum - 1]

    def __init__(self):
        print "FIGHT!"
        inpt = raw_input ('what would you like to do:\n1.fight\n2.run\n')
        if inpt == "fight" or inpt == "1":
            list = []
            numen = random.randint(6, 6)
            index = 0
            while index < numen:
                enmy = random.randint(1, 3)
                if enmy == 1:
                    list.append(Barbarian())
                elif enmy == 2:
                    list.append(Zombie())
                elif enmy == 3:
                    list.append(Dragon())
                elif enmy == 4:
                    list.append(Barbarian())
                elif enmy == 5:
                    list.append(Zombie())
                elif enmy == 6:
                    list.append(Zombie())

                index = index + 1

    
                    
            while len(list) > 0:
                #Your attack phase
                inpt = raw_input ('1. attack\n2. use special move\n3. Open Bag\n4. flee\n')


                if inpt == "1":
                    mainCharacter.attack(self.chooseEnemy(list))
                elif inpt =="2":
                    if isinstance(mainCharacter, Knight):
                        mainCharacter.specialMove(list)
                    elif isinstance(mainCharacter, Werewolf):
                        mainCharacter.specialMove()
                    elif isinstance(mainCharacter, Rogue):
                        mainCharacter.specialMove(self.chooseEnemy(list))
                elif inpt =="3":
                    mainCharacter.Inventory.Openbag()
                elif inpt == "4":
                    if mainCharacter.weapon != None:
                        print "your stats are:\nhealth = ", mainCharacter.health, "\nmana = ", mainCharacter.mana, "\nmoney = ", mainCharacter.money, "\ndamage = ", mainCharacter.weapon.damage, "\nYou are a coward! You fled! Come back and face your destiny!"
                    else:
                        print "your stats are:\nhealth = ", mainCharacter.health, "\nmana = ", mainCharacter.mana, "\nmoney = ", mainCharacter.money, "\ndamage = ", mainCharacter.damage, "\nYou are a coward! You fled! Come back and face your destiny!"

                    return


                   
                #Enemy attack phase
                for enemy in list:
                    if enemy.health <= 0:
                        list.remove(enemy)
                        mainCharacter.money = mainCharacter.money + 10
                        print "Enemy Defeated! You have gained 10 money to be greedy with. Just remember you're still poor!"
                for enemy in list:
                    inpt = raw_input ('The %s is about to attack you. What would you like to do:\n1.dodge\n2.block\n3.parry\n'%enemy.name)
                    if inpt == "dodge" or inpt == "1":
                        if mainCharacter.dodge() == False:
                            enemy.attack(mainCharacter)

                    elif inpt == "block" or inpt == "2":
                        if mainCharacter.block() == False:
                            enemy.attack(mainCharacter)
                    elif inpt == "parry" or inpt == "3":
                        if mainCharacter.parry() == False:
                            enemy.attack(mainCharacter)
                    else:
                        print "check your spelling"
        if isinstance(mainCharacter, Werewolf):
            if mainCharacter.werewolfMode == True:
                mainCharacter.untransform()
        if isinstance(mainCharacter, Rogue):
            if mainCharacter.rogueMode == True:
                mainCharacter.untransform()


class Enemy:
    health = 1
    damage = 20
    name = "Your name here"
    def attack(self, enemy):
        totaldamage = self.damage
        if enemy.chestpiece != None:
            totaldamage = totaldamage - enemy.chestpiece.impactpower
        if enemy.helmet != None:
            totaldamage = totaldamage - enemy.helmet.impactpower
        enemy.health = enemy.health - totaldamage
        print "Your foe dealt %d damage" % totaldamage
      
class Zombie(Enemy):
    health = 100
    damage = 15
    name = "Zombie"
    def __init__(self):
        print "I am a Zombie!! I will eat your brains!!!"
class Barbarian(Enemy):
    health = 300
    damage = 20
    name = "Barbarian"
    def __init__(self):
        print "Tremble before the mighty power of a Barbarian!!!"
class Dragon(Enemy):
    health = 500
    damage = 40
    name = "Dragon"
    def __init__(self):
        print "I will claw you to shreds and roast you with fire. I am a dragon!"
        
class Character():
    dodgeChance = 50
    blockChance = 50
    health = 200
    city = Boston()
    money = 200
    potion = None
    weapon = None
    chestpiece = None
    helmet = None
    mana = 100 
    damage = 5
    Inventory = Inventory()
    def stash(self, item):
        self.Inventory.Addtobag(item)
    def dodge(self):
        if random.randint(1,6) >3:
            print "Successful dodge!"
            return True
        else:
            print "Unsuccesful dodge"
            return False
    def parry(self):
        if random.randint(1,6) >3:
            print "Successful parry!"
            return True
        else:
            print "Unsuccesful parry"
            return False
    def block(self):
        if random.randint(1,6) >3:
            print "Successful block!"
            return True
        else:
            print "Unsuccesful block"
            return False
    def attack(self, enemy):
        if self.weapon == None:
            enemy.health = enemy.health - self.damage
            print "you dealt %d damage" % self.damage
        else:
            enemy.health = enemy.health - self.weapon.damage
            print "you dealt %d weapon damage" % self.weapon.damage
    def setCity(self, city):
        self.city = city
    def getCity():
        print self.city.name 
    def equip(self, equipment):

        if isinstance(equipment, Armor):
            
            if isinstance(equipment, Helmet):
                self.helmet = equipment 

            if isinstance(equipment, Chestpiece):
                self.chestpiece = equipment

        if isinstance(equipment, Weapon):
            self.weapon = equipment


        print "you equiped the %s" %equipment.name
    #We want to to use this method to make sure our code works.
    #it should show off the weapon we bought OR
    #nothing at all
    def showOff(self):
        if self.weapon == None:
            print "Oh shoot, I don't even have a weapon!"
        else:
            print "Ha! Ha! Check out my cool", self.weapon.name

        if self.chestpiece == None:
            print "Oh shoot, I dont even have a chestpiece!"
        else:
            print "Ha! Ha! Check out my cool", self.chestpiece.name


        if self.helmet == None:
            print "Oh shoot, I dont even have a helmet!"
        else:
            print "Ha! Ha! Check out my cool", self.helmet.name
    
    def store(self):
        print "It costs 50 bucks to open a store."
        mainCharacter.money = mainCharacter.money - 50
        while mainCharacter.money <=30:
            print "a customer has bought something in your store. You get 10 money"
            mainCharacter.money = mainCharacter.money + 50
          
    def masterWizard(self):
        inpt = raw_input ('Hello, little one. I can help you with these things:\n 1. go to a nice restaurant\n 2. Open a store to get money\n 3. Buy a dog\n Which would you like to do?\n')
        if inpt == "none" or inpt == "None":
            pass
        elif inpt == "1":
            inpt = raw_input('Which restaurant would you like to go to:\n 1. Masa, New York City ($75)\n 2. SubliMotion, Spain ($100)\n 3. Restaurant Crissier, Switzerland ($80)\n4. Cheap Meal($15)\n')
            if inpt == "1":
                mainCharacter.money = mainCharacter.money - 75
                print "you are dining most exquisitly on \"Masa\" food. Your health is now +40"
                mainCharacter.health = mainCharacter.health + 40
            elif inpt == "2":
                mainCharacter.money = mainCharacter.money - 100
                print "you are dining most exquisitly on \"SubliMotion\" food. Your health is now +60"
                mainCharacter.health = mainCharacter.health + 60
            elif inpt == "3":
                mainCharacter.money = mainCharacter.money - 80
                print "you are dining most exquisitly on \"Crissier\" food. Your health is now +50"
                mainCharacter.health = mainCharacter.health + 50
            elif inpt == "4":
                mainCharacter.money = mainCharacter.money - 15
                print "You are dining on cheap crap food! you have gained +15 health"
                mainCharacter.health = mainCharacter.health + 15
        elif inpt == "2":
            print "you have opened a store. Every time a customer comes in and buys something, you will get money!"
            mainCharacter.store()
        elif inpt == "3":
            inpt = raw_input('which dog would you like to buy?\n1.German Shepard($97)\n2.Belgian Malinios($100)\n3.Golden Retriever($75)\n')
            if inpt == "1":
                if mainCharacter.money > GoldenRetriever.cost:
                    if mainCharacter.weapon == None:
                        mainCharacter.damage = mainCharacter.damage + germanShepard.damage
                    else:
                        mainCharacter.weapon.damage = mainCharacter.weapon.damage + germanShepard.damage
                    mainCharacter.money = mainCharacter.money - 97
                else:
                    return
                    print "you don't have enough money to buy that dog"
            elif inpt == "2":
                if mainCharacter.money > GoldenRetriever.cost:
                    if mainCharacter.weapon == None:
                        mainCharacter.damage = mainCharacter.damage + belgianMalinios.damage
                    else:
                        mainCharacter.weapon.damage = mainCharacter.weapon.damage + belgianMalinios.damage
                    mainCharacter.money = mainCharacter.money - 100
                else:
                    return
                    print "you don't have enough money to buy that dog"
            elif inpt == "3":
                if mainCharacter.money > GoldenRetriever.cost:
                    if mainCharacter.weapon == None:
                        mainCharacter.damage = mainCharacter.damage + GoldenRetriever.damage
                    else:
                        mainCharacter.weapon.damage = mainCharacter.weapon.damage + GoldenRetriever.damage
                    mainCharacter.money = mainCharacter.money - 75
                else:
                    return
                    print "you don't have enough money to buy that dog"
            print "Your dog is very cute! And ferocious! And now, you and your dog share damage!"




    def Home(self):
        inpt = raw_input('What would you like to do?\n 1. sleep\n 2. book a flight\n 3. exercise\n')
        if inpt == "1":
            while True:
                inpt = raw_input ('zzzzzzzzzzzzz. You are snoring away! Every time you sleep, you gain 3 health. \nWould you like to\n 1.wake up \n 2.wait\n')
                if inpt == "1":
                    print "wha, wha, what??? Why'd you wake me up?"
                    mainCharacter.health = mainCharacter.health + 3
                    break
                elif inpt == "2":
                    continue
        elif inpt == "2":
            inpt = raw_input('here are the flights available:\n1. Gabrieapolis($50)\n2. Zschorlau($50)\n3. Fidgura($50)\n4. Boston($50)\n')
            if inpt == "1":
                print "Ok. Boarding... You have arrived!"
                self.city = Gabrieapolis()
            elif inpt == "2":
                print "Ok. Boarding... You have arrived!"
                self.city = Zschorlau()
            elif inpt == "3":
                print "Ok. Boarding... You have arrived!"
                self.city = Fidgura()
            elif inpt == "4":
                print "Ok. Boarding... You have arrived!"
                self.city = Boston()

            self.money = self.money - 50

        elif inpt == "3":
            print "walking to the gym... Ok, You are breaking a sweat. Doing pull-ups... Doing push-ups... Running on the treadmill... Exercise complete! Your muscles are looking mighty big. You have gained + 2 damage"
            if mainCharacter.weapon == None:
                mainCharacter.damage = mainCharacter.damage + 2
            else:
                mainCharacter.weapon.damage = mainCharacter.weapon.damage + 2
class Devil(Character):
    name = "Devil"
    

class Knight(Character):
    name = "Piercer"
    def specialMove(self, allEnemies):
        if mainCharacter.mana <15:
            print "you don't have enough mana!"
            return
        elif mainCharacter.mana >15:
            mainCharacter.mana = mainCharacter.mana - 15
            if random.randint(1,6) >=3:
                for enemy in allEnemies: 
                    enemy.health = enemy.health - 100
                    print "you dealt %d damage" % 100 
            else:
                print "you failed your special move!!!"
class Rogue(Character):
    name = "Altair"
    tempWeapon = None
    rogueMode = False
    def specialMove(self, enemy):
        if mainCharacter.mana <15:
            print "you don't have enough mana!"
            return
        elif mainCharacter.mana >15:
            mainCharacter.mana = mainCharacter.mana - 15
            if random.randint(1,6) >=3:
                enemy.damage = 0
                print "Now you have transformed into a rogue that prevents your enemies from doing any damage"
            else:
                print "you failed your special move!!!"

    def untransform(self):
        self.damage = 5
        self.weapon = self.tempWeapon
        self.rogueMode = False
        print "You have untransformed back into your sneaky, lying, backstabbing self!!!"

class Werewolf(Character): 
    name = "Wolverine"
    tempWeapon = None
    werewolfMode = False

    def specialMove(self):
        if mainCharacter.mana <15:
            print "you don't have enough mana!"
            return 
        elif mainCharacter.mana >15:
            mainCharacter.mana = mainCharacter.mana - 15
            if random.randint(1,6) >=3:

                print "You have transformed into a scary werewolf! Now your attack power is 100 damage!"
                self.damage = 150
                self.tempWeapon = self.weapon
                self.weapon = None

                self.werewolfMode = True

    def untransform(self):
        self.damage = 5
        self.weapon = self.tempWeapon
        self.werewolfMode = False
        print "You have untransformed back into your sneaky, lying, backstabbing self!!!"

################GAME STARTS HERE################

mainCharacter = None
inpt = raw_input('type the number or word of the main character you choose :\n1. knight\n2. werewolf\n3. rogue\n')

if inpt == "knight" or inpt == "1" or inpt == "Knight":
    mainCharacter = Knight()
    print "you have choosen the path of the knight, the bravest of the trisquod. Green blob zombies are attacking Manhattan. Get help from the master wizard. Fight the zombies, or Humanity will be destroyed. If you want to know how much money, health, mana... you have, type \"show stats\". When you buy a weapon, go to the inventory and type the number of that weapon to equip it. If you go to a store, but don't want to buy anything, type \'None\' or \'none\'. You start off with 200 money and 150 health. Good Luck!"
if inpt == "Werewolf" or inpt == "werewolf" or inpt == "2":
    print "you have chosen the path of the werewolf, the strongest and most vicious of the trisquod. Green blob zombies are attacking Manhattan. Get help from the master wizard. Fight the zombies, or Humanity will be destroyed. If you want to know how much money, health, mana... you have, type \"show stats\". When you buy a weapon, go to the inventory and type the number of that weapon to equip it. If you go to a store, but don't want to buy anything, type \'None\' or \'none\'. You start off with 200 money and 150 health. Good Luck!"
    mainCharacter = Werewolf()
if inpt == "Rogue" or inpt == "rogue" or inpt == "3":
    mainCharacter = Rogue()
    print "you have chosen the path of the rogue, the most tactical and stealthy of the trisquod. Green blob zombies are attacking Manhattan. Get help from the master wizard. Fight the zombies, or Humanity will be destroyed. If you want to know how much money, health, mana... you have, type \"show stats\". When you buy a weapon, go to the inventory and type the number of that weapon to equip it. If you go to a store, but don't want to buy anything, type \'None\' or \'none\'. You start off with 200 money and 150 health. Good Luck!"


mainCharacter.setCity(Boston())



 
while True:
    inpt = raw_input ("Menu\n  1.go to shops\n  2.show off\n  3.fight\n  4.Inventory\n  5.Visit Master wizard\n  6.Go home\n  7.Change character\n")    
    if inpt == "go to" or inpt == "1": 
        #print startingCity.shops
        inpt = raw_input ("Type your store name here \n1.potion\n2.weapon\n ")
        
        if inpt == "potion" or inpt == "potion shop" or inpt == "1":
            potionShop = PotionShop()    
        elif inpt == "weapon" or inpt == "weapon shop" or inpt == "2":
            weaponShop = WeaponShop()
        elif inpt == "3":
            dogStore = dogStore()
    elif inpt == "show off" or inpt == "2": 
        mainCharacter.showOff()
    elif inpt == "fight" or inpt == "3":
        battle = Battle()
    elif inpt == "Inventory" or inpt == "4":
        mainCharacter.Inventory.Openbag()
    elif inpt == "5" or inpt == "Visit Master wizard":
        mainCharacter.masterWizard()
    elif inpt == "6":
        mainCharacter.Home()
    elif inpt == "7":
        inpt = raw_input('which character would you like to be\n1. Knight\n2. Werewolf\n3. Rogue\n')
        if inpt == "1":
            mainCharacter = Knight()
            print "you have choosen the path of the knight, the bravest and most couragous of the trisquod. Green blob zombies are attacking Manhattan. Get help from the master wizard. Fight the zombies, or Humanity will be destroyed. If you want to know how much money, health, mana... you have, type \"show stats\""
        if inpt == "2":
            mainCharacter = Werewolf()
            print "you have chosen the path of the werewolf, the strongest and most vicious of the trisquod. Green blob zombies are attacking Manhattan. Get help from the master wizard. Fight the zombies, or Humanity will be destroyed. If you want to know how much money, health, mana... you have, type \"show stats\""
        if inpt == "3":
            mainCharacter = Rogue()
            print "you have chosen the path of the rogue, the most tactical and stealthy of the trisquod. Green blob zombies are attacking Manhattan. Get help from the master wizard. Fight the zombies, or Humanity will be destroyed. If you want to know how much money, health, mana... you have, type \"show stats\""
    
    elif inpt == "show stats":
        if mainCharacter.weapon == None:
            print "health = ", mainCharacter.health,"\nmoney = ", mainCharacter.money, "\nmana = ", mainCharacter.mana, "\nwhere you are = ", mainCharacter.city.name,  "\ndamage = ", mainCharacter.damage
        else:
            print "health = ", mainCharacter.health,"\nmoney = ", mainCharacter.money, "\nmana = ", mainCharacter.mana, "\nyour weapons = ", mainCharacter.weapon.name, "\nwhere you are = ", mainCharacter.city.name,  "\ndamage = ", mainCharacter.weapon.damage
    elif inpt == "potions":
        inpt = raw_input ('here are your potions; which would you like to use:\n1.Healthpotion\n2.Manapotion\n3.Suicidepotion\n4.Money\n')
        if inpt == "1":
            mainCharacter.health = mainCharacter.health + 100
        elif inpt == "2":
            mainCharacter.mana = mainCharacter.mana + 100
        elif inpt == "3":
            inpt = raw_input ('are you sure you want to die: all your scores will be lost?\n')
            if inpt == "yes":
                while True:
                    x = raw_input ('YOU DIED! EXIT TERMINAL AND COME BACK TO PLAY AGAIN!')
            elif inpt == "no":
                continue
        elif inpt == "4":
            mainCharacter.money = mainCharacter.money + 5000
        elif inpt == "5":
            mainCharacter.health = mainCharacter.health - 89
        elif inpt == "6":
            mainCharacter.money = mainCharacter.money - 220

    if mainCharacter.mana > 201:
        if random.randint(1, 2) < 1:
            inpt = raw_input('There is a special deal for a health potion in the city of Gabrieapolis. It is only 50 mana and no money! Would you like to\n1. Go there and buy\n2. Stay and miss out\n')
            if inpt == "1":
                mainCharacter.city = Gabrieapolis()
                print "You have traveled to Gabrieapolis for free and have gotten +50 health\n"
                print "Nice negotiating! You have earned a inexpensive Health Potion!"
                mainCharacter.health = mainCharacter.health + 50
                mainCharacter.mana = mainCharacter.mana - 50
            else:
                print "Too bad, loser!"
        else:
            inpt = raw_input('There is a special deal for a atomic spinner potion in the city of Fidgura. It is only 100 mana and no money! Would you like to\n1. Go there and buy\n2. Stay and miss out\n')
            if inpt == "1":
                if mainCharacter.weapon == None:
                    mainCharacter.city = Fidgura()
                    mainCharacter.weapon = atomicSpinner
                    mainCharacter.damage = 250
                    mainCharacter.mana = mainCharacter.mana - 100
                    print "You have traveled to Fidgura for free and gotten a new weapon!"
                    print "Nice negotiating! You have earned a inexpensive atomic spinner!"
                else:
                    mainCharacter.damage = 250
                    mainCharacter.city = Fidgura()
                    mainCharacter.weapon = atomicSpinner
                    mainCharacter.mana = mainCharacter.mana - 100
                    print "You have traveled to Fidgura for free and gotten a new weapon!"
                    print "Nice negotiating! You have earned a inexpensive atomic spinner!"                    
            else:
                print "Too bad, loser!"


    elif inpt == "":
        print "What's the matter with you, spell it right!!!"
    if mainCharacter.health <=0:
        while True:
            x = raw_input ('YOU DIED! EXIT TERMINAL AND COME BACK TO PLAY AGAIN!')

#list of things that we want to do:
#1.break up the code into several files to make it easier to orginize
#2.turn potions into classes (class potion)
#3.give different classes special moves
#4.add sound effects
#5.create and actual story line  
# DaGame_py