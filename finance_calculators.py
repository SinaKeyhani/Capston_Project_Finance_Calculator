
# First Capstone project: 
# Welcome the user by asking their names
# Asking  which form between investment and bond they want to proceed
# For 'investment' asking the required questions and providing the result
# For 'bond' asking the required questions and provinding monthly repayments




import math

User_name = input('Please enter your name: \n')
if len(User_name) == 0: 
    print("Please enter your Name:  ")

else:  
    print(f"Hi {User_name}, Welcome to our Bank \n Please Choose either 'investment' or 'bond'to proceed: ")
user_input = input().lower()

# Based on user input for investment or bond, I use an if statement to provide more information. 
# If the user chooses 'investment', we need to collect more information as dictated by the case study.

if user_input == 'investment':
    amount = float(input("Please enter the amount you would like to put as a deposite: £ "))
    interest_rate =  float(input("Please enter interest rate as a number: % "))
    num_years = int(input("Please enter number of year: "))
    interest = input("please enter simple or compound interest: ").lower()
    
# As investments have two options, 'simple' and 'compound', I used a nested if statement to calculate each of them based on the user's input.

    if interest == "simple": 
      result =  amount *(1 + interest_rate / 100 * num_years)
      print(f"The result for your investment is £{round(result,3)}") 
    
    elif interest == "compound": 
        result = amount * math.pow((1 + interest_rate / 100), num_years)
        print(f" The resuld of your investment is £ {round(result,3)}")
    
    else: 
        print("Invalid interest type for investment.") 
        
# If the user chooses the bond option, we need to ask for different data from them to calculate the amount of money that they will have to repay

elif user_input == 'bond': 
    present_value = float(input("Please enter the current value of your home: £ "))
    interest_rate = float(input("Please enter the interest rate: % "))/100/12
    num_month = int(input("Enter the number of months to repay the bond: "))
    repay = (interest_rate * present_value) / (1 - (1 + interest_rate)**(-num_month))
    print (f" The monthly repayment is £{round(repay,3)}")

else: 
    print("Invalid choice. Please enter 'investment' or 'bond'.")

