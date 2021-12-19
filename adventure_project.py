import time
import random

monsters = ['fairie', 'dementor', 'dragon', 'vampire']

items = []


def printer(message):
    print(message)
    time.sleep(1)


def intro():
    printer("You find yourself standing in an open field, "
            "filled with grass and yellow wildflowers.")
    printer("Rumor has it that a wicked enemy is somewhere around here, "
            "and has been terrifying the nearby village.")
    printer("...")


def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        if response in options:
            return response
        printer(f"The option '{response}' is invalid, retry.")


def play_again():
    rep = valid_input("Want to play again, 'y' or 'n'?", ['y', 'n'])
    if 'y' in rep:
        intro()
        game_detail()
    else:
        printer("Thank you for playing our game.")


def door1():   # fairie door
    printer("You have opened the first door")
    printer("The wicked enemy is inside this room")
    global items
    global monsters
    monster = random.choice(monsters)
    if 'weapon' in items:
        if 'armor' in items:
            printer(f"You have the necessary items to fight the {monster}")
            printer(f"after a prolonged battle, "
                    "you defeat the {monster} and saved the town")
            printer("The villagers are happy and named you their hero.")
            play_again()
        else:
            printer("you enter a prolonged battle with only "
                    "weapon and no armor")
            printer(f"The {monster} wins the battle as a result "
                    "of your lack of armor")
            printer("The villagers are sad")
            play_again()
    elif 'armor' in items:
        if 'weapon' in items:
            print(f"You have the necessary items to fight the {monster}")
            printer(f"after a prolonged battle, you defeat the {monster} "
                    "and saved the town")
            printer("The villagers are happy and named you their hero.")
            play_again()
        else:
            printer("you enter a prolonged battle with only "
                    "armor and no weapon")
            printer(f"The {monster} wins the battle as a result "
                    "of your lack of weapon")
            printer("The villagers are sad")
            play_again()
    else:
        printer("You have neither weapon nor armor, are you "
                "sure you want to proceed?")
        rep = valid_input("Enter '1' to proceed or '2' to go back outside\n",
                          ['1', '2'])
        if rep == '1':
            printer(f"you come face to face with the {monster} "
                    "who wastes no time in killing you")
            printer("The villagers are sad")
            play_again()
        elif rep == '2':
            printer("you have choosen to go back outside")
            select_door()


def door2():  # armor door
    global items
    printer("You have entered the armor room")
    printer("You find an armor behind the door")
    take = valid_input("Take it or not, 'y' or 'n' ", ['y', 'n'])
    if 'y' in take:
        items.append('armor')
        printer("You have taken and worn the armor")
        select_door()
    elif 'n' in take:
        printer("You have choosen not to wear the armor")
        select_door()


def door3():  # weapon door
    global items
    printer("You have entered the weapon room")
    printer("You find a weapon behind the door")
    take = valid_input("Take it or not, 'y' or 'n' ", ['y', 'n'])
    if 'y' in take:
        items.append('weapon')
        printer("you have taken the weapon")
        select_door()
    elif 'n' in take:
        printer("you have choosen not to take the weapon")
        select_door()


def select_door():
    response = valid_input("Which door do you want to open?, "
                           "'1' or '2' or '3'\n",
                           ['1', '2', '3'])
    if '1' in response:
        door1()
    elif '2' in response:
        door2()
    elif '3' in response:
        door3()


def game_detail():
    printer("There are 3 doors in front of you, "
            "one contains weapon, "
            "another contains armor, "
            "another contains the wicked monster")
    select_door()


def start():
    intro()
    game_detail()


start()
