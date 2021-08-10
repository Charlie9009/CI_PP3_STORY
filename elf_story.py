from character import name, hero_data
from gmail_sheet import update_sheet_ending_1, update_sheet_ending_2

def elfPath0():
    """
    Function to display the intro of the story
    and present the user with two path options by using to integers.
    """
    pathChoice = int(input("1\n"))
    if pathChoice == 1:
        elfPath1()
        
    return pathChoice


def elfPath1():
    """
    Function to display the first path choice of intro
    and present the user with three new options by using three integers.
    A while loop is also added to loop one of these choices.
    """
    with open('stories/elf/elf_path1.txt') as f:
            path1 = f.read()
            print(path1.format(name))
    while True:
        print("What will you do?")
        print("1. Light the torch by scraping two rocks together")
        print("2. Don't light the torch and keep walking")
        secondPathChoice = int(input("1, 2\n"))
        if secondPathChoice == 1:
            elfPath1_1()
            break
        elif secondPathChoice == 2:
            elfPath1_2()



def elfPath1_1():
    """
    Function to display the second path choice of path1
    and present the user with two new options by using two integers.
    """
    with open('stories/elf/elf_path1_1.txt') as f:
            path1_1 = f.read()
            print(path1_1.format(name))
    print("1. Talk to the ogre")
    print("2. Sneak around the ogre")
    thirdPathChoice = int(input("1, 2\n"))
    if thirdPathChoice == 1:
        elfBattle()
    elif thirdPathChoice == 2:
        elfPath1_1_2()
        
    return thirdPathChoice


def elfBattle():
    print("The ogre wakes up and starts running at you.")
    print("What will you do?")
    print("1. Offer your gold neckless to the ogre")
    print("2. Attack the ogre")
    battleChoice = int(input("1, 2\n"))
    if battleChoice == 1:
        battlePath1()
    elif battleChoice == 2:
        battlePath2()



def battlePath1():
    print("As the ogre charges at you, you offer it your gold neckless.")
    print("The ogre stops in it's tracks and looks at it with awe.")
    print("- Wooow not one person has offered me gold in centuries. The ogre said.")
    print("- You are free to pass. He said")
    elfPath1_1_1()



def battlePath2():
    print("As the ogre charges at you, you jump to get out of the way.")
    print("The ogre catches you mid air, and slams you in to the wall.")
    print(f"Your health is now {hero_data[0] - 25}")
    print("You are dead.")



def elfPath1_1_1():
    """
    Function to display the first path choice of path1_2
    and present the user with two new options by using two integers.
    A while loop is also added to loop one of these choices.
    """
    with open('stories/elf/elf_path1_1_1.txt') as f:
            path1_1_1 = f.read()
            print(path1_1_1.format(name))
    while True:
        print("What will you do?")
        print("1. Collect courage")
        print("2. Jump down")
        fourthPathChoice = int(input("1, 2\n"))
        if fourthPathChoice == 1:
            print("You collected courage")
        elif fourthPathChoice == 2:
            elfPath1_1_1_2()
            break



def elfPath1_1_2():
    """
    Function to display the second path choice of path1_2
    and to end the game.
    """
    with open('stories/elf/elf_path1_1_2.txt') as f:
            path1_1_2 = f.read()
            print(path1_1_2.format(name))



def elfPath1_1_1_2():
    """
    Function to display the second path choice of path1_2_1
    and present the user with two new options by using two integers.
    Code is added to send back information to google sheet when users finish the game.
    """
    with open('stories/elf/elf_path1_1_1_2.txt') as f:
            path1_1_1_2 = f.read()
            print(path1_1_1_2.format(name))
    print("1. Take the Caldun")
    print("2. Leave")
    fifthPathChoice = int(input("1, 2\n"))
    if fifthPathChoice == 1:
        """
        Get the value for path1 cell from the worksheet, turn it to an int so it can be incremented by 1
        Send it back to update the sheet  
        """
        update_sheet_ending_1()

        with open('stories/elf/elf_end_1.txt') as f:
            end1 = f.read()
            print(end1.format(name))
    elif fifthPathChoice == 2:
        """
        Get the value for path2 cell from the worksheet, turn it to an int so it can be incremented by 1
        Send it back to update the sheet  
        """
        update_sheet_ending_2()

        with open('stories/elf/elf_end_2.txt') as f:
            end2 = f.read()
            print(end2.format(name))



def elfPath1_2():
    """
    Function to display the second path choice of path1
    and to loop the game.
    """
    with open('stories/elf/elf_path1_2.txt') as f:
            path1_2 = f.read()
            print(path1_2.format(name))