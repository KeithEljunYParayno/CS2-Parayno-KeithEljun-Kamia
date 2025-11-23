places = []

print("Please enter your 5 travel destinations:")
for i in range(5):
    places.append(input(f"Destination {i+1}: "))

print("Original Travel Itinerary:")
for i in range(5):
    print(f"{i+1}. {places[i]}")

print("Let's update your 2nd and 5th destinations.")
places[1] = input("Enter a new destination for position 2: ")
places[4] = input("Enter a new destination for position 5: ")

print("Updated Travel Itinerary:")
for i in range(5):
    print(f"{i+1}. {places[i]}")
