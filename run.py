from character import NAME, characterSelect
# Import continuation of stories
from wizard_story import wizardPath0
from warrior_story import warriorPath0
from elf_story import elfPath0


def intro():
    """
    Function to display three choices to the user,
    Wizard, Warrior or Elf.
    Opening chosen file when user has chosen class,
    format NAME to keep user name and new function to continue story.
    """
    if characterSelect == 1:
        # Wizard
        with open('stories/wizard/wizard_intro.txt') as f:
            intro = f.read()
            print(intro.format(NAME))
            wizardPath0()
    elif characterSelect == 2:
        # Warrior
        with open('stories/warrior/warrior_intro.txt') as f:
            intro = f.read()
            print(intro.format(NAME))
            warriorPath0()
    elif characterSelect == 3:
        # Elf
        with open('stories/elf/elf_intro.txt') as f:
            intro = f.read()
            print(intro.format(NAME))
            elfPath0()


intro()
