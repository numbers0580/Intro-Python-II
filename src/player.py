# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
    def __init__(self, name, startingRoom, coins):
        self.name = name
        self.currentRoom = startingRoom
        self.coins = coins
        #self.item = [] # Not initialized as a parameter since player starts with 0 items # NOT CURRENTLY USING, BUT I MAY CHANGE MY MIND
        self.wpn = Item("Fists", "N/A", 3, 0, 0, 0)
        self.shld = Item("Body", "N/A", 0, 2, 0, 0)
        self.shoe = Item("Bare Feet", "N/A", 0, 0, 3, 0)
        #self.atk = 1 # Default value for using fists
        #self.dfns = 1 # Default value for blocking with limbs
        #self.spd = 1 # Default value for moving without shoes
        self.hp = 100 # Default value for new players
        self.won = 0 # Tracks the number of enemies killed