# Import Credentials and worksheet for Google Drive API.
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


name = input("What it your name?\n")

def intro():
    """
    Function to display the intro of the story
    and present the user with two path options.
    """
    print(f"In the deep Veryovkina caves in Abkhazia year 1545 the wizard {name} is looking for the legendary artefact caldun.")
    print(f"{name} comes to a crossroads. The left path is dark.")
    print("The right path is light.")
    print("Which path will you take?")
    print("1. Go left")
    print("2. Go right")
    pathChoice = int(input("1, 2\n"))
    if pathChoice == 1:
        path1()
    elif pathChoice == 2:
        path2()
        
    return pathChoice


def path1():
    """
    Function to display the first path choice
    and present the user with three new options.
    """
    print(f"{name} starts walking down the dark path, the feeling of unease creeps closer as the air is getting thinner.")
    print("The flame on the torch is fading  slowly and suddenly is put out.")
    print(f"{name} can no longer see, only hear the small drops in the distance and smell the wierd odur.")
    print("What will you do?")
    print("1. Light the torch with magic ")
    print("2. Light the torch with two rocks")
    print("3. Don't light the torch and keep walking")
    secondPathChoice = int(input("1, 2, 3\n"))
    while True:
        if secondPathChoice == 1:
            print("As the flame lights up {name} is not in the same place anymore.")
            print(f"{name} is at the crossroads and takes the left path again.")
            path1()
        elif secondPathChoice == 2:
            path1_2()
            break
        elif secondPathChoice == 3:
            path1_3()
            break

        return secondPathChoice


def path1_1():
    print("The flame shines brightly for a second but is the put out by a mysterious force.")
    print("")
    print("")
    print("")


def path1_2():
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
    print(f"{name} uses magic to lift a big rock with the mind and with a great force throws the rock  in the ogres head knocking it out.")
    print(f"{name} moves quickly towards the hole in the ground still scared the ogre might wake.")
    print(f"Now {name} stares down in to a dark hole.")
    print("What will you do?")
    print("1. Collect courage")
    print("2. Jump down")


def path1_2_2():
    print(f"As {name} quietly moves towards the hole the ogre wakes up and sprints at {name}.")
    print(f"Before {name} has even reacted the ogre picks {name} up and throws {name} to the wall, knocking {name} out.")
    print("Game Over.")
    print("Want to try again?")


#def path1_2_1_1():



#def path1_2_1_2():




def path1_3():
    print(f"{name} starts walking forward in the darkness not seeing anything.")
    print(f"Suddenly {name} hears a scrape.")
    print(f"But before {name} can turn around something grabs the ankle and pulls hard, knocking {name} out.")
    print("Game Over.")
    print("Want to try again?")




intro()

