# Import Credentials and worksheet for Google Drive API.
from character import choseClass, name, characterSelect
import gspread
from google.oauth2.service_account import Credentials

# Code used from Code Institutes love-sandwiches project.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("cave_story")

finished_game = SHEET.worksheet("finished_game")

data = finished_game.get_all_values()



def intro():
    if characterSelect == 1:
        with open('stories/wizard_intro.txt') as f:
            intro = f.read()
            print(intro.format(name))
    elif characterSelect == 2:
        with open('stories/warrior_intro.txt') as f:
            intro = f.read()
            print(intro.format(name))
    elif characterSelect == 3:
        with open('stories/elf_intro.txt') as f:
            intro = f.read()
            print(intro.format(name))




def path0():
    """
    Function to display the intro of the story
    and present the user with two path options by using to integers.
    """
    pathChoice = int(input("1, 2\n"))
    if pathChoice == 1:
        path1()
    elif pathChoice == 2:
        path2()
        
    return pathChoice


def path1():
    """
    Function to display the first path choice of intro
    and present the user with three new options by using three integers.
    A while loop is also added to loop one of these choices.
    """
    print(f"{name} starts walking down the dark path, the feeling of unease creeps closer as the air is getting thinner.")
    print("The flame on the torch is fading  slowly and suddenly is put out.")
    print(f"{name} can no longer see, only hear the small drops in the distance and smell the wierd odur.")
    while True:
        print("What will you do?")
        print("1. Light the torch with magic ")
        print("2. Light the torch with two rocks")
        print("3. Don't light the torch and keep walking")
        secondPathChoice = int(input("1, 2, 3\n"))
        if secondPathChoice == 1:
            print("The flame shines brightly for a second but is the put out by a mysterious force.")
        elif secondPathChoice == 2:
            path1_2()
            break
        elif secondPathChoice == 3:
            path1_3()
            break



def path1_2():
    """
    Function to display the second path choice of path1
    and present the user with two new options by using two integers.
    """
    print("The flame shines brightly and lights up the cave.")
    print(f"{name} continues to walk further down in the cave.")
    print(f"{name} gets to a cave room and in the middle of the room stands a big ogre")
    print(f"The ogre twice the size of {name} seems to be asleep.")
    print("Behind the ogre there is a big hole in the ground.")
    print("What will you do?")
    print("1. Attack the ogre")
    print("2. Sneak around the ogre")
    thirdPathChoice = int(input("1, 2\n"))
    if thirdPathChoice == 1:
        path1_2_1()
    elif thirdPathChoice == 2:
        path1_2_2()
        
    return thirdPathChoice


def path1_2_1():
    """
    Function to display the first path choice of path1_2
    and present the user with two new options by using two integers.
    A while loop is also added to loop one of these choices.
    """
    print(f"{name} uses magic to lift a big rock with the mind and with a great force throws the rock  in the ogres head knocking it out.")
    print(f"{name} moves quickly towards the hole in the ground still scared the ogre might wake.")
    print(f"Now {name} stares down in to a dark hole.")
    while True:
        print("What will you do?")
        print("1. Collect courage")
        print("2. Jump down")
        fourthPathChoice = int(input("1, 2\n"))
        if fourthPathChoice == 1:
            print("You collected courage")
        elif fourthPathChoice == 2:
            path1_2_1_2()
            break



def path1_2_2():
    """
    Function to display the second path choice of path1_2
    and to end the game.
    """
    print(f"As {name} quietly moves towards the hole the ogre wakes up and sprints at {name}.")
    print(f"Before {name} has even reacted the ogre picks {name} up and throws {name} to the wall, knocking {name} out.")
    print("Game Over.")
    print("Want to try again?")



def path1_2_1_2():
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



def path1_3():
    """
    Function to display the third path choice of path1
    and to end the game.
    """
    print(f"{name} starts walking forward in the darkness not seeing anything.")
    print(f"Suddenly {name} hears a scrape.")
    print(f"But before {name} can turn around something grabs the ankle and pulls hard, knocking {name} out.")
    print("Game Over.")
    print("Want to try again?")



intro()
path0()

