# mearge_programms

# This program allows the user to choose between multiple services:

print("_______Welcome to Multi Service System_______")
print("1. Movie Ticket Booking")
print("2. Banking Loan System")
print("3. Voter ID Eligibility Check")
print("4. Calculator")
print("5. Days Finder")
print("6. Leapyear Varifier")
print("7. welcome Simple Shopping Cart Program")

# Take user choice as input
service = int(input("Please select a service (1/2/3/4/5/6/7): "))

# Movie Ticket Booking System
if service == 1:
    import tickets

# Banking Loan System
elif service == 2:
    import banking

# Voter ID Eligibility Check
elif service == 3:
    import voting

# Calculator
elif service == 4:
    import calculator

# Days Finder (e.g., find day of the week)
elif service == 5:
    import weekly

# Leap Year Verifier
elif service == 6:
    import leap_year

# Simple Shopping Cart Program
elif service == 7:
    import mall    

# Invalid choice handling
else:
    print("Invalid service selection.")