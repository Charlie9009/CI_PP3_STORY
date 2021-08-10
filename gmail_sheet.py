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