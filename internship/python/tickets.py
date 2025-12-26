# Assigning the values to variables
adults_price = 150   # Price of one adult ticket
kids_price = 75      # Price of one kid ticket

# Greeting message
print("Welcome! How many tickets do you want?")

# Ask the number of tickets
tickets = int(input("Enter your tickets: "))

# Ask how many adults and kids
adults = int(input("Enter number of adults: "))
kids = int(input("Enter number of kids: "))

# Check if tickets match the sum of adults and kids
if tickets != adults + kids:
    print("Number of tickets does not match with adults + kids")
else:
    # Calculate total amount
    total_amount = (adults * adults_price) + (kids * kids_price)

    # Print ticket details neatly
    print("\nTicket Details")
    print("Adults:", adults, "x", adults_price, "=", adults * adults_price)
    print("Kids:", kids, "x", kids_price, "=", kids * kids_price)
    print("Total tickets:", tickets)
    print("Total amount:", total_amount)