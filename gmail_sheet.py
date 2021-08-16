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


def update_sheet_ending_1():
    finishedPath1 = int(finished_game.cell(2, 1).value)
    finishedPath1 += 1
    finished_game.update_cell(2, 1, finishedPath1)


def update_sheet_ending_2():
    finishedPath2 = int(finished_game.cell(2, 2).value)
    finishedPath2 += 1
    finished_game.update_cell(2, 2, finishedPath2)


def get_wizard_loot():
    ogreItem = []
    wizardLoot = finished_game.cell(2, 7).value
    ogreItem.append(wizardLoot)
    print(f"The ogre dropped a {ogreItem[0]}")


def get_warrior_loot():
    ogreItem = []
    warriorLoot = finished_game.cell(2, 8).value
    ogreItem.append(warriorLoot)
    print(f"The ogre dropped a {ogreItem[0]}")


def get_elf_loot():
    ogreItem = []
    elfLoot = finished_game.cell(2, 9).value
    ogreItem.append(elfLoot)
    print(f"The ogre gave you a {ogreItem[0]}")