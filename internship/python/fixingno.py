# Given list with duplicates
numbers = [1, 2, 2, 3, 4, 4]

# Create an empty list to store unique values
unique_list = []

# Loop through each element in the original list
for num in numbers:
    # Check if the element is not already in unique_list
    if num not in unique_list:
        # Add the element to unique_list
        unique_list.append(num)

# Print the new list with unique values
print("List with unique values:", unique_list)