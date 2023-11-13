import math

# ask the user for the calculation type that they'd like to do
print("Menu:")
print("investment - to calculate the amount of interest you'll earn on your investment.")
print("bond - to calculate the amount you'll have to pay on a home loan")

calculation_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# the following code asks for user inputs upon choosing the 'investment' option
if calculation_type.lower() == "investment":
    investment_amount = float(input("What is the amount you are depositing? "))
    interest_rate = float(input("What is the interest rate? ")) / 100
    investment_years = int(input("How many years do you plan on investing? "))
    interest_type = input("Do you want simple or compound interest? ")

    # calculates the user's total upon choosing simple interest
    if interest_type.lower() == "simple":
        total_interest = investment_amount * (1 + interest_rate * investment_years)
        print("Your total amount after", investment_years, "years of simple interest:", round(total_interest, 2))
    
    # calculates the user's total upon choosing compound interest
    elif interest_type.lower() == "compound":
        total_interest = investment_amount * math.pow((1 + interest_rate), investment_years)
        print("Your total amount after", investment_years, "years of compound interest:", round(total_interest, 2))

# the following code asks for user input upon choosing the 'bond' option
elif calculation_type.lower() == "bond":
    house_val = float(input("What is the value of the house?:"))
    bond_int_rate = float(input("What is the interest rate?:")) / 100
    bond_period = int(input("How many months will it take to repay the bond?:"))

    # calculates the total amount user will pay monthly for the period of their bond
    monthly_int_rate = bond_int_rate / 12
    monthly_payment = (monthly_int_rate * house_val) / (1 - (1 + bond_int_rate) ** (-bond_period))
    total_bond = monthly_payment * bond_period
    print("Your total monthly bond payment is", round(monthly_payment, 2))
    print("Your total bond repayment amount is", round(total_bond, 2))

# displays an error message when the user enters anything other than "investment" or "bond"
else:
    print("Invalid, please enter either 'investment' or 'bond'.")






