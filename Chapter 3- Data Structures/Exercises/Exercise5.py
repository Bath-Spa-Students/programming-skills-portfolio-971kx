# List of people to invite to dinner
guests = ["Bruce Lee", "Kobe Bryant", "Sheikh Zayed", "Paul Walker"]

# Print invitations to each person
for guest in guests:
    print(f"Dear {guest},\nYou are cordially invited to dinner at my place. I would be honored to have you as my guest.\n\nSincerely, [Your Name]")

# Name of the guest who can't make it
guest_cant_make_it = "Kobe Bryant"
print(f"\nUnfortunately, {guest_cant_make_it} can't make it to the dinner.\n")

# Replace the guest who can't make it with a new person
guests.remove(guest_cant_make_it)
new_guest = "Isaac Newton"
guests.append(new_guest)

# Print second set of invitation messages
for guest in guests:
    print(f"Dear {guest},\nYou are cordially invited to dinner at my place. I would be honored to have you as my guest.\n\nSincerely, [Your Name]")