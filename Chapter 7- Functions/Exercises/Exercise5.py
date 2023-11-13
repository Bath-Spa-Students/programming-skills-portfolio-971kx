def describe_city(city, country="Default Country"):
    message = f"{city} is in {country}."
    print(message)

# Call the function for three different cities
describe_city("Tokyo", "Japan")
describe_city("Berlin", "Germany")
describe_city("Sydney")  # Using the default country
