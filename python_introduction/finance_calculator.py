# Personal Finance Calculator
# Monthly savings and project annual savings calculator script
# With a fixed interest rate to show the effect of compound interest.

monthly_income = float(input ("Enter your monthly income: "))
Total_monthly_expenses = float(input ("Enter your total monthly expenses: "))
# Calculate the monthly savings by subtracting monthly expenses from the monthly income.
monthly_savings = int(monthly_income) -  int(Total_monthly_expenses)
print ("Your monthly savings are", monthly_savings)

# Project Annual Savings
interest_rate = 0.05
# Calculate projected savings after one year
projected_savings = (monthly_savings) * 12 + int(monthly_savings * 12 * 0.05)
print ("Project savings after one year, with interest, is: " , projected_savings)