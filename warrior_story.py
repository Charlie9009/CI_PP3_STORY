from character import NAME, hero_data, ogre_data
from gmail_sheet import update_sheet_warrior_ending_1, get_warrior_loot
from gmail_sheet import update_sheet_warrior_ending_2


def warriorPath0():
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
        warriorPath1()


def warriorPath1():
    """
    Function to display the continuation of warriorPath0
    and present the user with two new options by using two integers.
    A while loop is also added to loop one of these choices.
    """
    with open('stories/warrior/warrior_path1.txt') as f:
            path1 = f.read()
            print(path1.format(NAME))
    while True:
        print("What will you do?")
        print("1. Don't light the torch and keep walking")
        print("2. Light the torch with magic")
        secondPathChoice = input("1, 2\n")
        # Input validation
        while secondPathChoice != "1" and secondPathChoice != "2":
            print("Invalid input")
            secondPathChoice = input("1, 2\n")

        if secondPathChoice == "1":
            warriorPath1_1()
            break
        elif secondPathChoice == "2":
            warriorPath1_2()


def warriorPath1_1():
    """
    Function to display the continuation of warriorPath1
    and present the user with two new options by using two integers.
    A while loop is also added to loop one of these choices.
    """
    with open('stories/warrior/warrior_path1_1.txt') as f:
            path1_1 = f.read()
            print(path1_1.format(NAME))
    while True:
        print("1. Attack the ogre")
        print("2. Sneak around the ogre")
        thirdPathChoice = input("1, 2\n")
        # Input validation
        while thirdPathChoice != "1" and thirdPathChoice != "2":
            print("Invalid input")
            thirdPathChoice = input("1, 2\n")

        if thirdPathChoice == "1":
            warriorBattle()
            break
        elif thirdPathChoice == "2":
            warriorPath1_1_2()


def warriorBattle():
    """
    Function to display the continuation of warriorPath1_1
    and present the user with two new options by using two integers.
    """
    print("The ogre starts running at you.")
    print("What will you do?")
    print("1. Pick up a big rock and throw it at the ogre")
    print("2. Jump out of the way")
    battleChoice = input("1, 2\n")
    # Input validation
    while battleChoice != "1" and battleChoice != "2":
        print("Invalid input")
        battleChoice = input("1, 2\n")

    if battleChoice == "1":
        warriorBattle1()
    elif battleChoice == "2":
        warriorBattle2()


def warriorBattle1():
    """
    Function to display the continuation of warriorBattle,
    getting hero_data and ogre_data to display health.
    and present the user with two new options by using two integers.
    """
    print("Your throw a rock at the ogre hitting it in the head.")
    print(f"The ogres health is now {ogre_data - 50}")
    print("The ogre swings it's arm and hits you barely knocking you back.")
    print(f"Your health is now {hero_data[0] - 10}")
    print("What will you do?")
    print("1. Wait for ogre to make the next move")
    print("2. Charge at the ogre")
    battleChoice = input("1, 2\n")
    # Input validation
    while battleChoice != "1" and battleChoice != "2":
        print("Invalid input")
        battleChoice = input("1, 2\n")

    if battleChoice == "1":
        warriorBattle1_1()
    elif battleChoice == "2":
        warriorBattle1_2()


def warriorBattle1_1():
    """
    Function to display the continuation of warriorBattle1,
    getting hero_data and ogre_data to display health.
    Function is called to present loot dropped from ogre
    Function is called to continue the story.
    """
    print("Before you can react the ogre runs at you,")
    print("pushing you in to the wall.")
    print(f"Your health is now {hero_data[0] - 60}")
    print("As you are trapped between the wall and the ogre,")
    print("you manage to punch the ogre in the face.")
    print(f"The ogres health is now {ogre_data - 100}")
    print("The ogre is dead")
    get_warrior_loot()
    warriorPath1_1_1()


def warriorBattle1_2():
    """
    Function to display the continuation of warriorBattle1,
    getting hero_data and ogre_data to display health.
    Function is called to present loot dropped from ogre
    Function is called to continue the story.
    """
    print("You charge the ogre with full force.")
    print("You smash into the ogre,")
    print("with the warrior strength the ogres feet leaves the ground")
    print("You push the ogre straight into the cave wall,")
    print("as the ogre smashes in to it, it collapses on the ground")
    print(f"The ogres health is now {ogre_data - 100}")
    print("The ogre is dead")
    print(f"Your health is now {hero_data[0] - 80}")
    get_warrior_loot()
    warriorPath1_1_1()


def warriorBattle2():
    """
    Function to display the continuation of warriorBattle,
    getting hero_data to display health
    and ending the game.
    """
    print("As the ogre charges at you, you jump to get out of the way.")
    print("The ogre catches you mid air, and slams you in to the wall.")
    print(f"Your health is now {hero_data[0] - 100}")
    print("You are dead.")


def warriorPath1_1_1():
    """
    Function to display the continuation of warriorBattle1_1, warriorBattle1_2
    and present the user with two new options by using two integers.
    A while loop is also added to loop one of these choices.
    """
    with open('stories/warrior/warrior_path1_1_1.txt') as f:
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
            warriorPath1_1_1_2()
            break


def warriorPath1_1_2():
    """
    Function to display the continuation of warriorPath1_1
    and to loop the choice.
    """
    with open('stories/warrior/warrior_path1_1_2.txt') as f:
            path1_1_2 = f.read()
            print(path1_1_2.format(NAME))


def warriorPath1_1_1_2():
    """
    Function to display the continuation of warriorPath1_1_1
    and present the user with two ending options by using two integers.
    Function is added to send back information to google sheet,
    when users finish the game.
    """
    with open('stories/warrior/warrior_path1_1_1_2.txt') as f:
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
        update_sheet_warrior_ending_1()
        # Display story
        with open('stories/warrior/warrior_end_1.txt') as f:
            end1 = f.read()
            print(end1.format(NAME))
    elif fifthPathChoice == "2":
        # Function called from gmail_sheet.py
        update_sheet_warrior_ending_2()
        # Display story
        with open('stories/warrior/warrior_end_2.txt') as f:
            end2 = f.read()
            print(end2.format(NAME))


def warriorPath1_2():
    """
    Function to display the continuation of warriorPath1
    and to loop the game.
    """
    with open('stories/warrior/warrior_path1_2.txt') as f:
            path1_2 = f.read()
            print(path1_2.format(NAME))
