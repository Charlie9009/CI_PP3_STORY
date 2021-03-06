from character import NAME, hero_data, ogre_data
from gmail_sheet import update_sheet_wizard_ending_1, get_wizard_loot
from gmail_sheet import update_sheet_wizard_ending_2


def wizardPath0():
    """
    Function to display the first choice in the story.
    Presenting the user with the number 1 to continue with a new function.
    """
    pathChoice = input("1\n")
    # Input validation
    while pathChoice != "1":
            print("Invalid input")
            pathChoice = input("1\n")

    if pathChoice == "1":
        wizardPath1()


def wizardPath1():
    """
    Function to display the continuation of wizardPath0
    and present the user with two new options by using two integers.
    A while loop is also added to loop one of these choices.
    """
    with open('stories/wizard/wizard_path1.txt') as f:
            path1 = f.read()
            print(path1.format(NAME))
    while True:
        print("What will you do?")
        print("1. Light the torch with magic ")
        print("2. Don't light the torch and keep walking")
        secondPathChoice = input("1, 2\n")
        # Input validation
        while secondPathChoice != "1" and secondPathChoice != "2":
            print("Invalid input")
            secondPathChoice = input("1, 2\n")

        if secondPathChoice == "1":
            wizardPath1_1()
            break
        elif secondPathChoice == "2":
            wizardPath1_2()


def wizardPath1_1():
    """
    Function to display the continuation of wizardPath1
    and present the user with two new options by using two integers.
    """
    with open('stories/wizard/wizard_path1_1.txt') as f:
            path1_1 = f.read()
            print(path1_1.format(NAME))
    print("1. Attack the ogre")
    print("2. Sneak around the ogre")
    thirdPathChoice = input("1, 2\n")
    # Input validation
    while thirdPathChoice != "1" and thirdPathChoice != "2":
        print("Invalid input")
        thirdPathChoice = input("1, 2\n")

    if thirdPathChoice == "1":
        wizardBattle()
    elif thirdPathChoice == "2":
        wizardPath1_1_2()


def wizardBattle():
    """
    Function to display the continuation of wizardPath1_1
    and present the user with two new options by using two integers.
    """
    print("The ogre wakes up and starts running at you.")
    print("What will you do?")
    print("1. Use magic to throw a rock at the ogre")
    print("2. Jump out of the way")
    battleChoice = input("1, 2\n")
    # Input validation
    while battleChoice != "1" and battleChoice != "2":
        print("Invalid input")
        battleChoice = input("1, 2\n")

    if battleChoice == "1":
        wizardBattle1()
    elif battleChoice == "2":
        wizardBattle2()


def wizardBattle1():
    """
    Function to display the continuation of wizardBattle,
    getting hero_data and ogre_data to display health and mana.
    and present the user with two new options by using two integers.
    """
    print("Your throw a rock at the ogre hitting it in the head.")
    print(f"Your mana is now {hero_data[1] - 25}")
    print(f"The ogres health is now {ogre_data - 30}")
    print("The ogre swings it's arm and hits you knocking you back.")
    print(f"Your health is now {hero_data[0] - 25}")
    print("What will you do?")
    print("1. Wait for ogre to make the next move")
    print("2. Use magic to push ogre in to wall")
    battleChoice = input("1, 2\n")
    # Input validation
    while battleChoice != "1" and battleChoice != "2":
        print("Invalid input")
        battleChoice = input("1, 2\n")

    if battleChoice == "1":
        wizardBattle1_1()
    elif battleChoice == "2":
        wizardBattle1_2()


def wizardBattle1_1():
    """
    Function to display the continuation of wizardBattle1,
    getting hero_data to display health
    and ending the game.
    """
    print("Before you can react the ogre runs at you")
    print("The ogre pushes you in to the wall knocking you out.")
    print(f"Your health is now {hero_data[0] - 50}")
    print("You are dead.")


def wizardBattle1_2():
    """
    Function to display the continuation of wizardBattle1,
    getting hero_data and ogre_data to display health and mana.
    Function is called to present loot dropped from ogre
    Function is called to continue the story.
    """
    print("You stand feeling the magic flowing thru you,")
    print("the ogre starts running for you")
    print("You push with you magic as the cave shakes,")
    print("the ogres feet leaves the ground.")
    print("The ogre flies backwards and hits the cave wall.")
    print(f"The ogres health is now {ogre_data - 100}")
    print("The ogre is dead")
    print(f"Your mana is now {hero_data[1] - 50}")
    get_wizard_loot()
    wizardPath1_1_1()


def wizardBattle2():
    """
    Function to display the continuation of wizardBattle,
    getting hero_data to display health
    and ending the game.
    """
    print("As the ogre charges at you, you jump to get out of the way.")
    print("The ogre catches you mid air, and slams you in to the wall.")
    print(f"Your health is now {hero_data[0] - 50}")
    print("You are dead.")


def wizardPath1_1_1():
    """
    Function to display the continuation of wizardBattle1_2
    and present the user with two new options by using two integers.
    A while loop is also added to loop one of these choices.
    """
    with open('stories/wizard/wizard_path1_1_1.txt') as f:
            path1_1_1 = f.read()
            print(path1_1_1.format(NAME))
    while True:
        print("What will you do?")
        print("1. Collect courage")
        print("2. Jump down")
        fourthPathChoice = input("1, 2\n")
        # Input validation
        while fourthPathChoice != "1" and fourthPathChoice != "2":
            print("Invalid input")
            fourthPathChoice = input("1, 2\n")

        if fourthPathChoice == "1":
            print("You collected courage")
        elif fourthPathChoice == "2":
            wizardPath1_1_1_2()
            break


def wizardPath1_1_2():
    """
    Function to display the continuation of wizardPath1_1
    and to end the game.
    """
    with open('stories/wizard/wizard_path1_1_2.txt') as f:
            path1_1_2 = f.read()
            print(path1_1_2.format(NAME))


def wizardPath1_1_1_2():
    """
    Function to display the continuation of wizardPath1_1_1
    and present the user with two ending options by using two integers.
    Function is added to send back information to google sheet,
    when users finish the game.
    """
    with open('stories/wizard/wizard_path1_1_1_2.txt') as f:
            path1_1_1_2 = f.read()
            print(path1_1_1_2.format(NAME))
    print("1. Take the Caldun")
    print("2. Leave")
    fifthPathChoice = input("1, 2\n")
    # Input validation
    while fifthPathChoice != "1" and fifthPathChoice != "2":
        print("Invalid input")
        fifthPathChoice = input("1, 2\n")

    if fifthPathChoice == "1":
        # Function called from gmail_sheet.py
        update_sheet_wizard_ending_1()
        # Display story
        with open('stories/wizard/wizard_end_1.txt') as f:
            end1 = f.read()
            print(end1.format(NAME))
    elif fifthPathChoice == "2":
        # Function called from gmail_sheet.py
        update_sheet_wizard_ending_2()
        # Display story
        with open('stories/wizard/wizard_end_2.txt') as f:
            end2 = f.read()
            print(end2.format(NAME))


def wizardPath1_2():
    """
    Function to display the continuation of wizardPath1
    and to loop the game.
    """
    with open('stories/wizard/wizard_path1_2.txt') as f:
            path1_2 = f.read()
            print(path1_2.format(NAME))
