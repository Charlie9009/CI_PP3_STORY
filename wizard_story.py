from character import name, hero_data

def wizardPath0():
    """
    Function to display the intro of the story
    and present the user with two path options by using to integers.
    """
    pathChoice = int(input("1, 2\n"))
    if pathChoice == 1:
        wizardPath1()
    elif pathChoice == 2:
        wizardPath2()
        
    return pathChoice


def wizardPath1():
    """
    Function to display the first path choice of intro
    and present the user with three new options by using three integers.
    A while loop is also added to loop one of these choices.
    """
    with open('stories/wizard_path1.txt') as f:
            path1 = f.read()
            print(path1.format(name))
    while True:
        print("What will you do?")
        print("1. Light the torch with magic ")
        print("2. Don't light the torch and keep walking")
        secondPathChoice = int(input("1, 2\n"))
        if secondPathChoice == 1:
            wizardPath1_1()
            break
        elif secondPathChoice == 2:
            wizardPath1_2()



def wizardPath1_1():
    """
    Function to display the second path choice of path1
    and present the user with two new options by using two integers.
    """
    with open('stories/wizard_path1_1.txt') as f:
            path1_1 = f.read()
            print(path1_1.format(name))
    print("1. Attack the ogre")
    print("2. Sneak around the ogre")
    thirdPathChoice = int(input("1, 2\n"))
    if thirdPathChoice == 1:
        wizardBattle()
    elif thirdPathChoice == 2:
        wizardPath1_1_2()
        
    return thirdPathChoice


def wizardBattle():
    print("The ogre wakes up and starts running at you.")
    print("What will you do?")
    print("1. Use magic to throw a rock at the ogre")
    print("2. Jump out of the way")
    battleChoice = int(input("1, 2\n"))
    if battleChoice == 1:
        battlePath1()
    elif battleChoice == 2:
        battlePath2()



def battlePath1():
    print("Your throw a rock at the ogre hitting it in the head.")
    print(f"Your mana is now {hero_data[1] - 25}")
    print(f"The ogres health is now ")
    print("The ogre swings it's arm and hits you knocking you back.")
    print(f"Your health is now {hero_data[0] - 25}")
    print("What will you do?")
    print("1. Wait for ogre to make the next move")
    print("2. Use magic to push ogre in to wall")
    battleChoice = int(input("1, 2\n"))
    if battleChoice == 1:
        battlePath1_1()
    elif battleChoice == 2:
        battlePath1_2()


def battlePath1_1():
    print("Before you can react the ogre runs at you pushing you in to the wall knocking you out.")
    print(f"Your health is now {hero_data[0] - 50}")
    print("You are dead.")


def battlePath1_2():
    print("You stand feeling the magic flowing thru you, the ogre start running for you")
    print("You push with you magic as the cave shakes, the ogres feet leaves the ground")
    print("The ogre flies backwards and hits the cave wall.")
    print(f"The ogres health is now")
    print("The ogre is dead")
    print(f"Your mana is now {hero_data[1] - 50}")
    wizardPath1_1_1()

def battlePath2():
    print("As the ogre charges at you, you jump to get out of the way.")
    print("The ogre catches you mid air, and slams you in to the wall.")
    print(f"Your health is now {hero_data[0] - 50}")
    print("You are dead.")



def wizardPath1_1_1():
    """
    Function to display the first path choice of path1_2
    and present the user with two new options by using two integers.
    A while loop is also added to loop one of these choices.
    """
    with open('stories/wizard_path1_1_1.txt') as f:
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
            wizardPath1_1_1_2()
            break



def wizardPath1_1_2():
    """
    Function to display the second path choice of path1_2
    and to end the game.
    """
    print(f"As {name} quietly moves towards the hole the ogre wakes up and sprints at {name}.")
    print(f"Before {name} has even reacted the ogre picks {name} up and throws {name} to the wall, knocking {name} out.")
    print("Game Over.")



def wizardPath1_1_1_2():
    """
    Function to display the second path choice of path1_2_1
    and present the user with two new options by using two integers.
    Code is added to send back information to google sheet when users finish the game.
    """
    print(f"{name} lands and quickly stands, ready to fight if any creature would come out of the dark.")
    print("The flame from the torch now lights up this room")
    print(f"there right in front of {name} a golden horn with the face of a dragon on the side.")
    print("This is the artefact caldun!")
    print(f"{name} starts walking forward but is stopped by a women who just appeared from thin air.")
    print("The woman had uncombed hair, rugged grey clothes and no expression on her face.")
    print("Suddenly the old lady started speaking.")
    print("- You seek caldun.")
    print(f"- Yes. {name} replied.")
    print("- You will then have 2 choices in front of you, either you will take the caldun and become the most powerful wizard")
    print("- Or you will leave and be satisfied with your life as it is. the lady said.")
    print("What will you do?")
    print("1. Take the Caldun")
    print("2. Leave")
    fifthPathChoice = int(input("1, 2\n"))
    if fifthPathChoice == 1:
        """
        Get the value for path1 cell from the worksheet, turn it to an int so it can be incremented by 1
        Send it back to update the sheet  
        """
        finishedPath1 = int(finished_game.cell(2, 1).value)
        finishedPath1 += 1
        finished_game.update_cell(2, 1, finishedPath1)
        print(f"{name} picks up the caldun and suddenly feels a rush of energy flowing thru the body.")
        print("The room starts to light up more and more as every sound intensifies.")
        print(f"{name} starts to scream as the energy starts to pierce thru the body.")
        print(f"Suddenly the room is quiet, the lady is gone and {name} has dissapeared.")
        print(f"The room is completely empty and everything you can hear is the eco of {name}s screams fading away.")
    elif fifthPathChoice == 2:
        """
        Get the value for path2 cell from the worksheet, turn it to an int so it can be incremented by 1
        Send it back to update the sheet  
        """
        finishedPath2 = int(finished_game.cell(2, 2).value)
        finishedPath2 += 1
        finished_game.update_cell(2, 2, finishedPath2)
        print(f"As {name} is walking out of the cave and the sun is shining upon {name} a calm sensation emerges.")
        print(f"What the lady had said was true, a satisfaction within {name} had taken hold.")
        print(f"Embracing that feeling {name} starts walking home.")



def wizardPath1_2():
    """
    Function to display the third path choice of path1
    and to end the game.
    """
    print(f"{name} starts walking forward in the darkness not seeing anything.")
    print(f"Suddenly {name} hears a scrape.")
    print(f"But before {name} can turn around something grabs the ankle and pulls hard, knocking {name} out.")
    print("Game Over.")
    print("Want to try again?")


