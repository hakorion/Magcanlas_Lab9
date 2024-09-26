salary = float(input("Enter your monthly salary: "))
loan_amount_requested = float(input("Enter the loan amount requested: "))

if salary >= 30000 and loan_amount_requested <= (10 * salary):
    print("You are eligible for the loan.")

    months = int(input("Enter the number of months to pay: "))
    
    interest = loan_amount_requested * 0.10

    new_loan_amount = loan_amount_requested + interest
    
    monthly_payment = new_loan_amount / months
    
    print(f"Loan Amount: {loan_amount_requested:}")
    print(f"Interest: {interest:}")
    print(f"New Loan Amount (with interest): {new_loan_amount:}")
    print(f"Monthly Payment: {monthly_payment:}")  
else:

    if salary < 30000:
        print("You are not approved for the loan: Your salary is too low.")
    elif loan_amount_requested > (10 * salary):
        print("You are not approved for the loan: The requested amount is too high.")