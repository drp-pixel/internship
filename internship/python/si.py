#find a simple interest value given by user

P = float(input("Enter the Principal amount: ")) #for grtting main velue of principal amount

R = float(input("Enter the Rate of interest (+% per annum): ")) #for grtting interest

T = float(input("Enter the Time (in years): "))

simple_interest = (P * R * T) / 100

print ("simple_interest_is:",simple_interest)