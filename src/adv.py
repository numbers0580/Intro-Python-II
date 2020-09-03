from os import system, name
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", "true"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", "false"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", "false"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", "false"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", "false"),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
mygame = Player("Jacks Treasure Hunt", [room["outside"], room["foyer"], room["overlook"], room["narrow"], room["treasure"]])

# Make a new player object that is currently in the 'outside' room.
# myhero = Player("Jack")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# I got the following code from: https://www.geeksforgeeks.org/clear-screen-python/
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
# ------Clear Screen Method Above--------------


#               MAP
# 
# |------------|   |------------|
# |            |   |            |
# |  Overlook  |   |  Treasure  |
# |            |   |            |
# |----|  |----|   |----|  |----|
#      |  |             |  |
# |----|  |----|   |----|  |----|
# |            -----            |
# |   Foyer            Narrow   |
# |            -----            |
# |----|  |----|   |------------|
#      |  |
# |----|  |----|
# |            |
# |  Outside   |
# |            |
# |------------|
# 

def drawmap1():
    print("               MAP\n")
    print(" |------------|   |------------|\n |            |   |            |\n |  Overlook  |   |  Treasure  |")
    if currentRoom.name == "Grand Overlook":
        print(" |     X      |   |            |")
    elif currentRoom.name == "Treasure Chamber":
        print(" |            |   |      X     |")
    else:
        print(" |            |   |            |")
    print(" |----|  |----|   |----|  |----|\n      |  |             |  |\n |----|  |----|   |----|  |----|\n |            -----            |\n |   Foyer            Narrow   |")
    if currentRoom.name == "Foyer":
        print(" |     X      -----            |")
    elif currentRoom.name == "Narrow Passage":
        print(" |            -----      X     |")
    else:
        print(" |            -----            |")
    print(" |----|  |----|   |------------|\n      |  |\n |----|  |----|\n |            |\n |  Outside   |")
    if currentRoom.name == "Outside Cave Entrance":
        print(" |     X      |")
    else:
        print(" |            |")
    print(" |------------|\n")


# ---Version 2---
def drawmap2(): # This one uses fog --> rooms become discoverable
    print("               MAP\n")
    if room['overlook'].discovered == "false":
        if room['treasure'].discovered == "false":
            print("\n\n")
        else:
            print("                  |------------|\n                  |            |\n                  |  Treasure  |")
    else:
        if room['treasure'].discovered == "false":
            print(" |------------|\n |            |\n |  Overlook  |")
        else:
            print(" |------------|   |------------|\n |            |   |            |\n |  Overlook  |   |  Treasure  |")
    if currentRoom.name == "Grand Overlook":
        if room['treasure'].discovered == "false":
            print(" |     X      |")
        else:
            print(" |     X      |   |            |")
    elif currentRoom.name == "Treasure Chamber":
        if room['overlook'].discovered == "false":
            print("                  |      X     |")
        else:
            print(" |            |   |      X     |")
    else:
        if room['overlook'].discovered == "false":
            if room['treasure'].discovered == "false":
                print()
            else:
                print("                  |            |")
        else:
            if room['treasure'].discovered == "false":
                print(" |            |")
            else:
                print(" |            |   |            |")
    if room['overlook'].discovered == "false":
        if room['treasure'].discovered == "false":
            print("\n")
        else:
            print("                  |----|  |----|\n                       |  |")
    else:
        if room['treasure'].discovered == "false":
            print(" |----|  |----|\n      |  |")
        else:
            print(" |----|  |----|   |----|  |----|\n      |  |             |  |")
    if room['foyer'].discovered == "false":
        # Then the Narrow also hasn't been discovered
        print("\n\n")
    else:
        if room['narrow'].discovered == "false":
            print(" |----|  |----|\n |            --\n |   Foyer")
        else:
            print(" |----|  |----|   |----|  |----|\n |            -----            |\n |   Foyer            Narrow   |")
    if currentRoom.name == "Foyer":
        if room['narrow'].discovered == "false":
            print(" |     X      --")
        else:
            print(" |     X      -----            |")
    elif currentRoom.name == "Narrow Passage":
        # The Foyer must already be discovered, so no nested if-else statements needed
        print(" |            -----      X     |")
    else:
        # Test if either room had been discovered, like normal
        if room['foyer'].discovered == "false":
            # Then the Narrow also hasn't been discovered
            print()
        else:
            if room['narrow'].discovered == "false":
                print(" |            --")
            else:
                print(" |            -----            |")
    if room['foyer'].discovered == "false":
        # Then the Narrow also hasn't been discovered
        print("\n")
    else:
        if room['narrow'].discovered == "false":
            print(" |----|  |----|\n      |  |")
        else:
            print(" |----|  |----|   |------------|\n      |  |")
    print(" |----|  |----|\n |            |\n |  Outside   |")
    if currentRoom.name == "Outside Cave Entrance":
        print(" |     X      |")
    else:
        print(" |            |")
    print(" |------------|\n")



currentRoom = room["outside"]
direct = ""
while direct != 'q':
    clear()
    drawmap2()
    
    print(f"{currentRoom.name}")
    print(f"{currentRoom.description}")
    direct = input("Where to, boss? (n, s, e, w): ")
    if direct is 'n' or direct is 's' or direct is 'e' or direct is 'w':
        if direct is 'n':
            try:
                currentRoom = currentRoom.n_to
                print("Going to:", currentRoom.name)
                currentRoom.discovered = "true"
            except:
                print("Can't go there, boss.")
        elif direct is 's':
            try:
                currentRoom = currentRoom.s_to
                print("Going to:", currentRoom.name)
                currentRoom.discovered = "true"
            except:
                if currentRoom.name == "Outside Cave Entrance":
                    print("You wander around aimlessly outside.")
                else:
                    print("Can't go there, boss.")
        elif direct is 'e':
            try:
                currentRoom = currentRoom.e_to
                print("Going to:", currentRoom.name)
                currentRoom.discovered = "true"
            except:
                if currentRoom.name == "Outside Cave Entrance":
                    print("You wander around aimlessly outside.")
                else:
                    print("Can't go there, boss.")
        else:
            try:
                currentRoom = currentRoom.w_to
                print("Going to:", currentRoom.name)
                currentRoom.discovered = "true"
            except:
                if currentRoom.name == "Outside Cave Entrance":
                    print("You wander around aimlessly outside.")
                else:
                    print("Can't go there, boss.")
        input("Press ENTER to continue.")
    elif direct is 'q':
        pass
    else:
        print("I don't understand that direction. What alien map are you using? Please try again.")
        input("Press ENTER to continue.")
print("Thanks for playing")
