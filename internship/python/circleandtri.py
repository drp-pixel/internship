#find the circle along with triangle area by input given by user

print ("welcome to calculate circle and triangle area")

import math

print("Choose an option:")  # giving option to user
print("1. Find area of Circle")  # for circle
print("2. Find area of Triangle")  # for triangle

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    # Circle area
    radius = float(input("Enter the radius of the circle: "))
    circle_area = math.pi * radius ** 2
    print(f"Area of the circle: {circle_area:.2f}") 
    #f-string (lets you insert variables into strings),2f → format the number as a float with 2 decimal places

elif choice == 2:
    # Triangle area
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of triangle: "))
    triangle_area = 0.5 * base * height
    print(f"Area of the triangle: {triangle_area:.2f}")
    #f-string (lets you insert variables into strings),2f → format the number as a float with 2 decimal places

else:
    print("Invalid choice! Please enter 1 or 2.")