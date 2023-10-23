# List of people to invite to dinner
guests = ["Bruce Lee", "Kobe Bryant", "Sheikh Zayed", "Paul Walker"]

# Print a message indicating only two people can be invited
print("Due to the limited space, I can invite only two people for dinner.")

# Use pop() to remove guests and print a message to them
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

# Print invitation messages to the remaining two guests
for guest in guests:
    print(f"Dear {guest},\nYou are still invited to dinner at my place. I'm looking forward to seeing you.\n")

# Use del to remove the last two names from the list
del guests[:]

# Print the empty list to confirm
print("Guest list:", guests)