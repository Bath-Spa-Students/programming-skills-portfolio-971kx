# Making a dictionary containing there country & its names
rivers = {
    'Amazon' : 'South America',
    'Indus' : 'Pakistan',
    'River Thames' : 'England'
}

# Utilizing loop to display sentence of each river
for river, country in rivers.items():
    print(f'the {river} is running through {country}.  ') 


# Utilizing loop to display river name in the dictionary
print("\nRivers:")
for river in rivers.keys():
    print(river)

# Utilizing loop to display name of country in the dictionary
print("\nCountries:")
for country in rivers.values():
    print(country)
