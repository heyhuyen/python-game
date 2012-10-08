# Game levels

from random import randint
from time import sleep
import string

import characters
import coin_flip
import rock_paper_scissors


class PuzzleLevel(object):
    
    def __init__(self, player):
        self.player = player
    

class MonsterLevel(object):

    def __init__(self, player):
        self.player = player
        
    def enter(self):
        monster = characters.Monster(randint(1,10))
        print "Oh no! Looks like you've run into a monster. It's level is %d." % monster.level
        if monster.level >= self.player.level:
            next = str.lower(raw_input("It's too strong for you, there's no way you can defeat it. Run away or fight? "))
            if "run" in next:
                escape = randint(1,6)
                if escape >= 4:
                    print "Phew, that was close but you're safe for now..."
                else:
                    print "You try to run, but the monster takes a hit at you. -2 health"
                    self.player.health -= 2
            elif "fight" in next:
                kill_monster = randint(1,10)
                if kill_monster >= 8:
                    print "By a miracle, you defeat the monster! +2 level up!"
                    self.player.level += 2
                else:
                    print "It was a valiant effort but you were no match for this beast."
                    print "-1 level down, -4 health"
                    self.player.level -=1
                    self.player.health -= 4
        else:
            print "The monster is no match for your greatness. +1 level up!"
            self.player.level += 1

    
class ChanceLevel(object):
    
    def __init__(self, player):
        self.player = player
        
    def enter(self):
        key = randint(0,1)
        minigame = self.get_minigame(key)
        win = minigame.play()
        if win == 1:
        	print "+1 level up."
    		self.player.level += 1
    
    def get_minigame(self, key):
    	if key == 0:
        	return coin_flip.CoinFlip()
        else:
            return rock_paper_scissors.RPS()
            
        
    
        
        
        
