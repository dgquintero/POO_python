from ctypes import cast


class Wizard:
    def __init__(self, name):
        self.name = name
        self.__mana = 45
        self.__health = 65
    
    def get_mana(self):
        return self.__mana
    
    def get_health(self):
        return self.__health

    def get_fireball(self):
        self.__health -= 30
        print('%s is hit by a fireball' % self.name)
        if self.__health <= 0:
            print('%s is dead' % self.name)
    
    def drink_mana_potion(self):
      print ('%s drinks a mana potion' % self.name)
      self.__mana += 40

    def cast_fireball(self, target):
        if self.__mana >= 20:
            self.__mana -= 20
            print('%s casts a fireball at %s' % (self.name, target.name))
            target.get_fireball()
        else:
            print('%s connot cast fireball' % self.name)
    

