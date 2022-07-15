portion_down_payment = 0.25
current_savings = 0
r = 0.04
# portion_saved = 0.1
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

down_payment = total_cost * portion_down_payment
monthly_salary = annual_salary/12
monthly_investment_returns = r / 12  
months = 0
while current_savings < down_payment:
    current_savings += (monthly_salary*portion_saved) + (current_savings*monthly_investment_returns)
    months += 1
print(f'Number of months: {months}')
    
    
    
    
    
    