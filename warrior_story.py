from character import name, hero_data, ogre_data
from gmail_sheet import update_sheet_ending_1, update_sheet_ending_2
from validation import validate_warrior_path0, validate_user_input

def warriorPath0():
    """
    Function to display the intro of the story
    and present the user with two path options by using to integers.
    """
    if validate_warrior_path0() == 1:
        warriorPath1()


def warriorPath1():
    """
    Function to display the first path choice of intro
    and present the user with three new options by using three integers.
    A while loop is also added to loop one of these choices.
    """
    with open('stories/warrior/warrior_path1.txt') as f:
            path1 = f.read()
            print(path1.format(name))
    while True:
        print("What will you do?")
        print("1. Don't light the torch and keep walking")
        print("2. Light the torch with magic")
        secondPathChoice = input(int("1, 2\n"))
        if secondPathChoice == 1:
            validate_user_input()
            warriorPath1_1()
            break
        elif secondPathChoice == 2:
            validate_user_input()
            warriorPath1_2()




def warriorPath1_1():
    """
    Function to display the second path choice of path1
    and present the user with two new options by using two integers.
    """
    with open('stories/warrior/warrior_path1_1.txt') as f:
            path1_1 = f.read()
            print(path1_1.format(name))
    while True:
        print("1. Attack the ogre")
        print("2. Sneak around the ogre")
        thirdPathChoice = int(input("1, 2\n"))
        if thirdPathChoice == 1:
            warriorBattle()
            break
        elif thirdPathChoice == 2:
            warriorPath1_1_2()


def warriorBattle():
    print("The ogre starts running at you.")
    print("What will you do?")
    print("1. Pick up a big rock and throw it at the ogre")
    print("2. Jump out of the way")
    battleChoice = int(input("1, 2\n"))
    if battleChoice == 1:
        battlePath1()
    elif battleChoice == 2:
        battlePath2()



def battlePath1():
    print("Your throw a rock at the ogre hitting it in the head.")
    print(f"The ogres health is now {ogre_data - 50}")
    print("The ogre swings it's arm and hits you barely knocking you back.")
    print(f"Your health is now {hero_data[0] - 10}")
    print("What will you do?")
    print("1. Wait for ogre to make the next move")
    print("2. Charge at the ogre")
    battleChoice = int(input("1, 2\n"))
    if battleChoice == 1:
        battlePath1_1()
    elif battleChoice == 2:
        battlePath1_2()


def battlePath1_1():
    print("Before you can react the ogre runs at you pushing you in to the wall.")
    print(f"Your health is now {hero_data[0] - 60}")
    print("As you are trapped between the wall and the ogre you manage to punch the ogre in the face.")
    print(f"The ogres health is now {ogre_data - 100}")
    print("The ogre is dead")
    warriorPath1_1_1()


def battlePath1_2():
    print("You charge the ogre with full force.")
    print("You smash into the ogre and with the warrior strength the ogres feet leaves the ground")
    print("You push the ogre straight into the cave wall and as the ogre smashes in to it it collapses on the ground")
    print(f"The ogres health is now {ogre_data - 100}")
    print("The ogre is dead")
    print(f"Your health is now {hero_data[0] - 80}")
    warriorPath1_1_1()

def battlePath2():
    print("As the ogre charges at you, you jump to get out of the way.")
    print("The ogre catches you mid air, and slams you in to the wall.")
    print(f"Your health is now {hero_data[0] - 100}")
    print("You are dead.")



def warriorPath1_1_1():
    """
    Function to display the first path choice of path1_2
    and present the user with two new options by using two integers.
    A while loop is also added to loop one of these choices.
    """
    with open('stories/warrior/warrior_path1_1_1.txt') as f:
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
            warriorPath1_1_1_2()
            break



def warriorPath1_1_2():
    """
    Function to display the second path choice of path1_2
    and to loop the choice.
    """
    with open('stories/warrior/warrior_path1_1_2.txt') as f:
            path1_1_2 = f.read()
            print(path1_1_2.format(name))



def warriorPath1_1_1_2():
    """
    Function to display the second path choice of path1_2_1
    and present the user with two new options by using two integers.
    Code is added to send back information to google sheet when users finish the game.
    """
    with open('stories/warrior/warrior_path1_1_1_2.txt') as f:
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

        with open('stories/warrior/warrior_end_1.txt') as f:
            end1 = f.read()
            print(end1.format(name))
    elif fifthPathChoice == 2:
        """
        Get the value for path2 cell from the worksheet, turn it to an int so it can be incremented by 1
        Send it back to update the sheet  
        """
        update_sheet_ending_2()

        with open('stories/warrior/warrior_end_2.txt') as f:
            end2 = f.read()
            print(end2.format(name))



def warriorPath1_2():
    """
    Function to display the second path choice of path1
    and to loop the game.
    """
    with open('stories/warrior/warrior_path1_2.txt') as f:
            path1_2 = f.read()
            print(path1_2.format(name))