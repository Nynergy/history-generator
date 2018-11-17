'''
    Event class
'''
import random

class Event:
    '''
        event_type: string denoting overall type of Event
        event_subtype: string denoting specific subtype of Event
        description: string that presents the final outcome of the Event
    '''
    def __init__(self, event_type):
        self.event_type = event_type
        self.event_subtype = self.GenerateSubtype()
        self.description = ""

    # Generates a random subtype given an overall event_type
    def GenerateSubtype(self):
        birth_subtype_list = ["miraculous conception", "born into riches", "born into poverty", "born in the wilderness", "born and then orphaned", "normal"]
        death_subtype_list = ["disease", "assassinated by rival", "assassinated by child", "died in battle", "heart attack", "driven to suicide", "normal"]
        discovers_a_relic_subtype_list = ["good relic", "bad relic", "normal"]
        seiges_a_city_subtype_list = ["to expand territory", "to liberate a faction", "to retrieve an artifact", "normal"]
        unearths_an_ancient_secret_subtype_list = ["awakens a god", "releases a curse", "reveals a civilization", "gains magical powers", "normal"]
        assassinates_a_rival_subtype_list = ["normal"]
        builds_a_monument_subtype_list = ["normal"]
        founds_a_religion_subtype_list = ["normal"]
        betrays_a_partner_subtype_list = ["normal"]
        marries_subtype_list = ["out of love", "out of diplomacy", "normal"]
        battles_for_faction_subtype_list = ["normal"]
        has_a_vision_subtype_list = ["end of the world", "prophecy", "strange dream", "normal"]
        commissions_a_massive_weapon_subtype_list = ["normal"]
        loses_a_magical_artifact_subtype_list = ["in battle", "is stolen", "normal"]
        calls_for_a_crusade_subtype_list = ["normal"]
        decrees_an_important_law_subtype_list = ["normal"]
        has_a_child_subtype_list = ["miscarriage", "orphans it", "normal"]
        victimizes_a_faction_subtype_list = ["normal"]
        wins_major_war_subtype_list = ["normal"]
        invents_something_important_subtype_list = ["normal"]
        gathers_favor_with_a_faction_subtype_list = ["normal"]
        builds_a_temple_subtype_list = ["normal"]
        creates_a_piece_of_art_subtype_list = ["normal"]
        holds_a_major_festival_subtype_list = ["seasonal", "celebration of royalty", "celebration of victory", "normal"]
        falls_under_a_curse_subtype_list = ["normal"]
        becomes_obsessed_with_something_subtype_list = ["normal"]

        switcher = {
                    "birth":random.choice(birth_subtype_list),
                    "death":random.choice(death_subtype_list),
                    "discovers a relic":random.choice(discovers_a_relic_subtype_list),
                    "seiges a city":random.choice(seiges_a_city_subtype_list),
                    "unearths an ancient secret":random.choice(unearths_an_ancient_secret_subtype_list),
                    "assassinates a rival":random.choice(assassinates_a_rival_subtype_list),
                    "builds a monument":random.choice(builds_a_monument_subtype_list),
                    "founds a religion":random.choice(founds_a_religion_subtype_list),
                    "betrays a partner":random.choice(betrays_a_partner_subtype_list),
                    "marries":random.choice(marries_subtype_list),
                    "battles for faction":random.choice(battles_for_faction_subtype_list),
                    "has a vision":random.choice(has_a_vision_subtype_list),
                    "commissions a massive weapon":random.choice(commissions_a_massive_weapon_subtype_list),
                    "loses a magical artifact":random.choice(loses_a_magical_artifact_subtype_list),
                    "calls for a crusade":random.choice(calls_for_a_crusade_subtype_list),
                    "decrees an important law":random.choice(decrees_an_important_law_subtype_list),
                    "has a child":random.choice(has_a_child_subtype_list),
                    "victimizes a faction":random.choice(victimizes_a_faction_subtype_list),
                    "wins major war":random.choice(wins_major_war_subtype_list),
                    "invents something important":random.choice(invents_something_important_subtype_list),
                    "gathers favor with a faction":random.choice(gathers_favor_with_a_faction_subtype_list),
                    "builds a temple":random.choice(builds_a_temple_subtype_list),
                    "creates a piece of art":random.choice(creates_a_piece_of_art_subtype_list),
                    "holds a major festival":random.choice(holds_a_major_festival_subtype_list),
                    "falls under a curse":random.choice(falls_under_a_curse_subtype_list),
                    "becomes obsessed with something":random.choice(becomes_obsessed_with_something_subtype_list)
                   }

        subtype = switcher.get(self.event_type, "none")

        return subtype
