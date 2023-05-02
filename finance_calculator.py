import math

print("investment\t -to calculate the amount of interest you'll earn on interest")
print("bond\t -to calculate the amount you'll have to pay on a home loan.")
print("\n")
user_1 = input("Choose either 'Investment' or 'Bond' from menu below to proceed:\n")  # declaring a user that is to enter either bond or investment

if user_1.lower() == "investment":
    print("You are now logged on to Investment Calculator; \n")
    deposit = float(input("How much would you like to Deposit ?"))
    interest_rate = float(input("What is you Interest rate"))
    num_of_years = float(input("Please Enter the Number of Years you want to Invest"))  # investment
    interest = input("Do you want Simple interest or Compound interest ?")  # investment Nested if for Simple interest and comound
    if interest.lower() == "simple interest": # nested if statement inside investment to choose interest
        print("You have Selected Simple Interest: \n")
        '''
        Formular to calculate Simple interest for  investment
        '''
        simple_interest = deposit * (1 + interest_rate / 100 * num_of_years)

        print("Total Simple Interest Investment{}".format(simple_interest)) # displaying the total
    elif interest.lower() == "compound interest":
        print("You have Selected Compound Interest: \n")
        '''
               Formular to calculate Compound for  investment
               '''
        compound = deposit * math.pow((1 + interest_rate / 100) ,num_of_years) #compound  formula
        print("Total Compound Interest Investment{}".format(compound))
elif user_1.lower() == "bond":
    print("You have Choosen Bond\n") #Users Input for the Bond selection
    property_cost = float(input("How much is the Value of the House"))
    interest_rate = float(input("What is your Interest Rate"))
    payment_plan = float(input("How many Months are you planning to take the Bond"))
    bond_repayment = (interest_rate / 12 * property_cost)/(1 - math.pow((1+interest_rate / 100), (- payment_plan))) #formular
    print("Total Bond Repayment :{}".format(bond_repayment)) # displaying total
