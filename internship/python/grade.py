# giving the grade and if if student is pass or fail via keboard

marks = float(input("Enter the student's marks (0-100): "))

    # Validate marks
if marks < 0 or marks > 100:
    print("Invalid input! Marks should be between 0 and 100.")
else:
    if marks >= 80:
        print("Grade: Distinction")
    elif marks >= 70:
        print("Grade: First Class")
    elif marks >= 60:
        print("Grade: Second Class")
    elif marks >= 40:
        print("Grade: third Class")
    else:
        print("Grade: Fail")