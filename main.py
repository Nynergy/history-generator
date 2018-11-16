'''
    History Generator by Ben Buchanan (2018)
'''

import random

# Generates a name
def GenerateName():
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    vowels = ['a', 'e', 'i', 'o', 'u']

    print("Generating name...")
    name = random.choice(consonants) + random.choice(vowels) + random.choice(consonants) + random.choice(consonants) + random.choice(vowels) + random.choice(consonants)

    return name

def main():
    name = GenerateName()
    print("Name: " + name)

    return

main()
