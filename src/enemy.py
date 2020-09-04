class Enemy:
    def __init__(self, name, qty, atk, dfns, spd, hp):
        # Note: I'm making this where if qty = 3, each one of the 3 has the same atk, dfns, spd, and hp values. Defeat all 3 to be credited with 1 win for Player
        # To that end, I will keep enemies dfns < player.wpn.atk, but I won't guarantee anything else
        # Simple Battle Concept:
        # Turns are determined by spd. First one to 25 gets to attack. Fastest spd for player = 10 ==> 3 loops (the extra 5 does NOT carry over)
        # In the event that both the player and the enemy reaches/passes 25 at the same time (i.e. Player accumulated 30 and enemy accumulated 27)...
        # The one with the highest value goes first
        #
        # Attacks: player.wpn.atk - enemy.dfns = damage dealt to enemy's HP
        # And enemy.atk - player.shld.dfns = damage dealt to player's HP (if enemy.atk < player.shld.dfns, damage = 0)
        #
        # If there are multiple enemies, player's attacks will only be applied to one enemy at a time until that enemy's HP <= 0
        # Then enemy.qty - 1, and enemy.HP resets to initial value given
        #
        # Fight continues until enemy.qty = 0 or player.hp <= 0
        self.name = name
        self.qty = qty
        self.atk = atk
        self.dfns = dfns
        self.spd = spd
        self.hp = hp