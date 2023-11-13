print("Welcome to the Pizza Topping Selection!")
print("Enter your favorite pizza toppings. Type 'quit' to finish.")

pizza_toppings = []

while True:
    topping = input("Enter a topping: ")

    if topping.lower() == 'quit':
        break
    else:
        pizza_toppings.append(topping)
        print(f"Great choice! {topping.capitalize()} will be added to your pizza.")

if pizza_toppings:
    print("\nYour pizza will have the following toppings:")
    for topping in pizza_toppings:
        print(f"- {topping.capitalize()}")
else:
    print("\nNo toppings selected. Enjoy your plain pizza!")

print("Thank you for using the Pizza Topping Selection!")
