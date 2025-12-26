#programm depend on string and it's function as per belowe

# Original text with extra spaces
text = "  python programming is Amazing  "
print("original text:", text)

# Remove spaces from start and end
clean_text = text.strip()
print("clean text:", clean_text)

# Convert to uppercase
upper = text.upper()
print("upper:", upper)

# Convert to lowercase
lower = text.lower()
print(f"lower text {lower}")

# Slice first 6 characters
slicing = clean_text[0:6]
print(f"Slice text:{slicing}")

# Replace word "Amazing" with "Powerfull"
replace = clean_text.replace("Amazing", "Powerfull")
print(f"Replace string:{replace}")

# Find length of string
print("length of string is:", len(clean_text))

# Check if a word exists in string
word = "python"
if word in clean_text:
    print(f"the given {word} is present in string")
else:
    print(f"given word {word} is not found in string")