import random
import math
from os import system, name
from room import Room
from player import Player
from item import Item
from enemy import Enemy

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
    'dagger': Item("Chipped Dagger", "A worn but still serviceable blade.", 8, 0, 0, 0),
    'buckler': Item("Wooden Buckler", "A simple shield to hide behind. And look, only 3 termites!", 0, 5, 0, 0),
    'hatchet': Item("Small Hatchet", "Not much reach, but well-balanced.", 10, 0, 0, 0),
    'sandals': Item("Discarded Sandals", "A free donation from the previous dinner guest.", 0, 0, 5, 0),
    'burger': Item("Partially-eaten Hamburger", "Only one bite taken. What a find!", 0, 0, 0, 20),
    'aegis': Item("Aegis Shield", "An ancient round shield from a lost civilization", 0, 10, 0, 0),
    'boots': Item("Leather Boots", "They're only slightly smelly!", 0, 0, 9, 0),
    'club': Item("Table Leg", "A broken part of a table. Would make a good club, though", 5, 0, 0, 0),
    'gladius': Item("Gladius", "A well-made, lightweight short-sword from an ancient civilization.", 15, 0, 0, 0),
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



each_hp = 0
def fightevent():
    # Enemy Names:
    # Skeleton, Bat, Goblin, Rat, Spider, Vampire, Possessed Dolls
    currentenemy = Enemy("NONE", 0, 0, 0, 0, 0) # Name, Qty, Atk, Dfns, Spd, HP
    setname = ""

    e_name = random.randint(1, 3)
    e_atk = 0
    e_def = 0

    if myhero.wpn.atk < 6:
        # Bats, Rats, Spiders
        e_atk = random.randint(1, 4)
        e_def = random.randint(0, 2)
        if e_name is 1:
            setname = "Bat"
        elif e_name is 2:
            setname = "Rat"
        else:
            setname = "Spider"
    elif myhero.wpn.atk >= 6 and myhero.wpn.atk < 11:
        # Spiders, Goblins, Possessed Dolls
        e_atk = random.randint(2, 8)
        e_def = random.randint(1, 5)
        if e_name is 1:
            setname = "Spider"
        elif e_name is 2:
            setname = "Goblin"
        else:
            setname = "Possessed Doll"
    else:
        # Possessed Dolls, Vampires, Skeletons
        e_atk = random.randint(5, 10)
        e_def = random.randint(3, 8)
        if e_name is 1:
            setname = "Possessed Doll"
        elif e_name is 2:
            setname = "Skeleton"
        else:
            setname = "Vampire"

    e_hp = 0
    e_qty = 0
    if setname is "Bat" or setname is "Rat":
        e_hp = random.randint(5, 12)
        e_qty = random.randint(2, 4)
    elif setname is "Spider":
        e_hp = random.randint(8, 18)
        e_qty = random.randint(2, 3)
    elif setname is "Goblin" or setname is "Possessed Doll":
        e_hp = random.randint(13, 21)
        e_qty = random.randint(1, 3)
    else:
        e_hp = random.randint(17, 26)
        e_qty = random.randint(1, 2)

    if e_def >= myhero.wpn.atk:
        e_def = myhero.wpn.atk - 1

    currentenemy = Enemy(setname, e_qty, e_atk, e_def, random.randint(1, int(myhero.shoe.spd * 2.5)), e_hp)

    # 3 lines of code below works!
    print(f"Test Enemy: name = {currentenemy.name}, qty = {currentenemy.qty}, atk = {currentenemy.atk}, def = {currentenemy.dfns}, spd = {currentenemy.spd}, hp = {currentenemy.hp}")
    #input("Press ENTER to clear.")
    #clear()

    print(f"You encounter {currentenemy.qty} {currentenemy.name}(s) that don't look friendly.\nThe narrator will hide and make some bets. Good luck!")
    input("Press ENTER to continue to the FIGHT!")

    playermeter = 0
    enemymeter = 0

    global each_hp
    each_hp = currentenemy.hp

    while currentenemy.qty > 0 and myhero.hp > 0:
        playermeter += myhero.shoe.spd
        enemymeter += currentenemy.spd

        if playermeter >= 25 or enemymeter >= 25:
            if playermeter >= enemymeter:
                print("Player initiates an attack")
                currentenemy = playerattacks(currentenemy, playermeter, enemymeter)

                if enemymeter >= 25 and currentenemy.qty > 0:
                    print("Enemy attacks next in the same turn")
                    currentenemy = playerdefends(currentenemy, playermeter, enemymeter)

            else:
                print("Enemy initiates an attack")
                currentenemy = playerdefends(currentenemy, playermeter, enemymeter)

                if playermeter >= 25 and myhero.hp > 0:
                    print("Player attacks next in the same turn")
                    currentenemy = playerattacks(currentenemy, playermeter, enemymeter)

            if playermeter >= 25:
                playermeter = 0

            if enemymeter >= 25:
                enemymeter = 0

            if currentenemy.qty is 0:
                print(f"You defeated all of the {currentenemy.name}(s). Congratulations! You win!")
                myhero.won += 1

            if myhero.hp <= 0:
                print(f"Unfortunately, you died an embarassingly inglorious death at the hands of {currentenemy.name}s")
                print("Game Over!")

    input("Fight ended. Press ENTER to continue.")




def playerattacks(currentenemy, pm, em):
    global each_hp
    atkchoice = ''
    atksuccess = 0
    tempatk = 0
    clear()
    print(f"{myhero.name}: HP: {myhero.hp}, Atk: {myhero.wpn.atk}, Def: {myhero.shld.dfns}, Spd: {myhero.shoe.spd}, Energy: {pm}")
    print(f"{currentenemy.name}(s) x{currentenemy.qty}: HP: {each_hp}, Atk: {currentenemy.atk}, Def: {currentenemy.dfns}, Spd: {currentenemy.spd}, Energy: {em}")
    while atkchoice != '1' and atkchoice != '2':
        print("Player Attack Choices:")
        print("1: Normal Attack (Guaranteed hit)")
        print("2: Try for Critical Attack (bonus 50% attack, but might miss)")
        atkchoice = input()
    enemychoice_d = random.randint(1, 5)

    if atkchoice is '2':
        atksuccess = random.randint(1, 3)

    edefsuccess = 0
    etempdef = 0
    if enemychoice_d is 3:
        edefsuccess = random.randint(1, 3)

    if edefsuccess is 0:
        etempdef = currentenemy.dfns
    elif edefsuccess is 1:
        etempdef = math.ceil(currentenemy.dfns * 0.5)
    else:
        etempdef = math.ceil(currentenemy.dfns * 1.5)
    
    if atksuccess is 0:
        tempatk = myhero.wpn.atk
        print(f"You go for a normal attack using {myhero.wpn.name}.")
        if edefsuccess is 0:
            print(f"The {currentenemy.name} opts for a normal Defense")
        elif edefsuccess is 1:
            print(f"The {currentenemy.name} slips on their Defense Posture, leaving them open")
        else:
            print(f"The {currentenemy.name} strngthens their Defense")
    elif atksuccess is 2 or atksuccess is 3:
        tempatk = math.ceil(myhero.wpn.atk * 1.5)
        print(f"You go for a critical attack using {myhero.wpn.name}.")
        if edefsuccess is 0:
            print()
        elif edefsuccess is 1:
            print(f"The {currentenemy.name} slips on their Defense Posture, leaving them open")
        else:
            print(f"The {currentenemy.name} strngthens their Defense")
    else:
        print(f"You go for the attack with your {myhero.wpn.name}, and... You missed! How could you miss?")

    dmg = tempatk - etempdef
    if dmg < 0:
        dmg = 0
    
    if atksuccess != 1:
        print(f"You strike the {currentenemy.name} for {dmg} points of damage.")

    each_hp -= dmg
    if each_hp > 0:
        print(f"The {currentenemy.name} grins back at you tauntingly.")
    else:
        print(f"You killed 1 {currentenemy.name}")
        currentenemy.qty -= 1
        each_hp = currentenemy.hp
        if currentenemy.qty > 0:
            print(f"There's still {currentenemy.qty} {currentenemy.name}(s) left to go.")

    input("Press ENTER to continue.")

    return currentenemy



def playerdefends(currentenemy, pm, em):
    global each_hp
    defchoice = ''
    defsuccess = 0
    tempdef = 0
    clear()
    print(f"{myhero.name}: HP: {myhero.hp}, Atk: {myhero.wpn.atk}, Def: {myhero.shld.dfns}, Spd: {myhero.shoe.spd}, Energy: {pm}")
    print(f"{currentenemy.name}(s) x{currentenemy.qty}: HP: {each_hp}, Atk: {currentenemy.atk}, Def: {currentenemy.dfns}, Spd: {currentenemy.spd}, Energy: {em}")
    while defchoice != '1' and defchoice != '2' and defchoice != '3':
        print("Player Defense Choices:")
        print("1: Normal")
        print("2: Defense Posture (chance to increase DEF by 50%, but might reduce DEF by 50%)")
        print("3: Try to Evade (chance enemy will miss entirely, but hits will ignore your DEF)")
        defchoice = input()
    enemychoice_a = random.randint(1, 5)

    if defchoice is '2':
        defsuccess = random.randint(1, 3)
    if defchoice is '3':
        defsuccess = random.randint(4, 6)
    
    eatksuccess = 0
    etempatk = 0
    if enemychoice_a is 3:
        eatksuccess = random.randint(1, 3)

    if defsuccess is 0:
        tempdef = myhero.shld.dfns
    elif defsuccess is 1:
        tempdef = math.ceil(myhero.shld.dfns * 0.5)
    elif defsuccess is 2 or defsuccess is 3:
        tempdef = math.ceil(myhero.shld.dfns * 1.5)
    elif defsuccess is 4:
        tempdef = 0
    else:
        pass

    if eatksuccess is 0:
        etempatk = currentenemy.atk
        print(f"The {currentenemy.name} goes for a normal attack.")
        if defsuccess is 0:
            print()
        elif defsuccess is 1:
            print("You alter your Defense Posture, but got stuck on an exposed rock, leaving you open.")
        elif defsuccess is 2 or defsuccess is 3:
            print("You successfully alter your Defense Posture to brace for the attack.")
        elif defsuccess is 4:
            print("As you try to evade the attack, you slam face-first into a door.")
        else:
            print(f"You swear you were able to predict where the {currentenemy.name}'s attack would land and deftly evaded it.")
    elif eatksuccess is 2 or eatksuccess is 3:
        etempatk = math.ceil(currentenemy.atk * 1.5)
        print(f"The {currentenemy.name} goes for a critical attack.")
        if defsuccess is 0:
            print()
        elif defsuccess is 1:
            print("You alter your Defense Posture, but got stuck on an exposed rock, leaving you open.")
        elif defsuccess is 2 or defsuccess is 3:
            print("You successfully alter your Defense Posture to brace for the attack.")
        elif defsuccess is 4:
            print("As you try to evade the attack, you slam face-first into a door.")
        else:
            print(f"You swear you were able to predict where the {currentenemy.name}'s attack would land and deftly evaded it.")
    else:
        print(f"The {currentenemy.name} comes in for the attack, and... misses!")

    edmg = etempatk - tempdef
    if edmg < 0 or defsuccess is 5 or defsuccess is 6:
        edmg = 0

    myhero.hp -= edmg

    input("Press ENTER to continue.")

    return currentenemy





# currentRoom = room["outside"]
direct = ""
randcoins = 0
roomitem = Item("NONE", "N/A", 0, 0, 0, 0)
while direct != 'q' and myhero.hp > 0:
    fightchance = random.randint(1, 10)
    if fightchance is 3 and myhero.currentRoom.name != "Outside Cave Entrance":
        fightevent()

    if myhero.hp > 0:
        #Clear screen after potential fight and before redrawing map
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
        direct = input("Where to, boss? (n, s, e, w, c, i, q): ")
        # E - Evaluate
        if direct is 'n' or direct is 's' or direct is 'e' or direct is 'w' or direct is 'c' or direct is 'i':
            tempcoins = 0 # Initially sets coins to 0 just in case fortune randomizer doesn't generate any coins
            tempitem = Item("NONE", "N/A", 0, 0, 0, 0) # Initially sets tempitem to Nothing just in case fortune randomizer doesn't create an item

            fortune = random.randint(1, 8) # Re-adjusted odds to make combined chance of finding items or coins = 50% total

            if fortune is 7: # Arbitrary random number value to luckily find coins. Odds at 25% of the above 50% = 12.5%
                tempcoins = random.randint(1, 25)

            if fortune is 2 or fortune is 5: # Arbitrary random number values. Odds at 50% of the above 50% = 25%
                #25, 12, 8, 5 -- 30, 10 -- 30, 15 -- 80, 35 = 250
                whichitem = random.randint(1, 250)
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
                elif whichitem >= 136 and whichitem <= 215:
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
                    # Note to future self: The 3 lines of code below placed here in "try" ALWAYS ended up running the "except" for some reason
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
