# problem2_1.py
# Paying debt off in a year

import math

def balance_remaining(bal, ir, pr):
    """
    bal: float, starting account balance
    ir: float, annual interest rate
    pr: float, minimum monthly payment rate (proportion of balance)
    
    Returns the remaining balance as a float, rounded to 2 decimal points,
        after applying the minimum monthly payment.
    """
    unpaid_bal = (1.0 - pr) * bal
    return (1 + (ir / 12.0)) * unpaid_bal

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
for m in range(0, 12):
    balance = balance_remaining(balance, annualInterestRate, monthlyPaymentRate)
    print("Month " + str(m + 1) + " Remaining balance: " + str(round(balance, 2)))

print("Remaining balance: " + str(round(balance, 2)))
