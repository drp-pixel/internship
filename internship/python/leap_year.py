#finding if given input by user is leap year or nor
# Ask the user to enter a year
year = int(input("Enter a year: "))

# Rule 1: If divisible by 400, it's a leap year
if year % 400 == 0:
    print(year, "is a leap year")

# Rule 2: If divisible by 100 but not 400, it's NOT a leap year
elif year % 100 == 0:
    print(year, "is not a leap year")

# Rule 3: If divisible by 4 but not 100, it's a leap year
elif year % 4 == 0:
    print(year, "is a leap year")

# Rule 4: Otherwise, it's not a leap year
else:
    print(year, "is not a leap year")