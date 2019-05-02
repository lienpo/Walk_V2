from observance import Observance
from player import Player

class Item(Observance):
    def __init__(self, NAME, DESCRIPTION, IS_ITEM = True, EFFECT_CODE):
        Item.__init__(self, NAME, DESCRIPTION, IS_ITEM)
        self.effect_code = EFFECT_CODE
    
    def (self, Player, 
