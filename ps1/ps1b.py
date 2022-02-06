cost_of_house = float(input("enter your dream house cost: "))
annual_salary = float(input("enter your annual salary: "))
portion_saved = float(input('your salary saving percentage: '))
semi_annual_raise = float(input('enter your semi annual raise :'))

portion_down_payment = 0.25
current_savings = 0
annual_investment_return = 0.04
monthly_investment_return = 0.04/12
goal = portion_down_payment*cost_of_house
monthly_invest_r = 0.04/12
month = 0

while current_savings < goal :
    
    if month % 6 != 0 :
            #assigning the monthly saving
        monthly_saving = (annual_salary/12)*portion_saved
    else:
            #updating the annual salary after raise
        annual_salary = annual_salary*(1+semi_annual_raise)
            #assigning the new monthly salary saving for the updated annual salary
        monthly_saving = (annual_salary/12)*portion_saved
    #the monthly invesment return
    monthly_return = current_savings*monthly_investment_return
    #adding the monthly salary saving and the monthly invesment return
    current_savings += monthly_saving + monthly_return
    month += 1
    
print(month)