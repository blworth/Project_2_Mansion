#!/usr/bin/env python3
from time import sleep
import sys

# displays item in current room


def current_room_item():
    if "item" in rooms[currentRoom]:
        print('---')
        typewriter('You see a ' + rooms[currentRoom]['item'])
        print('\n---')

# typewrite for normal text


def typewriter(l):
    for letter in l:
        print(letter, end='')
        sys.stdout.flush()
        sleep(.05)

# typewriter for big ASCII letters


def typewriter2(big_letter):
    for x in big_letter:
        print(x, end="")
        sys.stdout.flush()
        sleep(.001)


# ASCII letters in a tuple for nicer display
game_over = ("\n░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░", "\n██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗", "\n██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝",
             "\n██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗", "\n╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║", "\n░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝")


def gameIntro():
    # prints instructions and tips
    typewriter('''
Let's find the truth about Pete!!

Directions:
    1) Navigate the mansion
    2) Find the key, lockbox, and computer
    3) Avoid the monster
    4) Find the exit

Commands:
    go [direction]      ex: go north
    get [item]          ex: get potion

Tips: 
    1) Get a piece of paper
    2) Get something to write with
    3) Map out the mansion as you go
\n''')


def showStatus():
    # printing player status
    typewriter('You are in the ' + currentRoom)
    # prinitng player inventory
    typewriter('\nInventory: ' + str(inventory))


# player inventory, items gett added to this list when acquired
inventory = []

# the rooms in dictionary form, shows what rooms lead to what rooms and what is inside each
rooms = {

    'Atrium': {
        'north': 'Indoor Pool',
        'south': 'Hallway',
        'east': 'Closet1',
    },
    'Closet1': {
        'west': 'Atrium',
    },
    'Bedroom': {
        'west': 'Indoor Pool',
    },
    'Indoor Pool': {
        'south': 'Atrium',
        'west': 'Bathroom',
        'east': 'Bedroom'
    },
    'Bathroom': {
        'east': 'Indoor Pool',
        'item': 'key'
    },
    'Hallway': {
        'north': 'Atrium',
        'east': 'Kitchen',
        'west': 'Game Room',
        'south': 'Laundry Room'
    },
    'Kitchen': {
        'west': 'Hallway',
        'item': 'lock box'
    },
    'Laundry Room': {
        'north': 'Hallway',
    },
    'Closet2': {
        'north': 'Game Room'

    },
    'Game Room': {
        'east': 'Hallway',
        'north': 'Office',
        'south': 'Closet2'
    },
    'Office': {
        'south': 'Game Room',
        'item': 'laptop',
    }
}

# player starting location
currentRoom = 'Atrium'

gameIntro()
while True:
    showStatus()

# input for players move i.e. 'go' or 'get'
    move = ''
    while move == '':
        move = input('\n>')
        print("\n\n\n")

    move = move.lower().split(" ", 1)

    # if player input is 'go'
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]

        # print message if the player cannot go a direction
        else:
            print('You can\'t go that way!')

    # if player input is 'get'
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            # for kitchen with key in inventory
            if currentRoom == 'Kitchen' and inventory.__contains__('key'):
                inventory += [move[1]]
                print('---')
                typewriter(move[1] + ' placed in your inventory!\n')
                print('---')
                del rooms[currentRoom]['item']
                typewriter(
                    'Nice job! You have opened the lock box and recieved a flash drive.\n')
                print('---')
                inventory += ['flash drive']
            # for bathroom no key yet
            elif currentRoom == 'Bathroom':
                inventory += [move[1]]
                print(move[1] + ' placed in your inventory!')
                del rooms[currentRoom]['item']
            # for office with flash drive in inventory
            elif currentRoom == 'Office' and inventory.__contains__('flash drive'):
                inventory += [move[1]]
                print('---')
                typewriter(move[1] + ' placed in your inventory!\n')
                print('---')
                del rooms[currentRoom]['item']
                typewriter(
                    'Nice job! You have found the laptop!\nYou place the flash drive in the laptop and discover the true whereabouts of Pete!\nThere is also a code... this has to be the code for the front door!\n')
                print('---')
                inventory += ['code']
        # otherwise, if no itme to get, print below
        else:
            print('Can\'t get ' + move[1] + '!')

    # conditionals for displaying items in rooms and win/lose
    if currentRoom == 'Kitchen' and 'key' not in inventory:
        current_room_item()
        typewriter('You need a key to get the lock box!')
        print('\n---')
    elif currentRoom == 'Kitchen' and 'key' in inventory:
        current_room_item()

    elif currentRoom == 'Office' and 'flash drive' in inventory:
        current_room_item()
    elif currentRoom == 'Office' and 'flash drive' not in inventory:
        current_room_item()
        typewriter(
            'The laptop has no connection and is wiped clean.\nI need to find something to plug into it!')
        print('\n---')

    # win
    elif currentRoom == 'Atrium' and 'code' in inventory:
        typewriter(
            '\nLook! there is the code on the front door! Here we go!\n<beep> <beep> <boop> <bop>\n*Access Granted*\n')
        input("Please enter anything to escape!\n")
        typewriter(
            "\nCongratulations you have escaped the Mansion!\n Now go let the world know what you discovered about Pete!")
        break
    elif currentRoom == 'Atrium' and 'code' not in inventory:
        print('---')
        typewriter(
            'You see a front door with a code lock... that must be my way out!')
        print('\n---')

    # lose to monster
    elif currentRoom == 'Closet1' or currentRoom == 'Closet2':
        typewriter(
            'Whaaaaaaa?!?! ahhhhhhh!!!!!!\n *your face is ripped off by a monster*\n\n')
        typewriter2(game_over)
        break

    # displays key in bathroom
    elif currentRoom == 'Bathroom':
        current_room_item()
