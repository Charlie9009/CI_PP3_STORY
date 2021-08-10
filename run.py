# Import Credentials and worksheet for Google Drive API.
from character import choseClass, name, characterSelect
from wizard_story import wizardPath0


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


