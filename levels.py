# Game levels

from random import randint

import characters
import coin_flip
import rock_paper_scissors

class PuzzleLevel(object):
	
	def __init__(self, player):
		self.player = player
	

class MonsterLevel(object):

	def __init__(self, player):
		self.player = player

	
class ChanceLevel(object):
	
	def __init__(self, player):
		self.player = player
		
	def enter(self):
		room_type = randint(0,1)
		
		if room_type == 0:
			self.player.level += coin_flip.play()
		else:
			self.player.level += rock_paper_scissors.play()
		
	
		
		
		
