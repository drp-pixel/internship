# programm to find price item in decimal e.g. gtting .45 type value in different type

print("welcome to getting price in different in rupee and paisa")

price = float(input("Please enter the cost: ")) # Take input as a floating-point number

rupees = int(price) # Extract rupees (integer part)

paise = round((price - rupees) * 100) # Extract paise (fractional part * 100)

# Display results
print("Rupees:", rupees)
print("Paise:", paise)