# problem2_2.py
# Paying debt off in a year

import math

def balance_remaining(bal, ir, pmt):
    """
    bal: float, starting account balance
    ir: float, annual interest rate
    pmt: int, minimum fixed monthly payment
    
    Returns the remaining balance as a float, rounded to 2 decimal points,
        after applying the minimum monthly payment.
    """
    unpaid_bal = bal - pmt
    return (1 + (ir / 12.0)) * unpaid_bal

balance = 3926
annualInterestRate = 0.2

# Strategy: Divide total balance by 12 to find lower bound for monthly payment.
# Then increment monthly payment by 10 until we find payment amount that
# results in zero or negative unpaid balance after 12 months.

min_payment = math.floor(balance/(12 * 10)) * 10 - 10
initial_balance = balance

while balance >= 0.0:
    balance = initial_balance
    min_payment += 10
    for m in range(0, 12):
        balance = balance_remaining(balance, annualInterestRate, min_payment)
    print("With minimum payment of " + str(min_payment) + ", remaining balance: " + str(round(balance, 2)))

print("Lowest Payment: " + str(min_payment))
