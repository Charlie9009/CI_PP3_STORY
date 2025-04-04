from pprint import pprint

# First choices for user
NAME = input("What is your name?\n")
print("Are you a Wizard, Warrior or an elf?")
print("1. Wizard/ 2. Warrior/ 3. Elf")
CHARACTERSELECT = input("1, 2, 3\n")
# Input validation
while CHARACTERSELECT != "1" and CHARACTERSELECT != "2" and CHARACTERSELECT != "3":
    print("Invalid input")
    CHARACTERSELECT = input("1, 2, 3\n")


class character:
    """
    Contains functions to set health, mana and mind,
    Also printing out selected character stats.
    This part was inspired from "Advanced Python Text Adventure"
    and addapted to my needs
    """
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
    """
    This part was inspired from "Advanced Python Text Adventure"
    and addapted to my needs
    """
    if CHARACTERSELECT == "1":
        # Wizard choice
        health = 50
        mana = 100
        mind = 50
        # My code
        clothes = wizardClothes
        print("You have chosen Wizard, your clothes are...")
        """
        This part was inspired from "Advanced Python Text Adventure"
        and addapted to my needs
        """
    elif CHARACTERSELECT == "2":
        # Warrior choice
        health = 100
        mana = 25
        mind = 50
        # My code
        clothes = warriorClothes
        print("You have chosen Warrior, your clothes are...")
        """
        This part was inspired from "Advanced Python Text Adventure"
        and addapted to my needs
        """
    elif CHARACTERSELECT == "3":
        # Elf choice
        health = 25
        mana = 50
        mind = 100
        # My code
        clothes = elfClothes
        print("You have chosen Elf, your clothes are...")

    for item in clothes.values():
        print(item)

    return(health, mana, mind)

"""
This part was inspired from "Advanced Python Text Adventure"
and addapted to my needs
Apply function to variable and print stats.
"""
hero_data = choseClass()
hero = character(hero_data[0], hero_data[1], hero_data[2])
print("Your stats are...")
print(f"Health: {hero.health}")
print(f"Mana: {hero.mana}")
print(f"Mind: {hero.mind}")



class enemy:
    """
    Declare class of enemy.
    My code.
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
