while True:
    age_input = input("Please enter your age (type 'quit' to exit): ").lower()

    if age_input == 'quit':
        print("Exiting the ticket pricing system. Have a great day!")
        break

    try:
        age = int(age_input)
        if age < 3:
            print("Good news! Your ticket is free. Enjoy the movie!")
        elif 3 <= age <= 12:
            print("Your ticket costs $10. Enjoy the movie!")
        else:
            print("Your ticket costs $15. Enjoy the movie!")
    except ValueError:
        print("Invalid input. Please enter a valid age or 'quit'.")
