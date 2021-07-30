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
    print(f"In the deep Veryovkina caves in Abkhazia year 1545 the wizard {name} is looking for the legendary artefact caldun.")
    print(f"{name} comes to a crossroads. The left path is dark.")
    print("The right path is light.")
    print("Which path will you take?")
    print("1. Go left")
    print("2. Go left")
    pathChoice = input(" (1, 2)\n")
    if pathChoice == "1":
        path1()
    elif pathChoice == "2":
        path2()
        
    return pathChoice


def path1():
    print(f"{name} starts walking down the dark path, the feeling of unease creeps closer as the air is getting thinner.")
    print("The flame on the torch is fading  slowly and suddenly is put out.")
    print(f"{name} can no longer see, only hear the small drops in the distance and smell the wierd odur.")
    print("What will you do?")
    print("1. Don't light the torch and keep walking")
    print("2. Light the torch with two rocks")
    print("3. Light the torch with magic")
    secondPathChoice = input("1, 2, 3\n")
    if secondPathChoice == "1":
        path1_1()
    elif secondPathChoice == "2":
        path1_2()
    elif secondPathChoice == "3":
        path1_3()

    return secondPathChoice


intro()

