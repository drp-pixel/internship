print("Reverse a string using a for loop")

# Input string
text = "Python"

# Empty string to store reversed result
reversed_text = ""

# Loop through each character in reverse order
for i in range(len(text) - 1, -1, -1):  # start from last index to 0
    reversed_text += text[i]            # add each character to result

print("Original:", text)
print("Reversed:", reversed_text)

# Example with your name
name = "Dhaval"
reversed_name = ""
for i in range(len(name) - 1, -1, -1):
    reversed_name += name[i]

print("Original Name:", name)
print("Reversed Name:", reversed_name)

print ("Reverse a string using a while loop")

# Input string
text = "Python"

# Empty string to store reversed result
reversed_text = ""

# Start from the last index
i = len(text) - 1

# Loop until index becomes -1
while i >= 0:
    reversed_text += text[i]   # add character at current index
    i -= 1                     # move to previous index

print("Original:", text)
print("Reversed:", reversed_text)

# Example with your name
name = "Dhaval"
reversed_name = ""
i = len(name) - 1
while i >= 0:
    reversed_name += name[i]
    i -= 1

print("Original Name:", name)
print("Reversed Name:", reversed_name)