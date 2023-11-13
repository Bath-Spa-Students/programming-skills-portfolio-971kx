# List of sandwich orders with 'pastrami' repeated at least three times
sandwich_orders = ["Emirates Club", "Matafi Club", "Francisco Club", "Double Zinger", "Tuna", "Pastrami", "Pastrami", "Pastrami"]

# Empty list for finished sandwiches
finished_sandwiches = []

# Inform customers about running out of pastrami
print("Sorry, we've run out of pastrami!")

# Remove all occurrences of 'pastrami' from sandwich_orders using a while loop
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

# Loop through the list of sandwich orders
for order in sandwich_orders:
    print(f"I made your {order} sandwich.")
    # Move the made sandwich to the list of finished sandwiches
    finished_sandwiches.append(order)

# Print a message listing each sandwich that was made
print("\nList of Finished Sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
