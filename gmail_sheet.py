# Import Credentials and worksheet for Google Drive API.
import gspread
from google.oauth2.service_account import Credentials


# Code used from Code Institutes love-sandwiches project.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

# Constants
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("cave_story")
FINISHED_GAME = SHEET.worksheet("finished_game")


def update_sheet_wizard_ending_1():
    """
    Function to get value from google sheets and increment it by 1,
    then send it back when user finishes wizard story ending 1
    """
    finishedPath1 = int(FINISHED_GAME.cell(2, 1).value)
    finishedPath1 += 1
    FINISHED_GAME.update_cell(2, 1, finishedPath1)


def update_sheet_wizard_ending_2():
    """
    Function to get value from google sheets and increment it by 1,
    then send it back when user finishes wizard story ending 2
    """
    finishedPath2 = int(FINISHED_GAME.cell(2, 2).value)
    finishedPath2 += 1
    FINISHED_GAME.update_cell(2, 2, finishedPath2)


def update_sheet_warrior_ending_1():
    """
    Function to get value from google sheets and increment it by 1,
    then send it back when user finishes warrior story ending 1
    """
    finishedPath1 = int(FINISHED_GAME.cell(2, 3).value)
    finishedPath1 += 1
    FINISHED_GAME.update_cell(2, 3, finishedPath1)


def update_sheet_warrior_ending_2():
    """
    Function to get value from google sheets and increment it by 1,
    then send it back when user finishes warrior story ending 2
    """
    finishedPath2 = int(FINISHED_GAME.cell(2, 4).value)
    finishedPath2 += 1
    FINISHED_GAME.update_cell(2, 4, finishedPath2)


def update_sheet_elf_ending_1():
    """
    Function to get value from google sheets and increment it by 1,
    then send it back when user finishes elf story ending 1
    """
    finishedPath1 = int(FINISHED_GAME.cell(2, 5).value)
    finishedPath1 += 1
    FINISHED_GAME.update_cell(2, 5, finishedPath1)


def update_sheet_elf_ending_2():
    """
    Function to get value from google sheets and increment it by 1,
    then send it back when user finishes elf story ending 2
    """
    finishedPath2 = int(FINISHED_GAME.cell(2, 6).value)
    finishedPath2 += 1
    FINISHED_GAME.update_cell(2, 6, finishedPath2)


def get_wizard_loot():
    """
    Function to get wizard loot value from google sheets,
    add it to a list and print it to the user to show dropped loot.
    """
    ogreItem = []
    wizardLoot = FINISHED_GAME.cell(2, 7).value
    ogreItem.append(wizardLoot)
    print(f"The ogre dropped a {ogreItem[0]}")


def get_warrior_loot():
    """
    Function to get warrior loot value from google sheets,
    add it to a list and print it to the user to show dropped loot.
    """
    ogreItem = []
    warriorLoot = FINISHED_GAME.cell(2, 8).value
    ogreItem.append(warriorLoot)
    print(f"The ogre dropped a {ogreItem[0]}")


def get_elf_loot():
    """
    Function to get elf loot value from google sheets,
    add it to a list and print it to the user to show dropped loot.
    """
    ogreItem = []
    elfLoot = FINISHED_GAME.cell(2, 9).value
    ogreItem.append(elfLoot)
    print(f"The ogre gave you a {ogreItem[0]}")
