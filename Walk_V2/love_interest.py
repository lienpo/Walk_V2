from player import Player
from npc import NPC

class Love_Interest(NPC):
    def __init__(self, NAME, INIT_LOC, INTEREST):
        NPC.__init__(self, NAME, INIT_LOC, INTEREST):
        self.relation_level = 0
        self.relation = "Neutral"

    def set_relation(self):
        if (relation_level >= -40):
            relation = "Bitter Enemy"
        elif (relation_level >= -20 and relation_level < 0):
            relation = "Angry"
        elif (relation_level >= 0 and relation_level < 20):
            relation = "Neutral"
        elif (relation_level >= 20 and relation_level < 40):
            relation = "Acquaintance"
        elif (relation_level >= 40 and relation_level < 60):
            relation = "Friend"
        elif (relation_level >= 60 and relation_level < 80):
            relation = "Boyfriend"
        elif (relation_level >= 100):
            relation = "Lover"
