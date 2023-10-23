# Cost of each USB stick in pounds
usb_stick_price = 6

# Total amount of money the girl has in pounds
total_money = 50

# Calculate the number of USB sticks she can buy
num_usb_sticks = total_money // usb_stick_price

# Calculate the remaining money after buying USB sticks
remaining_money = total_money % usb_stick_price

# Print the results
print(f"The girl can buy {num_usb_sticks} USB sticks.")
print(f"She will have £{remaining_money}left.")