import random
from os import system, name
from room import Room
from player import Player
from item import Item

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

# I commented out the line below because upon further examination, I found the depts -> store model in lecture doesn't apply to room -> player
# mygame = Player("Jacks Treasure Hunt", [room["outside"], room["foyer"], room["overlook"], room["narrow"], room["treasure"]])
# However, I do think the depts -> store model applies to item -> room for this game
item = {
    'dagger': Item("Chipped Dagger", "A worn but still serviceable blade.", 4, 0, 0, 0),
    'buckler': Item("Wooden Buckler", "A simple shield to hide behind. And look, only 3 termites!", 0, 3, 0, 0),
    'hatchet': Item("Small Hatchet", "Not much reach, but well-balanced.", 5, 0, 0, 0),
    'sandals': Item("Discarded Sandals", "A free donation from the previous dinner guest.", 0, 0, 3, 0),
    'burger': Item("Partially-eaten Hamburger", "Only one bite taken. What a find!", 0, 0, 0, 20),
    'aegis': Item("Aegis Shield", "An ancient round shield from a lost civilization", 0, 10, 0, 0),
    'boots': Item("Leather Boots", "They're only slightly smelly!", 0, 0, 8, 0),
    'club': Item("Table Leg", "A broken part of a table. Would make a good club, though", 3, 0, 0, 0),
    'gladius': Item("Gladius", "A well-made, lightweight short-sword from an ancient civilization.", 9, 0, 0, 0),
    'milkshake': Item("Warm leftover Milkshake", "Don't think too much about it. Just pinch your nose and enjoy!", 0, 0, 0, 10)
}

# Make a new player object that is currently in the 'outside' room.
myhero = Player("Jack", room["outside"], 0)

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
# |            |---|            |
# |   Foyer            Narrow   |
# |            |---|            |
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
    if myhero.currentRoom.name == "Grand Overlook":
        print(" |     X      |   |            |")
    elif myhero.currentRoom.name == "Treasure Chamber":
        print(" |            |   |      X     |")
    else:
        print(" |            |   |            |")
    print(" |----|  |----|   |----|  |----|\n      |  |             |  |\n |----|  |----|   |----|  |----|\n |            |---|            |\n |   Foyer            Narrow   |")
    if myhero.currentRoom.name == "Foyer":
        print(" |     X      |---|            |")
    elif myhero.currentRoom.name == "Narrow Passage":
        print(" |            |---|      X     |")
    else:
        print(" |            |---|            |")
    print(" |----|  |----|   |------------|\n      |  |\n |----|  |----|\n |            |\n |  Outside   |")
    if myhero.currentRoom.name == "Outside Cave Entrance":
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
    if myhero.currentRoom.name == "Grand Overlook":
        if room['treasure'].discovered == "false":
            print(" |     X      |")
        else:
            print(" |     X      |   |            |")
    elif myhero.currentRoom.name == "Treasure Chamber":
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
            print(" |----|  |----|\n |            |-\n |   Foyer")
        else:
            print(" |----|  |----|   |----|  |----|\n |            |---|            |\n |   Foyer            Narrow   |")
    if myhero.currentRoom.name == "Foyer":
        if room['narrow'].discovered == "false":
            print(" |     X      |-")
        else:
            print(" |     X      |---|            |")
    elif myhero.currentRoom.name == "Narrow Passage":
        # The Foyer must already be discovered, so no nested if-else statements needed
        print(" |            |---|      X     |")
    else:
        # Test if either room had been discovered, like normal
        if room['foyer'].discovered == "false":
            # Then the Narrow also hasn't been discovered
            print()
        else:
            if room['narrow'].discovered == "false":
                print(" |            |-")
            else:
                print(" |            |---|            |")
    if room['foyer'].discovered == "false":
        # Then the Narrow also hasn't been discovered
        print("\n")
    else:
        if room['narrow'].discovered == "false":
            print(" |----|  |----|\n      |  |")
        else:
            print(" |----|  |----|   |------------|\n      |  |")
    print(" |----|  |----|\n |            |\n |  Outside   |")
    if myhero.currentRoom.name == "Outside Cave Entrance":
        print(" |     X      |")
    else:
        print(" |            |")
    print(" |------------|\n")



# currentRoom = room["outside"]
direct = ""
randcoins = 0
roomitem = Item("DEFAULT", "N/A", 0, 0, 0, 0)
while direct != 'q':
    clear()
    drawmap2()
    
    print(f"TESTING ITEM FOUND: {roomitem.name}")
    print(f"{myhero.name} is in the {myhero.currentRoom.name}\n{myhero.currentRoom.description}\n")
    myweap = "NONE"
    myshield = "NONE"
    myshoes = "NONE"
    for inv in myhero.item:
        if inv.name is "Chipped Dagger" or inv.name is "Small Hatchet" or inv.name is "Table Leg" or inv.name is "Gladius":
            myweap = inv.name
        if inv.name is "Wooden Buckler" or inv.name is "Aegis Shield":
            myshield = inv.name
        if inv.name is "Discarded Sandals" or inv.name is "Leather Boots":
            myshoes = inv.name
    print(f"Equipped: {myweap},  {myshield},  {myshoes}")
    print(f"ATK: {myhero.atk}, DEF: {myhero.dfns}, SPD: {myhero.spd}, HP: {myhero.hp}, COINS: {myhero.coins}     ENEMIES DEFEATED: {myhero.won}/20\n")
    if randcoins > 0:
        if randcoins == 1:
            print(f"You see {randcoins} coin glinting in the distance.")
        else:
            print(f"You see {randcoins} coins glinting in the distance.")
    # R - Read input
    direct = input("Where to, boss? (n, s, e, w, c, i): ")
    # E - Evaluate
    if direct is 'n' or direct is 's' or direct is 'e' or direct is 'w' or direct is 'c' or direct is 'i':
        tempcoins = 0
        tempitem = Item("NONE", "N/A", 0, 0, 0, 0)

        fortune = random.randint(1, 4)
        founditem = random.randint(1, 2)

        if fortune == 4:
            tempcoins = random.randint(1, 25)

        if founditem == 2:
            #25, 12, 8, 5 -- 30, 10 -- 30, 15 -- 50, 15 = 200
            whichitem = random.randint(1, 200)
            if whichitem >= 1 and whichitem <= 25:
                tempitem = item['club']
            elif whichitem >= 26 and whichitem <= 37:
                tempitem = item['dagger']
            elif whichitem >= 38 and whichitem <= 45:
                tempitem = item['hatchet']
            elif whichitem >= 46 and whichitem <= 50:
                tempitem = item['gladius']
            elif whichitem >= 51 and whichitem <= 80:
                tempitem = item['buckler']
            elif whichitem >= 81 and whichitem <= 90:
                tempitem = item['aegis']
            elif whichitem >= 91 and whichitem <= 120:
                tempitem = item['sandals']
            elif whichitem >= 121 and whichitem <= 135:
                tempitem = item['boots']
            elif whichitem >= 136 and whichitem <= 185:
                tempitem = item['milkshake']
            else:
                tempitem = item['burger']
        roomitem = tempitem
        if direct is 'n':
            try:
                myhero.currentRoom = myhero.currentRoom.n_to
                # P - Print
                print("Going to:", myhero.currentRoom.name)
                myhero.currentRoom.discovered = "true"
                randcoins = tempcoins
                #fortune = randint(1, 4)
                #if fortune == 4:
                #    randcoins = randint(1, 25)
            except:
                # P - Print
                print("Can't go there, boss.")
        elif direct is 's':
            try:
                myhero.currentRoom = myhero.currentRoom.s_to
                # P - Print
                print("Going to:", myhero.currentRoom.name)
                myhero.currentRoom.discovered = "true"
                randcoins = tempcoins
                #fortune = randint(1, 4)
                #if(fortune == 4):
                #    randcoins = randint(1, 25)
            except:
                if myhero.currentRoom.name == "Outside Cave Entrance":
                # P - Print
                    print(f"{myhero.name} wanders around aimlessly outside.")
                else:
                # P - Print
                    print("Can't go there, boss.")
        elif direct is 'e':
            try:
                myhero.currentRoom = myhero.currentRoom.e_to
                # P - Print
                print("Going to:", myhero.currentRoom.name)
                myhero.currentRoom.discovered = "true"
                randcoins = tempcoins
                #fortune = randint(1, 4)
                #if(fortune == 4):
                #    randcoins = randint(1, 25)
            except:
                if myhero.currentRoom.name == "Outside Cave Entrance":
                # P - Print
                    print(f"{myhero.name} wanders around aimlessly outside.")
                else:
                # P - Print
                    print("Can't go there, boss.")
        elif direct is 'w':
            try:
                myhero.currentRoom = myhero.currentRoom.w_to
                # P - Print
                print("Going to:", myhero.currentRoom.name)
                myhero.currentRoom.discovered = "true"
                randcoins = tempcoins
                #fortune = randint(1, 4)
                #if(fortune == 4):
                #    randcoins = randint(1, 25)
            except:
                if myhero.currentRoom.name == "Outside Cave Entrance":
                # P - Print
                    print(f"{myhero.name} wanders around aimlessly outside.")
                else:
                # P - Print
                    print("Can't go there, boss.")
        else:
            if randcoins == 0:
                # Did this first, so it won't run immediately AFTER player picks up the coins
                print(f"There are no coins left unscavenged in this room.")
            else:
                # player picks up the coins
                if randcoins == 1:
                    print(f"{myhero.name} picks up the {randcoins} coin")
                else:
                    print(f"{myhero.name} picks up the {randcoins} coins")
                myhero.coins += randcoins
                randcoins = 0
                tempcoins = 0
        input("Press ENTER to continue.")
    elif direct is 'q':
        pass
    else:
        # P - Print
        print("I don't understand that direction. What alien map are you using? Please try again.")
        input("Press ENTER to continue.")
        # L - Loop back to step 1
print("Thanks for playing")
