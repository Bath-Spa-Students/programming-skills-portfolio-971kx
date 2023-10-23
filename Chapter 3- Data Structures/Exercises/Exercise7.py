# List of places to visit
places_to_visit = ["Maldives", "Canada", "Kashmir", "Hunza", "Goa", "Singapore"]

# Print the original list
print("Original list:")
print(places_to_visit)

# Print the list in alphabetical order using sorted()
print("\nSorted list:")
print(sorted(places_to_visit))

# Print the original list again to show it's still in its original order
print("\nOriginal list after sorted():")
print(places_to_visit)

# Print the list in reverse alphabetical order using sorted() with reverse=True
print("\nReverse sorted list:")
print(sorted(places_to_visit, reverse=True))

# Print the original list again to show it's still in its original order
print("\nOriginal list after reverse sorted():")
print(places_to_visit)

# Reverse the order of the list using reverse()
places_to_visit.reverse()
print("\nReversed list:")
print(places_to_visit)

# Reverse the order of the list again to get back to the original order
places_to_visit.reverse()
print("\nList back to original order after reverse():")
print(places_to_visit)

# Sort the list in alphabetical order using sort()
places_to_visit.sort()
print("\nList sorted in alphabetical order:")
print(places_to_visit)

# Sort the list in reverse alphabetical order using sort() with reverse=True
places_to_visit.sort(reverse=True)
print("\nList sorted in reverse alphabetical order:")
print(places_to_visit)