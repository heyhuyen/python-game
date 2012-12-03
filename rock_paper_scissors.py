# Simple Rock Paper Scissors Game
# adapted from Rosetta Code: http://rosettacode.org/wiki/Rock-paper-scissors#Python

import re
import string
from random import randint


class RockPaperScissors(object):
    
    def __init__(self):
        self.whatbeats = {'paper': 'scissors',
                'scissors': 'rock',
                'rock': 'paper'}
        self.objects = ("rock", "paper", "scissors")

    def get_winner(self, hand_a, hand_b):
        """ Compare hand_a and hand_b and return the winner. """
        if hand_b == self.whatbeats[hand_a]:
            return 1
        elif hand_a == self.whatbeats[hand_b]:
            return 0
        else:
            return -1

    def play(self):
        """ Loop to play a single round of rock, paper, scissors and returns win status. """
        print "Let's play rock, paper, scissors."
        
        while True:
            player_hand = str.lower(raw_input("Rock, paper, scissors, SHOOT!> "))
            
            if player_hand not in self.objects:
                print "What was that? Let's try again."
            else:
                computer_hand = self.objects[randint(0, 2)]
                winner = self.get_winner(player_hand, computer_hand)
                print "Your %s versus my %s." % (player_hand, computer_hand)
                if winner == -1:
                    print  "Draw."
                elif winner == 0:
                    print "You win!"
                    return 1
                else:
                    print "You lose."
                    return 0