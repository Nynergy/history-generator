'''
    History Generator by Ben Buchanan (2018)
'''

import random
from classes.Figure import Figure
from classes.Event import Event

'''
    Global lists to pull from
'''

generic_nouns = ["apple", "trumpet", "book", "rose", "heron", "volume", "glitter", "space", "rock", "face", "pole", "solitude", "menagerie", "zoetrope", "wizard", "joke", "fern", "cloud", "moon", "sun", "weed", "lock", "bottle", "crown", "key", "moth", "window", "snow", "candle", "throne", "sceptre", "trial", "pathogen", "friend", "will", "leek", "rice"]
adjective_list = ["dirty", "dusty", "shady", "rainy", "red", "blue", "green", "clean", "smelly", "polite", "lovely", "bloody", "dilapidated", "ancient", "modern", "futuristic", "crazy", "quiet", "loud", "holy", "evil", "high", "low", "crusty", "smooth", "rough", "quick", "wild", "golden", "black", "gloomy", "sunny", "broken", "sunken", "raised", "gilded", "embossed", "yellow", "orange", "purple", "tired", "sick", "pleasant", "taut", "viscous"]

material_list = ["stone", "limestone", "onyx", "amber", "diamond", "wood", "emerald", "ruby", "sapphire", "opal", "obsidian", "glass", "fabric of time", "topaz", "peridot", "steel", "iron", "chalk", "talc", "graphite", "plastic", "mica", "shale", "basalt", "pumice", "ice", "sandstone", "ash", "mud", "lead", "copper", "titanium", "uranium", "fabric of space", "solid light", "dust", "coal", "stained glass", "iridescent plates", "bone"]

weapons_list = ["sword", "knife", "cudgel", "mace", "arrow", "longbow", "greatsword", "handaxe", "flail", "lance", "pike", "scimitar", "pistol", "rifle", "shotgun", "slingshot", "cannon", "trebuchet", "catapult", "artillery", "bomb", "flamethrower", "wand", "crossbow", "guillotine"]
tools_list = ["hammer", "axe", "drill", "chisel", "saw", "razor", "plow", "brand", "crook", "wrench", "screwdriver", "telescope", "grinder", "wheel", "whisk", "ladle", "comb", "brush", "clamp", "tape", "balance", "riveter", "hatchet"]

location_list = ["Alley", "Archfield", "Barrows", "Boulder", "Cave", "Crossing", "Crater", "Delta", "Depth", "Desert", "Dunes", "Elevation", "Field", "Fjord", "Farm", "Grotto", "Hill", "Hamlet", "Hovel", "Isle", "Island", "Junction", "Jump", "Knoll", "Lake", "Lookout", "Mine", "Neo-Dome", "Open", "Outpost", "Plateau", "Peak", "Quarter", "Quadrant", "Rise", "Rift", "Rim", "Steeple", "Scorch", "Scavenge", "Trench", "Tunnel", "Undergrowth", "Volcano", "White Cap", "Watchtower", "Yard"]

# Resolves subtypes for birth
def ResolveBirthSubtype(event, figure):
    description = ""

    if(event.event_subtype == "miraculous conception"):
        description = "A child is born with {} {}, called {}, and the {} are amazed by them.".format(random.choice(material_list), random.choice(["upon their eyes", "in their mouth", "around their throat", "on their swaddling clothes"]), figure.name, random.choice(figure.allied_factions))
    elif(event.event_subtype == "born into riches"):
        description = "A child named {} is born into the riches of a noble family of {}.".format(figure.name, random.choice(figure.allied_factions))
    elif(event.event_subtype == "born into poverty"):
        description = "A child named {} is born in the {} slums of {}.".format(figure.name, random.choice(adjective_list), GenerateLocationName())
    elif(event.event_subtype == "born in the wilderness"):
        description = "A child is born to a clan of {} in the remote wilderness, and they are named {}.".format(random.choice(figure.allied_factions), figure.name)
    elif(event.event_subtype == "born and then orphaned"):
        description = "A child is born and abandoned, and taken in by a group of {}. They name the child {}.".format(random.choice(figure.allied_factions), figure.name)
    elif(event.event_subtype == "normal"):
        description = "A child named {} is born into a clan of {}.".format(figure.name, random.choice(figure.allied_factions))

    return description

# Resolves subtypes for discovering a relic
def ResolveRelicSubtype(event, figure):
    description = ""

    if(event.event_subtype == "good relic"):
        description = "{} found a relic of the {} civilization, which created a bright radiance around itself. {} called it the {} of {}s.".format(figure.name, GenerateName(), figure.name, random.choice(random.choice([tools_list, weapons_list])).title(), random.choice(generic_nouns).title())
    elif(event.event_subtype == "bad relic"):
        description = "{} found a relic of the {} civilization, surrounded by an evil presence. Frightened, {} cast it away, declaring it {}, {} of {}s.".format(figure.name, GenerateName(), figure.name, GenerateName(), random.choice(random.choice([tools_list, weapons_list])).title(), random.choice(generic_nouns).title())
    elif(event.event_subtype == "normal"):
        civ_name = GenerateName()
        material_one = random.choice(material_list)
        material_two = random.choice(material_list)
        while(material_one == material_two):
            material_two = random.choice(material_list)
        description = "{} found a relic of {}, carved in {} and {}, and named it the {} of {}.".format(figure.name, civ_name, material_one, material_two, random.choice(generic_nouns).title(), civ_name)

    return description

# Resolves subtypes for seigeing a city
def ResolveSeigeSubtype(event, figure):
    description = ""

    if(event.event_subtype == "to expand territory"):
        enemy_fac = random.choice(figure.enemy_factions)
        description = "In order to expand the territory of their domain, {} led a seige upon the city of {}, which was under control of the {}. {} fought with such ferocity that they were given the title {}, {} of {}.".format(figure.name, GenerateLocationName(), enemy_fac, figure.name, figure.name, random.choice(["Killer", "Flayer", "Subjugator", "Scourge", "Enemy", "Murderer", "Demon", "Crusher", "Executioner"]), enemy_fac.title())
    elif(event.event_subtype == "to liberate a faction"):
        friendly_fac = random.choice(figure.allied_factions)
        description = "In order to liberate the {} from the city at {}, {} led a seige against it, earning them the title of {}, {} of {}.".format(friendly_fac, GenerateLocationName(), figure.name, figure.name, random.choice(["Friend", "Savior", "Angel", "Helper", "Blessing", "Boon", "Honor", "Embodiment", "Vision"]), friendly_fac.title())
    elif(event.event_subtype == "to retrieve an artifact"):
        noun_one = random.choice(generic_nouns)
        noun_two = random.choice(generic_nouns)
        while(noun_one == noun_two):
            noun_two = random.choice(generic_nouns)
        description = "{} led a seige against the city at {} in order to retrieve the fabled artifact {} of {}s and {}s.".format(figure.name, GenerateLocationName(), GenerateName(), noun_one.title(), noun_two.title())
    elif(event.event_subtype == "normal"):
        description = "Seemingly on a whim, {} decided to raze the city at {}, decimating the population of {} that lived there.".format(figure.name, GenerateLocationName(), random.choice(figure.enemy_factions))

    return description

# Resolves subtypes for finding ancient secrets
def ResolveAncientSecretSubtype(event, figure):
    description = ""

    if(event.event_subtype == "awakens a god"):
        description = "When delving some ancient cave systems for an expedition around {}, {} stumbled upon some strange runes. When spoken aloud, a terrifying vision filled their head of an ancient {} older than time itself, slowly waking from an infinite slumber. The only words that came to mind were frenzied screams of their name, {}'{}.".format(GenerateLocationName(), figure.name, random.choice(["god", "goddess", "deity", "demigod", "horror", "sentient force", "omniscience"]), GenerateName(), GenerateName().lower())
    elif(event.event_subtype == "releases a curse"):
        description = "After discovering an ancient tome of knowledge in a forgotten cave system around {}, {} found that a curse had been released upon the kingdom! In order to reverse the damage, the tome, The Index of {}s, was thrown into the fires of {}.".format(GenerateLocationName(), figure.name, random.choice(generic_nouns).title(), GenerateLocationName())
    elif(event.event_subtype == "reveals a civilization"):
        description = "Deep in the belly of the earth, {} discovered the remains of an ancient civilization called {}. Among the treasures kept hidden there was the fabled weapon, The {} {} of {}. {} brought it back as a prize of their discovery.".format(figure.name, GenerateName(), random.choice(adjective_list).title(), random.choice(weapons_list).title(), GenerateName(), figure.name)
    elif(event.event_subtype == "gains magical powers"):
        description = "With the incantation of ancient runes on the wall of a cave, {} summons a forgotten magical energy into their body, infusing them with the power to {}!".format(figure.name, random.choice(["spit acid", "shoot fire from their hands", "freeze anything by looking at it", "commune with animals", "read a person's mind", "see through walls", "fly", "glow in the dark", "persuade anybody", "disintegrate anything with a single thought", "shoot lightning from their fingertips", "move at the speed of light", "manipulate objects with telekinesis"]))
    elif(event.event_subtype == "normal"):
        description = "{} was able to locate the lost treasures of {} in the Mines of {}, earning them limitless riches!".format(figure.name, GenerateName(), GenerateLocationName())

    return description

# Resolves subtypes for assassinating a rival
def ResolveAssassinationSubtype(event, figure):
    description = ""

    if(event.event_subtype == "normal"):
        description = "In a fit of revenge against the murder of their {}, {} ordered the assassination of their rival {} of the clan of {}.".format(random.choice(["mother", "father", "brother", "sister", "uncle", "aunt", "grandfather", "grandmother", "son", "daughter", "niece", "nephew", "cousin"]), figure.name, GenerateName(), random.choice(figure.enemy_factions))

    return description

# Resolves subtypes for building a monument
def ResolveMonumentSubtype(event, figure):
    description = ""

    # Handlers

    return description

# Resolves subtypes for founding a religion
def ResolveReligionSubtype(event, figure):
    description = ""

    # Handlers

    return description

# Resolves subtypes for betraying a partner
def ResolveBetrayalSubtype(event, figure):
    description = ""

    # Handlers

    return description

# Resolves subtypes for marriage
def ResolveMarriageSubtype(event, figure):
    description = ""

    # Handlers

    return description

# Resolves subtypes for battling for a faction
def ResolveFactionBattleSubtype(event, figure):
    description = ""

    # Handlers

    return description

# Resolves subtypes for having a vision
def ResolveVisionSubtype(event, figure):
    description = ""

    # Handlers

    return description

# Resolves subtypes for commissioning massive weapons
def ResolveMassiveWeaponSubtype(event, figure):
    description = ""

    # Handlers

    return description

# Resolves subtypes for losing an artifact
def ResolveArtifactLossSubtype(event, figure):
    description = ""

    # Handlers

    return description

# Resolves subtypes for calling crusades
def ResolveCrusadeSubtype(event, figure):
    description = ""

    # Handlers

    return description

# Resolves subtypes for decreeing important laws
def ResolveDecreeSubtype(event, figure):
    description = ""

    # Handlers

    return description

# Resolves subtypes for having a child
def ResolveChildSubtype(event, figure):
    description = ""

    # Handlers

    return description

# Resolves subtypes for victimizing a faction
def ResolveVictimizationSubtype(event, figure):
    description = ""

    # Handlers

    return description

# Resolves subtypes for winning a major war
def ResolveWarSubtype(event, figure):
    description = ""

    # Handlers

    return description

# Resolves subtypes for inventing something important
def ResolveInventionSubtype(event, figure):
    description = ""

    # Handlers

    return description

# Resolves subtypes for gathering favor with a faction
def ResolveFavorSubtype(event, figure):
    description = ""

    # Handlers

    return description

# Resolves subtypes for building a temple
def ResolveTempleSubtype(event, figure):
    description = ""

    # Handlers

    return description

# Resolves subtypes for creating a piece of art
def ResolveArtSubtype(event, figure):
    description = ""

    # Handlers

    return description

# Resolves subtypes for holding a major festival
def ResolveFestivalSubtype(event, figure):
    description = ""

    # Handlers

    return description

# Resolves subtypes for falling under a curse
def ResolveCurseSubtype(event, figure):
    description = ""

    # Handlers

    return description

# Resolves subtypes for becoming obsessed with something
def ResolveObsessionSubtype(event, figure):
    description = ""

    # Handlers

    return description

# Resolves subtypes for death
def ResolveDeathSubtype(event, figure):
    description = ""

    if(event.event_subtype == "disease"):
        description = "{} dies suddenly of a strange and rare disease called {} of the {} {}.".format(figure.name, GenerateName(), random.choice(adjective_list).title(), random.choice(generic_nouns).title())
    elif(event.event_subtype == "assassinated by rival"):
        description = "{} is assassinated by their rival, {} of a clan of {}.".format(figure.name, GenerateName(), random.choice(figure.enemy_factions))
    elif(event.event_subtype == "assassinated by child"):
        description = "{} was {} by their child, {}, in an attempt to claim the throne through early succession.".format(figure.name, random.choice(["poisoned", "stabbed", "beheaded", "disemboweled", "burned alive", "buried alive", "shot", "hanged"]), GenerateName())
    elif(event.event_subtype == "died in battle"):
        description = "{} was slain by a group of {} during the battle of {} at {}.".format(figure.name, random.choice(figure.enemy_factions), GenerateName(), GenerateLocationName())
    elif(event.event_subtype == "heart attack"):
        description = "{} was overcome by a sharp pain, and succumbed to a heart attack.".format(figure.name)
    elif(event.event_subtype == "driven to suicide"):
        description = "Without warning on one quiet morning, {} decided to end their own life by {}.".format(figure.name, random.choice(["jumping from the tallest parapet in the castle", "hanging", "swallowing poison", "stabbing", "self-beheading", "bleeding out"]))
    elif(event.event_subtype == "normal"):
        description = "{} died in their sleep one quiet night, with a smile on their face.".format(figure.name)

    return description

# Resolves an event and adds it to the figure's event list
def ResolveEvent(event, figure):
    '''
        TODO: Resolve all of these types and their respective subtypes
    '''

    event_type_handler = {
                            "birth":ResolveBirthSubtype(event, figure),
                            "discovers a relic":ResolveRelicSubtype(event, figure),
                            "seiges a city":ResolveSeigeSubtype(event, figure),
                            "unearths an ancient secret":ResolveAncientSecretSubtype(event, figure),
                            "assassinates a rival":ResolveAssassinationSubtype(event, figure),
                            #"builds a monument":ResolveMonumentSubtype(event, figure),
                            #"founds a religion":ResolveReligionSubtype(event, figure),
                            #"betrays a partner":ResolveBetrayalSubtype(event, figure),
                            #"marries":ResolveMarriageSubtype(event, figure),
                            #"battles for faction":ResolveFactionBattleSubtype(event, figure),
                            #"has a vision":ResolveVisionSubtype(event, figure),
                            #"commissions a massive weapon":ResolveMassiveWeaponSubtype(event, figure),
                            #"loses a magical artifact":ResolveArtifactLossSubtype(event, figure),
                            #"calls for a crusade":ResolveCrusadeSubtype(event, figure),
                            #"decrees an important law":ResolveDecreeSubtype(event, figure),
                            #"has a child":ResolveChildSubtype(event, figure),
                            #"victimizes a faction":ResolveVictimizationSubtype(event, figure),
                            #"wins major war":ResolveWarSubtype(event, figure),
                            #"invents something important":ResolveInventionSubtype(event, figure),
                            #"gathers favor with a faction":ResolveFavorSubtype(event, figure),
                            #"builds a temple":ResolveTempleSubtype(event, figure),
                            #"creates a piece of art":ResolveArtSubtype(event, figure),
                            #"holds a major festival":ResolveFestivalSubtype(event, figure),
                            #"falls under a curse":ResolveCurseSubtype(event, figure),
                            #"becomes obsessed with something":ResolveObsessionSubtype(event, figure),
                            "death":ResolveDeathSubtype(event, figure)
                         }

    event.description = event_type_handler.get(event.event_type, "There is no record of this event...")

    figure.events.append(event)

# Generates a series of events to be resolved
def GenerateLifetime(figure):
    event_types = ["discovers a relic", "seiges a city", "unearths an ancient secret", "assassinates a rival", "builds a monument", "founds a religion", "betrays a partner", "marries", "battles for faction", "has a vision", "commissions a massive weapon", "loses a magical artifact", "calls for a crusade", "decrees an important law", "has a child", "victimizes a faction", "wins major war", "invents something important", "gathers favor with a faction", "builds a temple", "creates a piece of art", "holds a major festival", "falls under a curse", "becomes obsessed with something"]

    # First event is always a birth event
    event = Event("birth")
    ResolveEvent(event, figure)

    # Generate a set of middle events
    num_events = random.randrange(10)
    for i in range(num_events):
        event = Event(random.choice(event_types))
        ResolveEvent(event, figure)

    # Last event is always a death event
    event = Event("death")
    ResolveEvent(event, figure)

# Generates a name
def GenerateName():
    # Bits and bobs to smash together into silly sounding names
    bits = ['ada', 'aro', 'awi', 'ace', 'axe', 'azi', 'ah', 'aet', 'an', 'bo', 'buf', 'bir', 'bea', 'bar', 'bhu', 'bli', 'cro', 'cu', 'chi', 'cha', 'cer', 'cre', 'clo', 'di', 'dha', 'dok', 'dhu', 'do', 'dra', 'dge', 'ei', 'edo', 'eta', 'eu', 'elu', 'eni', 'for', 'fea', 'fin', 'far', 'fhi', 'fu', 'gra', 'gub', 'go', 'ghi', 'ger', 'ge', 'hai', 'he', 'huz', 'hof', 'hu', 'hau', 'ie', 'ian', 'im', 'il', 'iak', 'iel', 'jul', 'jid', 'jag', 'jhe', 'jar', 'jin', 'kor', 'kri', 'kha', 'ku', 'ker', 'kei', 'lou', 'lea', 'lim', 'lev', 'lan', 'la', 'min', 'mag', 'muck', 'mei', 'mar', 'mir', 'moe', 'nil', 'nex', 'nar', 'nu', 'nyn', 'nye', 'or', 'oan', 'ous', 'oye', 'oi', 'pre', 'par', 'pel', 'poa', 'piv', 'py', 'pay', 'pey', 'qu', 'qua', 'qi', 'qo', 'quy', 're', 'ra', 'ri', 'ro', 'ru', 'rei', 'rum', 'rin', 'rav', 'rey', 'rye', 'sol', 'so', 'sar', 'sin', 'son', 'sep', 'sei', 'sen', 'szu', 'say', 'sy', 'to', 'tu', 'tad', 'tea', 'ten', 'tru', 'tri', 'try', 'tye', 'ua', 'uo', 'ui', 'ue', 'uyo', 'var', 'va', 'vop', 'vuh', 'vex', 'vir', 'vye', 'wa', 'we', 'woa', 'win', 'wha', 'whe', 'who', 'whi', 'whu', 'wu', 'wy', 'xe', 'xa', 'xi', 'xu', 'xo', 'xhi', 'xy', 'ya', 'yu', 'yo', 'yi', 'ye', 'yan', 'za', 'zu', 'zi', 'zo', 'ze', 'zeh', 'zhe', 'zha', 'zhi', 'zho', 'zy', 'zhy', 'zhiv']

    name = ""

    num_parts = random.randrange(2, 4)
    for i in range(num_parts):
        name += random.choice(bits)

    name = name.title()
    
    return name

# Generates a location name
def GenerateLocationName():
    # Locations will be of three varieties:
    # 1. Single word (GenerateName())
    # 2. Two words (Freemans Quarter, Deep Trench, Grand Valley, etc...)
    # 3. Two words with ownership (GenerateName()'s Plateau, GenerateName()'s Cave, etc...)

    name = ""

    loc_type = random.randrange(1, 4)
    if(loc_type == 1):
        name = GenerateName()
    elif(loc_type == 2):
        name = "{} {}".format(random.choice(adjective_list).title(), random.choice(location_list))
    elif(loc_type == 3):
        name = "{}'s {}".format(GenerateName(), random.choice(location_list))

    return name

def main():
    figure = Figure(GenerateName())
    print("NAME: {}".format(figure.name))
    #print("Here are their faction relations:")
    #for faction in figure.factions.keys():
    #    print("{} : {}".format(faction, str(figure.factions[faction])))

    GenerateLifetime(figure)
    print("EVENTS:")
    for i in range(len(figure.events)):
        print("\tEvent {}: {} ({})\n\n{}\n".format(i+1, figure.events[i].event_type.title(), figure.events[i].event_subtype.title(), figure.events[i].description))

    return

main()
