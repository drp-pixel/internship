#getting three number from user and finding out which number have max out of three of these
print("finding max number out of three number")

# Taking three numbers as input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Compare the numbers
if (num1 >= num2) and (num1 >= num3):
    print("The maximum number is:", num1)
elif (num2 >= num1) and (num2 >= num3):
    print("The maximum number is:", num2)
else:
    print("The maximum number is:", num3)