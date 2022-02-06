# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 15:40:09 2022

@author: Administrator
"""
annual_salary = int(input('please enter your annual salary: '))

down_cost = 250000
current_savings = 0
annual_investment_return = 0.04
monthly_investment_return = 0.04/12
annual_raise = 0.07




def saving(my_annual_salary,my_annual_raise,guessed_saving_rate):
    
    #create a saving pocket
    current_savings = 0
    #start a counter for the 36 month to follow your annual raise
    for month in range(0,36):

        if month % 6 != 0 :
            #assigning the monthly saving
            monthly_saving = (my_annual_salary/12)*guessed_saving_rate
        else:
            #adding the annual raise
            my_annual_salary = my_annual_salary*(1+annual_raise)
            #assigning the new monthly salary saving for the new annual salary
            monthly_saving = (my_annual_salary/12)*guessed_saving_rate
        #the monthly invesment return
        monthly_return = current_savings*monthly_investment_return
        #adding the monthly salary saving and the monthly invesment return
        current_savings += monthly_saving + monthly_return


    return current_savings



def checking_best_percentage():
    #our guess  info start
    high = 1
    low = 0
    #intial guess start
    guess = 0.5
    #steps counter
    steps = 0
    
    while guess < 1 :
        #checking the total savings
        guessed_savings = saving(annual_salary,annual_raise,guess)
        
        """
        -if our savings is higher than the down payment with 100$ 
        then we will need to increase our saving percentage guess
        - if our savings is lower than the down payment with 100$
        then we will decrease saving percentage
        - if it was near the 100$ we will break the while loop
        - we have here two reasons to break this loop 
        first if the guess is more than 1 
        second if we have reached our saving goal
        """
        
        if guessed_savings - down_cost > 100:
             high = guess 
             guess = (high + low)/2
             steps += 1
        elif guessed_savings - down_cost < -100 :
            low = guess
            guess = (high + low)/2
            steps += 1
        else:
            break
    """
     checking if our while loop was broke beacuse of the guess exceed 1 
     or we have reached our goal
    """
    if guess == 1 :
        print("you can't save this money in 36 month")
    else:
        guess = round(guess,4)   
        print('best saving rate is:', guess)
        print('steps in binary search :', steps)
        
        
checking_best_percentage()
            
            