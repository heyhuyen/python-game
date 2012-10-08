# Simple Rock Paper Scissors Game
# adapted from Rosetta Code: http://rosettacode.org/wiki/Rock-paper-scissors#Python

from random import randint

WHATBEATS = {'paper': 'scissors',
                'scissors': 'rock',
                'rock': 'paper'}

objects = ("rock", "paper", "scissors")

def determine_winner(hand_a, hand_b):
    if hand_b == WHATBEATS[hand_a]:
        return 1
    elif hand_a == WHATBEATS[hand_b]:
        return 0
    else:
        return -1
        
def play():
    print "Let's play rock, paper, scissors."
    
    while True:
        player_hand = raw_input("Rock, paper, scissors, SHOOT!> ")
        
        if player_hand not in objects:
            print "What was that? Let's try again."
        else:
            computer_hand = objects[randint(0, 2)]
            winner = determine_winner(player_hand, computer_hand)
        
            print "Your %s versus my %s." % (player_hand, computer_hand)
            if winner == -1:
                print  "Draw."
            elif winner == 0:
                print "You win!"
                return 1
            else:
                print "You lose."
            return 0