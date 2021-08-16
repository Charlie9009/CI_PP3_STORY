from character import name, characterSelect
# Import continuation of stories
from wizard_story import wizardPath0
from warrior_story import warriorPath0
from elf_story import elfPath0


def intro():
    if characterSelect == 1:
        with open('stories/wizard/wizard_intro.txt') as f:
            intro = f.read()
            print(intro.format(name))
            wizardPath0()
    elif characterSelect == 2:
        with open('stories/warrior/warrior_intro.txt') as f:
            intro = f.read()
            print(intro.format(name))
            warriorPath0()
    elif characterSelect == 3:
        with open('stories/elf/elf_intro.txt') as f:
            intro = f.read()
            print(intro.format(name))
            elfPath0()


intro()
