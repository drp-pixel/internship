print ("even numbers between 1 and 20 using a for loop")

# Loop through numbers from 1 to 20
for num in range(1, 21):
    # Check if the number is even / 2
    if num % 2 == 0:
        print(num)

print ("even numbers between 1 and 20 using a while loop")
# Start with the first number
num = 1

# Continue looping until num reaches 20
while num <= 20:
    # Check if the number is even
    if num % 2 == 0:
        print(num)
    # Move to the next number
    num += 1