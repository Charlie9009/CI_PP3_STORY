from pprint import pprint


NAME = input("What is your name?\n")
print("Are you a Wizard, Warrior or an elf?")
print("1. Wizard/ 2. Warrior/ 3. Elf")
characterSelect = int(input("1/2/3\n"))


class character:

    def __init__(self, health, mana, mind):
        self.health = health
        self.mana = mana
        self.mind = mind


def choseClass():
    """
    Create dictionaries containing clothes for classes.
    Add if/else to print out different classes depending on user choice.
    Set health, mana and mind for different classes and return it.
    """
    wizardClothes = {
        "head": "A blue pointy hat",
        "torso": "A red cape",
        "legs": "Blue pants",
        "feet": "Red pointy shoes"
    }
    warriorClothes = {
        "head": "A metal helmet",
        "torso": "A big armor",
        "legs": "Armored pants",
        "feet": "Armored boots"
    }
    elfClothes = {
        "head": "Beautiful hair",
        "torso": "A red silk shirt",
        "legs": "Red silk pants",
        "feet": "Black smooth shoes"
    }
    if characterSelect == 1:
        # Wizard choice
        health = 50
        mana = 100
        mind = 50

        print("You have chosen Wizard, your clothes are...")
        for wizard in wizardClothes:
            print(wizardClothes[wizard])

    elif characterSelect == 2:
        # Warrior choice
        health = 100
        mana = 25
        mind = 50

        print("You have chosen Warrior, your clothes are...")
        for warrior in warriorClothes:
            print(warriorClothes[warrior])

    elif characterSelect == 3:
        # Elf choice
        health = 25
        mana = 50
        mind = 100

        print("You have chosen Elf, your clothes are...")
        for elf in elfClothes:
            print(elfClothes[elf])

    return(health, mana, mind)

hero_data = choseClass()
hero = character(hero_data[0], hero_data[1], hero_data[2])
print("Your stats are...")
pprint(vars(hero))


class enemy:
    """
    Declare class of enemy.
    """
    def __init__(self, health):
        self.health = health


def ogreHealth():
    """
    Set ogre health and return it.
    """
    health = 100

    return health

ogre_data = ogreHealth()
