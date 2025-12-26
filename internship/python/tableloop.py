# Program to print multiplication table of a given number using a for loop
print("multification in for loop")
# Take input from the user
num = int(input("Enter number to find the table: "))

# Loop from 1 to 10
for i in range(1, 11):
    # Multiply the number with the loop counter
    table = num * i
    
    # Print the result in table format
    print(num, 'x', i, '=', table)

# Program to print multiplication table of a given number using a while loop
print("multification in while loop")
# Take input from the user
num = int(input("Enter number to find the table: "))

# Initialize counter variable
i = 1

# Continue looping while i <= 10
while i <= 10:
    # Multiply the number with the counter
    table = num * i
    
    # Print the result in table format
    print(num, 'x', i, '=', table)
    
    # Increment the counter by 1
    i += 1