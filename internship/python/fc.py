#here is the program to calculate factorial.#
#take num from the user
num = int(input("please enter the number :"))

fac = 1

#use loop to put formula of factorial
for i  in range(1, num + 1):
     
     fac *= i
(print("you num's factorial is :",fac))

#here is the same program writen by useing while loop 

#take input from the user 
# Take a number from the user to calculate its factorial
num = int(input("Please enter a number: "))

# Initialize factorial variable with 1
# (Factorial of 0 or 1 is 1)
fac = 1

# Initialize counter variable
i = 1

# Loop runs from 1 up to the given number
while i <= num:
    # Multiply the current value of factorial by i
    fac = fac * i
    
    # Increase the counter by 1 to end the loop
    i += 1

# Print ans
print("Your number's factorial is:", fac)