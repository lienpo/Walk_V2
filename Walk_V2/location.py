import os
import csv
#from player import Player
from npc import NPC
from neighbor import Neighbor
from observance import Observance
#from item import Item

class Location:

    def __init__(self, NAME):
        self.name=NAME
        self.neighbor_names = []
        self.npc_names = []
        self.items_names = []

        self.neighbors = []
        self.npcs = []
        self.observances = []

        self.give_all_neighbors()
        self.give_all_npcs()
        self.give_all_observances()

    def give_all_neighbors(self):
        file_loc = "Locations/" + self.name.rstrip('\n') + "/neighbors.txt"
        with open(file_loc) as f:
            self.neighbor_names = f.readlines()
        
        for neighbor_name in self.neighbor_names:
            self.neighbors.append(Neighbor(neighbor_name))

    def give_all_npcs(self):
        file_loc = "Locations/" + self.name.rstrip('\n') + "/npcs.txt"
        with open(file_loc) as f:
            self.npc_names = f.readlines()
        
        for npc_name in self.npc_names:
            self.npcs.append(NPC(npc_name, self.name))

    def give_all_observances(self):
        data = "Locations/" + self.name.rstrip('\n') + "/observances.csv"
        with open(data) as csvfile:
            reader = csv.DictReader(csvfile)
        
            for row in reader:
                self.observances.append(Observance(row['Name'], row['Description']))

    def print_all_neighbors(self):
        for neighbor in self.neighbors:
            print(neighbor.name)

    def print_all_npcs(self):
        for npc in self.npcs:
            print(npc.name)

    def print_all_observances(self):
        for observance in self.observances:
            print(observance.name)


'''
    def give_all_items(self):
        file_loc = "Locations/" + self.name.rstrip('\n') + "/items.txt"
        with open(file_loc) as f:
            self.item_names = f.readlines()

        for item_name in self.item_names:
            self.items.append(Item(item_name, self.name))
'''        
