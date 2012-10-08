# Exercise 45: Make Your Own Game

from sys import exit
from random import randint

import characters
import levels

class Game(object):

    def __init__(self):
        self.player = characters.Player(1,10)
    
    def play(self):
        print "\n", "=" * 50
        print "Goal: Reach level 10!"
        print self.player.get_stats()
    
        while True:
            print "\n", "-" * 50
            
            if self.player.health < 0:
                self.game_over()
            elif self.player.level == 3:
                self.win()
            else:
                next_level = self.select_random_level()
                next_level.enter()
                print self.player.get_stats()
                keep_going = raw_input("Do you want to keep going?[y/n]> ")
                if keep_going == "n":
                    print "Thanks for playing!"
                    exit(2)
                        
    def win(self):
        print "Congratulations! You've won the game :)"
        exit(0)
        
    def game_over(self):
        print "GAME OVER"
        exit(1)
        
    def select_random_level(self):
        #level_key = randint(0,2)
        level_key = 2
        
        if level_key == 0:
            return levels.PuzzleLevel(self.player)
        elif level_key == 1:
            return levels.MonsterLevel(self.player)
        else:
            return levels.ChanceLevel(self.player)
        
a_game = Game()
a_game.play()