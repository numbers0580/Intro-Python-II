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
    'dagger': Item("Chipped Dagger", "A worn but still serviceable blade.", 5, 0, 0, 0),
    'buckler': Item("Wooden Buckler", "A simple shield to hide behind. And look, only 3 termites!", 0, 4, 0, 0),
    'hatchet': Item("Small Hatchet", "Not much reach, but well-balanced.", 6, 0, 0, 0),
    'sandals': Item("Discarded Sandals", "A free donation from the previous dinner guest.", 0, 0, 3, 0),
    'burger': Item("Partially-eaten Hamburger", "Only one bite taken. What a find!", 0, 0, 0, 20),
    'aegis': Item("Aegis Shield", "An ancient round shield from a lost civilization", 0, 10, 0, 0),
    'boots': Item("Leather Boots", "They're only slightly smelly!", 0, 0, 8, 0),
    'club': Item("Table Leg", "A broken part of a table. Would make a good club, though", 3, 0, 0, 0),
    'gladius': Item("Gladius", "A well-made, lightweight short-sword from an ancient civilization.", 10, 0, 0, 0),
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
roomitem = Item("NONE", "N/A", 0, 0, 0, 0)
while direct != 'q':
    # Clears the Console screen before re-drawing
    clear()

    # Checks player's current position, checks rooms discovery states, and redraws the map accordingly
    drawmap2()
    # drawmap1() # This version of the map doesn't have a fog algorithm, it just shows the entire map
    
    # print(f"TESTING ITEM FOUND: {roomitem.name}") # Works!
    print(f"{myhero.name} is in the {myhero.currentRoom.name}\n{myhero.currentRoom.description}\n")
    myweap = myhero.wpn.name
    myshield = myhero.shld.name
    myshoes = myhero.shoe.name

    print(f"Equipped: {myhero.wpn.name},  {myhero.shld.name},  {myhero.shoe.name}")
    print(f"ATK: {myhero.wpn.atk}, DEF: {myhero.shld.dfns}, SPD: {myhero.shoe.spd}, HP: {myhero.hp}, COINS: {myhero.coins}     ENEMIES DEFEATED: {myhero.won}/20\n")

    # Checks for any random items (Weapons, Shields, Shoes, Food)
    if roomitem.name != "NONE" and myhero.currentRoom.name != "Outside Cave Entrance":
        if roomitem.name == "Table Leg" or roomitem.name == "Chipped Dagger" or roomitem.name == "Small Hatchet" or roomitem.name == "Gladius":
            print(f"As you make your way through the mess, you find: {roomitem.name} -- ATK: {roomitem.atk}")
        elif roomitem.name == "Wooden Buckler" or roomitem.name == "Aegis Shield":
            print(f"As you make your way through the mess, you find: {roomitem.name} -- DEF: {roomitem.dfns}")
        elif roomitem.name == "Discarded Sandals" or roomitem.name == "Leather Boots":
            print(f"As you make your way through the mess, you find: {roomitem.name} -- SPD: {roomitem.spd}")
        else:
            print(f"As you make your way through the mess, you find: {roomitem.name} -- HP: {roomitem.hp}")
    else:
        # This is only really checking to make sure the player is not Outside. Removing random item if so
        roomitem = Item("NONE", "N/A", 0, 0, 0, 0)

    # Checks for any random coins in the room
    if randcoins > 0:
        if randcoins == 1:
            print(f"You see {randcoins} coin glinting in the distance.")
        else:
            print(f"You see {randcoins} coins glinting in the distance.")

    # R - Read input
    # q - quit
    direct = input("Where to, boss? (n, s, e, w, c, i, q: ")
    # E - Evaluate
    if direct is 'n' or direct is 's' or direct is 'e' or direct is 'w' or direct is 'c' or direct is 'i':
        tempcoins = 0 # Initially sets coins to 0 just in case fortune randomizer doesn't generate any coins
        tempitem = Item("NONE", "N/A", 0, 0, 0, 0) # Initially sets tempitem to Nothing just in case fortune randomizer doesn't create an item

        fortune = random.randint(1, 8) # Re-adjusted odds to make combined chance of finding items or coins = 50% total

        if fortune is 7: # Arbitrary random number value to luckily find coins. Odds at 25% of the above 50% = 12.5%
            tempcoins = random.randint(1, 25)

        if fortune is 2 or fortune is 5: # Arbitrary random number values. Odds at 50% of the above 50% = 25%
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
        if direct is 'n':
            try:
                myhero.currentRoom = myhero.currentRoom.n_to
                # P - Print
                print("Going to:", myhero.currentRoom.name)
                myhero.currentRoom.discovered = "true"
                randcoins = tempcoins
                roomitem = tempitem
                # Note to future self: The 3 lines of code below placed here in "try" ALWAYS ended up running the "except" fpr some reason
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
                roomitem = tempitem
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
                roomitem = tempitem
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
                roomitem = tempitem
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
        elif direct is 'i':
            if roomitem.name == "NONE":
                print(f"There's nothing left to find here, boss.")
            else:
                if roomitem.name == myweap or roomitem.name == myshield or roomitem.name == myshoes:
                    print(f"You already have the {roomitem.name} equipped.")
                else:
                    print(roomitem.description)
                    if roomitem.name == "Table Leg" or roomitem.name == "Chipped Dagger" or roomitem.name == "Small Hatchet" or roomitem.name == "Gladius":
                        diff = roomitem.atk - myhero.wpn.atk
                        print(f"The {roomitem.name} can be used as a weapon. Your attack increased by {diff}")
                        myhero.wpn = roomitem
                    elif roomitem.name == "Wooden Buckler" or roomitem.name == "Aegis Shield":
                        diff = roomitem.dfns - myhero.shld.dfns
                        print(f"The {roomitem.name} can be used as a shield. Your defense increased by {diff}")
                        myhero.shld = roomitem
                    elif roomitem.name == "Discarded Sandals" or roomitem.name == "Leather Boots":
                        diff = roomitem.spd - myhero.shoe.spd
                        print(f"You can wear the {roomitem.name}. Your speed increased by {diff}")
                        myhero.shoe = roomitem
                    else:
                        diff = 100 - myhero.hp
                        if roomitem.hp > diff:
                            print(f"You consume the {roomitem.name}, but you can only recover {diff} HP")
                            myhero.hp = 100
                        else:
                            print(f"You consume the {roomitem.name} and recover {roomitem.hp} HP")
                            myhero.hp += roomitem.hp
                    roomitem = Item("NONE", "N/A", 0, 0, 0, 0) # removes item from the room
                    tempitem = Item("NONE", "N/A", 0, 0, 0, 0) # prevents removed item from re-appearing if player chooses to walk into a wall
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
                randcoins = 0 # removes coins from the room
                tempcoins = 0 # prevents removed coins from re-appearing
        input("Press ENTER to continue.")
    elif direct is 'q':
        pass
    else:
        # P - Print
        print("I don't understand that direction. What alien map are you using? Please try again.")
        input("Press ENTER to continue.")
        # L - Loop back to step 1
print("Thanks for playing")
