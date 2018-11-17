'''
    Figure class
'''
import random

class Figure:
    '''
        name: Figure's name
        birth_year: year of Figure's birth
        obsessions: list of things Figure may become obsessed with, which will affect any pieces of art they make, etc...
        faction_list: list of factions
        factions: dictionary of factions and their respective reputation with the Figure
        allied_factions: list of all factions with a positive reputation
        enemy_factions: list of all factions with a negative reputation
        events: list of events that shape the Figure
    '''
    def __init__(self, name):
        self.name = name
        self.birth_year = random.randrange(100, 10000)
        self.obsessions = []
        self.faction_list = ["humans", "apes", "dwarves", "dogs", "cats", "insects", "arachnids", "demons", "dragons", "trees", "flowers", "cows", "horses", "fish", "mutants", "penguins", "deer", "salamanders", "pixies", "elves", "vampires", "tortoises", "birds", "fungi", "giants", "spirits", "serpents", "crabs", "lemurs", "elephants"]
        self.factions = self.GenerateFactions()
        self.allied_factions = self.GetAlliedFactions()
        self.enemy_factions = self.GetEnemyFactions()
        self.events = []

    # Generates a reputation for every faction
    def GenerateFactions(self):
        factions = {}
        for faction in self.faction_list:
            factions[faction] = 0

        for i in range(3):
            factions[random.choice(self.faction_list)] = random.randrange(50, 101)
            factions[random.choice(self.faction_list)] = random.randrange(-100, -49)

        return factions

    # Gets all factions with positive reputation
    def GetAlliedFactions(self):
        allied_factions = []
        for faction in self.factions.keys():
            if(self.factions[faction] > 0):
                allied_factions.append(faction)

        return allied_factions

    # Gets all factions with negative reputation
    def GetEnemyFactions(self):
        enemy_factions = []
        for faction in self.factions.keys():
            if(self.factions[faction] < 0):
                enemy_factions.append(faction)

        return enemy_factions
