def make_sandwich(order):
    print(f"I made your {order} sandwich.")
    return order

# List of sandwich orders
sandwich_orders = ["Emirates Club", "Matafi Club", "Francisco Club", "Double Zinger", "Tuna"]

# Empty list for finished sandwiches
finished_sandwiches = []

# Loop through the list of sandwich orders
for order in sandwich_orders:
    finished_sandwich = make_sandwich(order)
    finished_sandwiches.append(finished_sandwich)

# Print a message listing each sandwich that was made
print("\nList of Finished Sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
