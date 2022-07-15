portion_down_payment = 0.25
current_savings = 0.0
r = 0.04
best_rate = 0
semi_annual_raise = 0.07

annual_salary = float(input("Enter your annual salary: "))
total_cost = float(input("Enter the cost of your dream home: "))


down_payment = total_cost * portion_down_payment
monthly_salary = 0
total_income = 0

low = 0
high = 10000
epsilon = 100
bisection_searches = 0
br = (high + low)/2.0

while abs(current_savings - down_payment) >= epsilon and bisection_searches <= 13: # log 10000 is a bit greater than 13
    current_savings = 0.0 # reset current savings
    reset_annual_salary = annual_salary # resetting the annual salary for use in the "for loop"
    
    for number_of_months in range(36):  # using the for loop to calculate the current savings for 3 years i.e 36 months
        if number_of_months % 6 == 0 and number_of_months != 0:  # if it's the 6th, 12th, 18th ...
            reset_annual_salary += (semi_annual_raise * reset_annual_salary)  # increasing annual salary w the raise
        monthly_salary = reset_annual_salary / 12.0  # monthly salary
        current_savings += (current_savings * 4 / 1200) +\
                           (br * monthly_salary) / 10000.0  # update current savings

    if current_savings < down_payment:  # binary / bisection search begins
        low = br
    else:
        high = br
    br = (low + high) / 2.0
    bisection_searches += 1
    

if bisection_searches > 13:  # if it took more than 13 bisection searches i.e log10000 , then ...
    print("Cannot afford house in 3 years")
else:
    print("Best Rate = ", br/10000)
    
# Reference: https://github.com/Nkumah7/MIT_OCW_6.0001_Probelm_Sets_Assignments/blob/master/mit_pset1/ps1c.py