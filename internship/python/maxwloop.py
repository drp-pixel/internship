# Program to find the largest number in a list using a loop wout max f

# Sample list of numbers
numbers = [12, 45, 7, 89, 34, 67]

# Assume the first element is the largest initially
largest = numbers[0]

# Loop through the list starting from the second element
for num in numbers[1:]:
    # Compare each element with the current largest
    if num > largest:
        # Update largest if a bigger number is found
        largest = num

#Print the result
print("The largest number in the list is:", largest)