# Step 1: Input
full_name = input("Enter your full name (First, Middle, Last): ")

# Step 2: Split into parts
first, middle, last = full_name.split(",")

# Step 3: Capitalize properly
first = first.strip().capitalize()
middle = middle.strip().capitalize()
last = last.strip().title()  # title() handles multi-part last names like "dela cruz"

# Step 4: Convert middle name to initial
middle_initial = middle[0] + "."

# Step 5: Rearrange format
formatted_name = f"{last}, {first} {middle_initial}"

# Step 6: Output
print("Formatted Name:", formatted_name)