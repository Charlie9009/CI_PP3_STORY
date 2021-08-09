from pprint import pprint

class character:

    def __init__(self, health, mana, mind, name):
        self.health = health
        self.mana = mana
        self.mind = mind
        self.name = name

def choseClass():
    print("1. Wizard/ 2. Warrior/ 3. Elf")
    characterSelect = int(input("1/2/3\n"))
    if characterSelect == 1:
        health = 50
        mana = 100
        mind = 50
    elif characterSelect == 2:
        health = 100
        mana = 25
        mind = 50
    elif characterSelect == 3:
        health = 25
        mana = 50
        mind = 100

    name = input("What is your name?\n")

    return(health, mana, mind, name)
        


