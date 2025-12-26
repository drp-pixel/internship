# Ask user for number of rows
rows = int(input("Enter number of rows: "))

# -------------------------------
# Normal star pattern using for loop
print("\nNormal Pattern (for loop):")
for i in range(1, rows + 1):
    print("*" * i)

# Reverse star pattern using for loop
print("\nReverse Pattern (for loop):")
for i in range(rows, 0, -1):   # start from rows down to 1
    print("*" * i)

# -------------------------------
# Normal star pattern using while loop
print("\nNormal Pattern (while loop):")
i = 1
while i <= rows:
    print("*" * i)
    i += 1

# Reverse star pattern using while loop
print("\nReverse Pattern (while loop):")
i = rows
while i >= 1:
    print("*" * i)
    i -= 1