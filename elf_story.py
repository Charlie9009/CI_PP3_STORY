from character import NAME, hero_data
from gmail_sheet import update_sheet_elf_ending_1, get_elf_loot
from gmail_sheet import update_sheet_elf_ending_2


def elfPath0():
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
        elfPath1()


def elfPath1():
    """
    Function to display the continuation of elfPath0
    and present the user with two new options by using two integers.
    A while loop is also added to loop one of these choices.
    """
    with open('stories/elf/elf_path1.txt') as f:
            path1 = f.read()
            print(path1.format(NAME))
    while True:
        print("What will you do?")
        print("1. Light the torch by scraping two rocks together")
        print("2. Don't light the torch and keep walking")
        secondPathChoice = input("1, 2\n")
        # Input validation
        while secondPathChoice != "1" and secondPathChoice != "2":
            print("Invalid input")
            secondPathChoice = input("1, 2\n")

        if secondPathChoice == "1":
            elfPath1_1()
            break
        elif secondPathChoice == "2":
            elfPath1_2()


def elfPath1_1():
    """
    Function to display the continuation of elfPath1
    and present the user with two new options by using two integers.
    """
    with open('stories/elf/elf_path1_1.txt') as f:
            path1_1 = f.read()
            print(path1_1.format(NAME))
    print("1. Talk to the ogre")
    print("2. Sneak around the ogre")
    thirdPathChoice = input("1, 2\n")
    # Input validation
    while thirdPathChoice != "1" and thirdPathChoice != "2":
        print("Invalid input")
        thirdPathChoice = input("1, 2\n")

    if thirdPathChoice == "1":
        elfBattle()
    elif thirdPathChoice == "2":
        elfPath1_1_2()


def elfBattle():
    """
    Function to display the continuation of elfPath1_1
    and present the user with two new options by using two integers.
    """
    print("The ogre wakes up and starts running at you.")
    print("What will you do?")
    print("1. Offer your gold neckless to the ogre")
    print("2. jump to get out of the way")
    battleChoice = input("1, 2\n")
    # Input validation
    while battleChoice != "1" and battleChoice != "2":
        print("Invalid input")
        battleChoice = input("1, 2\n")

    if battleChoice == "1":
        elfBattle1()
    elif battleChoice == "2":
        elfBattle2()


def elfBattle1():
    """
    Function to display the continuation of elfBattle,
    Function is called to present loot dropped from ogre
    Function is called to continue the story.
    """
    print("As the ogre charges at you, you offer it your gold neckless.")
    print("The ogre stops in it's tracks and looks at it with awe.")
    print("- Wooow not one person has offered me gold in centuries,")
    print("- you are free to pass. The ogre said")
    get_elf_loot()
    elfPath1_1_1()


def elfBattle2():
    """
    Function to display the continuation of elfBattle,
    getting hero_data to display health
    and ending the game.
    """
    print("As the ogre charges at you, you jump to get out of the way.")
    print("The ogre catches you mid air, and slams you in to the wall.")
    print(f"Your health is now {hero_data[0] - 25}")
    print("You are dead.")


def elfPath1_1_1():
    """
    Function to display the continuation of elfBattle1
    and present the user with two new options by using two integers.
    A while loop is also added to loop one of these choices.
    """
    with open('stories/elf/elf_path1_1_1.txt') as f:
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
            elfPath1_1_1_2()
            break


def elfPath1_1_2():
    """
    Function to display the continuation of elfPath1_1
    and to end the game.
    """
    with open('stories/elf/elf_path1_1_2.txt') as f:
            path1_1_2 = f.read()
            print(path1_1_2.format(NAME))


def elfPath1_1_1_2():
    """
    Function to display the continuation of elfPath1_1_1
    and present the user with two ending options by using two integers.
    Function is added to send back information to google sheet,
    when users finish the game.
    """
    with open('stories/elf/elf_path1_1_1_2.txt') as f:
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
        update_sheet_elf_ending_1()
        # Display story
        with open('stories/elf/elf_end_1.txt') as f:
            end1 = f.read()
            print(end1.format(NAME))
    elif fifthPathChoice == "2":
        # Function called from gmail_sheet.py
        update_sheet_elf_ending_2()
        # Display story
        with open('stories/elf/elf_end_2.txt') as f:
            end2 = f.read()
            print(end2.format(NAME))


def elfPath1_2():
    """
    Function to display the continuation of elfPath1
    and to loop the game.
    """
    with open('stories/elf/elf_path1_2.txt') as f:
            path1_2 = f.read()
            print(path1_2.format(NAME))
