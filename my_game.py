# Exercise 45: Make Your Own Game

from sys import exit
from random import randint

import characters
import levels

class Game(object):

    def __init__(self):
        self.player = characters.Player(0,10)
    
    def play(self):
    	""" Loop to play a game. Player must reach level 10 to win without losing
    	all health or leveling down below 0.
    	"""
        print "\n", "=" * 50
        print "Goal: Reach level 10!"
        print self.player.get_stats()
    
        while True:
            print "\n", "-" * 50
            
            next_level = self.get_random_level()
            next_level.enter()
            print self.player.get_stats()
            if self.player.health < 0 or self.player.level < 0:
                self.die()
            elif self.player.level == 10:
                self.win()
            else:
                keep_going = raw_input("Do you want to keep going?[y/n]> ")
                if keep_going == "n":
                    print "Thanks for playing!"
                    exit(2)

    
    def win(self):
        print "~ ~ ~ Congratulations! You've won the game :) ~ ~ ~"
        exit(0)
        
    def die(self):
        print ">>>GAME OVER<<<"
        exit(1)
        
    def get_random_level(self):
        level_key = randint(1,2)
        #level_key = 2
        
        if level_key == 0:
            return levels.PuzzleLevel(self.player)
        elif level_key == 1:
            return levels.MonsterLevel(self.player)
        else:
            return levels.ChanceLevel(self.player)
        
a_game = Game()
a_game.play()