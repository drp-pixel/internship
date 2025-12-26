# Convert Fahrenheit to Celsius

print("welcome to tempareture converter")

# Get input from user
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Conversion formula
celsius = (fahrenheit - 32) * 5 / 9

# Display result
print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")