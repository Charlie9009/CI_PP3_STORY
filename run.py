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
    path = input("Which path will you take? (1 or 2)\n")
    if path == '1':
        firstPath()
    elif path == '2':
        secondPath()
        
    return path

intro()

