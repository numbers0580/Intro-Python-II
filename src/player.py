# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, startingRoom, coins):
        self.name = name
        self.currentRoom = startingRoom
        self.coins = coins
        self.item = [] # Not initialized as a parameter since player starts with 0 items
        self.atk = 1 # Default value for using fists
        self.dfns = 1 # Default value for blocking with limbs
        self.spd = 1 # Default value for moving without shoes
        self.hp = 100 # Default value for new players
        self.won = 0 # Tracks the number of enemies killed