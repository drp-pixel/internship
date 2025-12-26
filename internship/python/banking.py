#user banking loan via using credit score

print("welcome to banking loan and credit score system")

salary = int(input("Enter your monthly salary: "))

credit_score = int(input("Enter your credit score (300-900): "))

if salary > 30000:   # Salary must be above 30,000
    if credit_score >= 750 and credit_score <= 900:  # user have Excellent credit score
        print(" Loan Approved with interest rate 7.25% (Excellent credit score).")

    elif credit_score >= 600 and credit_score < 750:  #  user have Good credit score
        print(" Loan Approved with interest rate 8.25% (Good credit score).")

    elif credit_score >= 500 and credit_score < 600:  #  user have Ok credit score
        print(" Loan Approved with interest rate 10.25% (Ok credit score).")

    else:  # credit_score < 500 user have bad credit score
        print(" Loan Not Approved (below minimum credit score).")

else:
    print(" Loan Not Approved (salary must be below 30,000).")