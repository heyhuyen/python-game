# Game characters including the player and monsters


class Player(object):

    def __init__(self, level, health):
        self.level = level
        self.health = health
        
    def get_stats(self):
        return "You are level %d and your health is %d." % (self.level, self.health)

class Monster(object):
    
    def __init__(self, level):
        #self.health = health 
        self.level = level
