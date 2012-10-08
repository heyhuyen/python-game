# Coin Flip

from random import randint
from time import sleep

dict = { 'head': 0, 'tails': 1}

def play():
    print "Let's flip a coin."
    
    while True:
        guess = raw_input("What's your guess?[head/tails]> ")
        if guess != "head" and guess!= "tails":
            print "Please guess 'head' or 'tails'"
        else:
            guess = dict[guess]
            print "Flipping coin..."
            sleep (2)
            outcome = randint(0,1)
            if outcome == dict['head']:
                print "Head."
            else:
                print "Tails."
            if guess == outcome:
                print "You win!"
                return 1
            else:
                print "You lose."
                return 0
    
