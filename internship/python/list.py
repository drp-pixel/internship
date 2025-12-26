# creating list using function like create, append etc
fruits = ["apple", "banana", "cherry"]
print("my_list:", fruits)

# Access elements
print("First fruit:", fruits[0])    # index 0
print("Last fruit:", fruits[-1])   # last item

# Add fruit at end
fruits.append("orange")
print("After append:", fruits)

# Add fruit at position
fruits.insert(1, "grape")  # at index 1
print("After insert:", fruits)

# Remove fruit by name
fruits.remove("cherry")
print("After remove:", fruits)

# Remove fruit by index (default last)
popped_item = fruits.pop()  # removes last
print("Popped fruit:", popped_item)
print("After pop:", fruits)

# Sorting (numbers only)
numbers = [5, 2, 9, 1, 7]
print("Unsorted numbers:", numbers)

numbers.sort()  # ascending
print("Sorted ascending:", numbers)

# Check if fruit exists 
if "banana" in fruits:
    print("Banana is in the list")
else:
    print("Banana not found")