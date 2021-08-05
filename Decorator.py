from abc import *

"""
class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,
            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()
"""

class AbstractEffect(ABC, Hero):
    
    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_stats(self):
        pass


class AbstractPositive(AbstractEffect):
    
    @abstractmethod
    def get_positive_effects(self):
        pass


class AbstractNegative(AbstractEffect):
    
    @abstractmethod
    def get_negative_effects(self):
        pass


class Berserk(AbstractPositive):

    def __init__(self, base):
        super(AbstractPositive, self).__init__(base)
        #self.base.positive_effects.append('Berserk')
        self.positive_effects = self.base.get_positive_effects()
        self.negative_effects = self.base.get_negative_effects()
        self.positive_effects.append('Berserk')
   
    def get_positive_effects(self):
        #self.positive_effects = self.base.get_positive_effects()
        #self.positive_effects.append('Berserk')
        #self.positive_effects = self.base.get_positive_effects()
        self = Berserk(self.base)
        return self.positive_effects.copy()

    def get_negative_effects(self):
        self = Berserk(self.base)
        return self.negative_effects.copy()

    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats['Strength'] += 7
        self.stats['Endurance'] += 7
        self.stats['Agility'] += 7
        self.stats['Luck'] += 7
        self.stats['Perception'] -= 3
        self.stats['Charisma'] -= 3
        self.stats['Intelligence'] -= 3
        self.stats['HP'] += 50
        return self.stats.copy()


class Blessing(AbstractPositive):

    def __init__(self, base):
        super(AbstractPositive, self).__init__(base)
        #self.stats = self.base.get_stats()
        #self.base.positive_effects.append('Blessing')
        self.positive_effects = self.base.get_positive_effects()
        self.negative_effects = self.base.get_negative_effects()
        self.positive_effects.append('Blessing')
        #self.stats['Strength'] += 2
        #self.stats['Endurance'] += 2
        #self.stats['Agility'] += 2
        #self.stats['Luck'] += 2
        #self.stats['Perception'] += 2
        #self.stats['Charisma'] += 2
        #self.stats['Intelligence'] += 2


    def get_positive_effects(self):
        #self.positive_effects = self.base.get_positive_effects()
        #self.positive_effects.append('Blessing')
        self = Blessing(self.base)
        return self.positive_effects.copy()

    def get_negative_effects(self):
        self = Blessing(self.base)
        return self.negative_effects.copy()

    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats['Strength'] += 2
        self.stats['Endurance'] += 2
        self.stats['Agility'] += 2
        self.stats['Luck'] += 2
        self.stats['Perception'] += 2
        self.stats['Charisma'] += 2
        self.stats['Intelligence'] += 2
        return self.stats.copy()


class Weakness(AbstractNegative):
    
    def __init__(self, base):
        super(AbstractNegative, self).__init__(base)
        #self.stats = self.base.get_stats()
        #self.base.negative_effects.append('Weakness')
        self.positive_effects = self.base.get_positive_effects()
        self.negative_effects = self.base.get_negative_effects()
        self.negative_effects.append('Weakness')
        #self.stats['Strength'] -= 4
        #self.stats['Endurance'] -= 4
        #self.stats['Agility'] -= 4


    def get_negative_effects(self):
        #self.negative_effects = self.base.get_negative_effects()
        #self.negative_effects.append('Weakness')
        self = Weakness(self.base)
        return self.negative_effects.copy()

    def get_positive_effects(self):
        self = Weakness(self.base)
        return self.positive_effects.copy()

    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats['Strength'] -= 4
        self.stats['Endurance'] -= 4
        self.stats['Agility'] -= 4
        return self.stats.copy()


class Curse(AbstractNegative):

    def __init__(self, base):
        super(AbstractNegative, self).__init__(base)
        #self.stats = self.base.get_stats()
        #self.base.negative_effects.append('Curse')
        self.positive_effects = self.base.get_positive_effects()
        self.negative_effects = self.base.get_negative_effects()
        self.negative_effects.append('Curse')
        #self.stats['Strength'] -= 2
        #self.stats['Endurance'] -= 2
        #self.stats['Agility'] -= 2
        #self.stats['Luck'] -= 2
        #self.stats['Perception'] -= 2
        #self.stats['Charisma'] -= 2
        #self.stats['Intelligence'] -= 2
  
    def get_negative_effects(self):
        #self.negative_effects = self.base.get_negative_effects()
        #self.negative_effects.append('Curse')
        self = Curse(self.base)
        return self.negative_effects.copy()

    def get_positive_effects(self):
        self = Curse(self.base)
        return self.positive_effects.copy()

    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats['Strength'] -= 2
        self.stats['Endurance'] -= 2
        self.stats['Agility'] -= 2
        self.stats['Luck'] -= 2
        self.stats['Perception'] -= 2
        self.stats['Charisma'] -= 2
        self.stats['Intelligence'] -= 2
        return self.stats.copy()


class EvilEye(AbstractNegative):

    def __init__(self, base):
        super(AbstractNegative, self).__init__(base)
        #self.stats = self.base.get_stats()
        #self.base.negative_effects.append('EvilEye')
        self.positive_effects = self.base.get_positive_effects()
        self.negative_effects = self.base.get_negative_effects()
        self.negative_effects.append('EvilEye')
        #self.stats['Luck'] -= 10

    
    def get_negative_effects(self):
        #self.negative_effects = self.base.get_negative_effects()
        #self.negative_effects.append('EvilEye')
        self = EvilEye(self.base)
        return self.negative_effects.copy()

    def get_positive_effects(self):
        self = EvilEye(self.base)
        return self.positive_effects.copy()

    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats['Luck'] -= 10
        return self.stats.copy()
