# programm to check if stundent pass or fail

#maximum marks= 100, passsing marks = 36

marks = float(input("Enter the student's marks (0-100): "))

# validate marks

if marks < 0 or marks > 100:
    print("Invalid input! Marks should be between 0 and 100.")
else:
    passing_marks = 36
    if marks >= passing_marks:
        print("The student has Passed.")
    else:
        print("The student has Failed.")
