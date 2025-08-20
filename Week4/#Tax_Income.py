#Tax income

income = float(input(f"Enter Taxable income: "))

if income <= 20000:
    tax = income * 0.02
elif income <= 50000:
    tax = (income-20000) * 0.025 + 400500
else:
    tax = (income-50000) * 0.035 + 1150

print(f"Tax Payable: ${tax:.2f}")
