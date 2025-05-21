# Collect necessary inputs: principal amount, interest rate, years
# Calculate the monthly payments
# Show to the user

def main():
    print("This is a monthly payment loan calculator")
    print("")

    principal = float(input("Enter the loan amount: "))
    interest_rate = float(input("Enter the annual interest rate: "))
    years = int(input("Enter the number of years: "))

    monthly_interest_rate = interest_rate / 1200
    months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-months))

    print("The monthly repayment for this loan is %.2f" % monthly_payment)

if __name__ == "__main__":
    main()