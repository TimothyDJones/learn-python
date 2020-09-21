# problem2_3.py
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

balance = 999999
annualInterestRate = 0.18

# Strategy: Divide total balance by 12 to find lower bound for monthly payment.
# Find upper bound as the total balance with interest compounded for entire year
# divided by 12. Then use bisection method to narrow solution until we find
# least payment with zero or negative final balance.

lower = balance / 12
upper = (balance * (1 + annualInterestRate)**12) / 12
initial_balance = balance
min_payment = 0

while abs(balance) > 0.01:
    balance = initial_balance
    min_payment = lower + (upper - lower) / 2
    for m in range(0, 12):
        balance = balance_remaining(balance, annualInterestRate, min_payment)
    print("With minimum payment of " + str(min_payment) + ", remaining balance: " + str(round(balance, 2)), balance)
    if balance < 0.0:
        upper = min_payment
    else:
        lower = min_payment

print("Lowest Payment: " + str(round(min_payment, 2)))
