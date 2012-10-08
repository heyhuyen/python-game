# Coin Flip

from random import randint
from time import sleep
import re

    
class CoinFlip(object):
    
    def __init__(self):
        self.re_head = re.compile('heads?', re.IGNORECASE)
        self.re_tail = re.compile('tails?', re.IGNORECASE)
        
    def flip(self):
    	""" Flip a coin and return the outcome. """
        print "Flipping coin..."
        sleep (2)
        outcome = randint(0,1)
        if outcome == 1:
        	print "Tails."
        else:
        	print "Heads."
        return outcome
            
    def query(self):
    	""" Prompt user and return guess. """
    	while True:
			guess = raw_input("What's your guess?[heads/tails]> ")
			if self.re_head.match(guess):
				return 0
			elif self.re_tail.match(guess):
				return 1
			else:
				print "Pardon?"
    
    def play(self):
    	""" Loop to play a single round of Heads or Tails and returns win status. """
        print "Let's flip a coin."
        
        while True:
            guess = self.query()
            outcome = self.flip()
            if guess == outcome:
            	print "You guessed right!"
            	return 1
            else:
            	print "You guessed wrong."
            	return 0