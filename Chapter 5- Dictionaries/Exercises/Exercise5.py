# Making dictionaries for each pet & its owner


mano = {
    'animal' : 'Cat',
    'owner' : "Ahmad"
}

jack = {
    'animal' : 'Pigeon',
    'owner' : 'Rafay'
}

donut = {
    'animal' : 'Goat',
    'owner' : 'Khadijah'

}

badal = {
    'animal' : 'Horse',
    'owner' : 'Abood'

}

jin = {
    'animal' : 'Husky dog',
    'owner' : 'Abdullah'
}

mithu = {
    "animal" : 'Parrot',
    'owner' : "Shaima"
}


# Storing all the above dictionaries in 1 list called pets
pets = [mano, jack, donut, badal, jin, mithu ]


# Looping the whole list & displaying info about each pet
for pet in pets:
    print(f"Animal: {pet['animal']}")
    print(f"Owner's Name: {pet['owner']}")
    print("-----------")
