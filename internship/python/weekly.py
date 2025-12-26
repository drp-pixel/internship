#get input from user between 1 to 7 and show 1 as mon and 7 as sunday
print("welcome to weelky day and number based system")

#using input from the user
day = int(input("enter a number (1 to 7): "))

if day == 1: #using number 1 to check the number
    print("monday") #if using number is 1 , showing monday
elif day == 2: #using number 2 to check the number
    print("tuesday") #if using number is 2, showing tuesday
elif day == 3: #using number 3 to check the number
    print("wednesday") #if using number is 3, showing wednesday
elif day == 4: #using number 4 to check the number
    print("thursday") #if using number is 4, showing thursday
elif day == 5: #using number 5 to check the number
    print("friday") #if using number is 5 , showing friday
elif day == 6: #using number 6 to check the number
    print("saturday") #if using number is 6, showing saturday
elif day == 7: #using number 7 to check the number
    print("sunday") #if using number is 7, showing sunday
else:
    #not eligible cause number is not between 1 to 7
    print("not eligible (number must be between 1 to 7)")