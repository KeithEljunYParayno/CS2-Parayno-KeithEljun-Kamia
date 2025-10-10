def calculate_delivery_fee(distance, rate):
    """
    Calculates the total delivery fee based on distance and rate per kilometer.

    Parameters:
        distance (float): The distance in kilometers.
        rate (float): The rate per kilometer.

    Returns:
        float: The total delivery fee.
    """
    return distance * rate


# --- Main Program ---
# Ask for user input
distance = float(input("Enter distance in kilometers: "))
rate = float(input("Enter rate per kilometer (₱): "))

# Compute total fee
total_fee = calculate_delivery_fee(distance, rate)

# Display the result
print("Total Delivery Fee: ₱", total_fee)

