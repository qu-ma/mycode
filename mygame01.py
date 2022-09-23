#!/usr/bin/python3

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Instructions:
      Get to the Garden with a key and a potion to win! Avoid the monsters! Commands include go direction and get item
    Commands:
      go [direction]
      get [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")

inventory = []

rooms = {
        'Hall': {
            'south': 'Kitchen',
            'east': 'Dining Room',
            'item': 'key'
            },
        'Kitchen': {
            'north': 'Hall',
            'item': 'monster'
            },
        'Dining Room': {
            'west': 'Hall',
            'south': 'Garden',
            'item': 'potion'
            },
        'Garden': {
            'north': 'Dining Room'}
        }

currentRoom = 'Hall'

showInstructions()

while True:
    showStatus()

    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split(" ", 1)

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("You can't go that way!")

    if move[0] == 'get':
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory.append(move[1])
            print(move[1] + ' got!')
            del rooms[currentRoom]['item']
        else:
            print("Can't get " + move[1] + "!")

    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break
    
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
