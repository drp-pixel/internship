#finding given input by user, age must be 18+ or have voting card

print("welcome to the system to find if you're aligable to vote or not")

age = int(input("Enter your age: "))

voting_card = input("Do you have a voting card? (yes/no): ").lower()

if age >= 18:
    if voting_card == "yes":
        print("You are eligible (age 18+ and has voting card).")
    else:
        print("Not eligible (age 18+ but no voting card).")
else:
    if voting_card == "yes":
        print("Not eligible (has voting card but age below 18).")
    else:
        print("Not eligible (age below 18 and no voting card).")