# --- 1. Basic Types ---
name = "Abhishek"
score = 95
height = 5.9
is_learning = True

# --- 2. List Mastery ---
fruits = ["Apple", "Banana", "Cherry"]

# Adding
fruits.append("Date")          # ["Apple", "Banana", "Cherry", "Date"]
fruits.insert(1, "Elderberry") # ["Apple", "Elderberry", "Banana", "Cherry", "Date"]

# Removing
removed_item = fruits.pop()    # Removes "Date"
fruits.remove("Banana")        # ["Apple", "Elderberry", "Cherry"]

# Finding & Counting
print(f"Index of Cherry: {fruits.index('Cherry')}")
print(f"Total Fruits: {len(fruits)}")

# Slicing (The Magic of Lists)
# [start:stop:step]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"First three: {numbers[:3]}")
print(f"Every second number: {numbers[::2]}")
print(f"Reversed list: {numbers[::-1]}")
