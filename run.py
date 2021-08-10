# Import Credentials and worksheet for Google Drive API.
from character import choseClass, name, characterSelect
from wizard_story import wizardPath0
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
            wizardPath0()
    elif characterSelect == 2:
        with open('stories/warrior_intro.txt') as f:
            intro = f.read()
            print(intro.format(name))
    elif characterSelect == 3:
        with open('stories/elf_intro.txt') as f:
            intro = f.read()
            print(intro.format(name))




intro()


