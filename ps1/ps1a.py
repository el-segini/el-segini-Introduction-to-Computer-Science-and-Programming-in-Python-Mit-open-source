# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 08:22:04 2022

@author: Administrator
"""

cost_of_house = float(input("enter your dream house cost: "))
annual_salary = float(input("enter your annual salary: "))
portion_saved = float(input('your salary saving percentage: '))


portion_down_payment = 0.25
current_savings = 0
annual_investment_return = 0.04
monthly_investment_return = 0.04/12
goal = portion_down_payment*cost_of_house
monthly_invest_r = 0.04/12
month = 0

while current_savings < goal :
    monthly_saving = (annual_salary/12)*portion_saved
    monthly_return = current_savings*monthly_investment_return
    current_savings += monthly_saving + monthly_return
    month += 1
    
    
print('number of months:',month)