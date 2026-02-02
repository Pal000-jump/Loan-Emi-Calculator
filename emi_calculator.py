def calculate_emi(principal, annual_interest_rate, tenure_years):
    """
    Calculate the Equated Monthly Installment (EMI) for a loan.

    :param principal: Loan amount (principal)
    :param annual_interest_rate: Annual interest rate in percentage
    :param tenure_years: Loan tenure in years
    :return: Monthly EMI amount
    """
    monthly_interest_rate = annual_interest_rate / 100 / 12
    num_payments = tenure_years * 12

    if monthly_interest_rate == 0:
        return principal / num_payments

    emi = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments / ((1 + monthly_interest_rate) ** num_payments - 1)
    return emi

# Example usage
if __name__ == "__main__":
    principal = float(input("Enter loan amount: "))
    annual_interest_rate = float(input("Enter annual interest rate (%): "))
    tenure_years = int(input("Enter loan tenure in years: "))

    emi = calculate_emi(principal, annual_interest_rate, tenure_years)
    print(f"Your monthly EMI is: {emi:.2f}")