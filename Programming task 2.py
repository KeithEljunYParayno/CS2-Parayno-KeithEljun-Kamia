def calculate_delivery_fee(distance, rate):
    total = distance * rate
    return total


#    Main Program
# Ask for user input
distance = float(input("Enter distance in kilometers: "))
rate = float(input("Enter rate per kilometer (₱): "))

# Compute total fee
total_fee = calculate_delivery_fee(distance, rate)

# Display the result
print("Total Delivery Fee: ₱", total_fee)
