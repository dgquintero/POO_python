class Archer:
    def __init__(self, num_arrows, health, name):
        self.num_arrows = num_arrows
        self.health = health
        self.name = name
    
    def get_shot(self):
      if self.health is not None and self.health > 0:
        self.health -= 1

      else:
        print('%s is dead' % self.name)
    
    def shoot(self, target):
      if self.num_arrows is not None and self.num_arrows > 0:
        self.num_arrows -= 1
        print ('%s shoots %s' % (self.name, target.name))
        target.get_shot()
      else:
        print('%s cant shoot' % self.name)

