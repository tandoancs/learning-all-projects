
# Get details of loan

money_owed = float(input('How much  money do you owe, in dollars?\n'))
apr = float(input('What is the amnual percentage rate of the loan?\n'))
payment = float(input('How much will you pay off each month in dollars?\n'))
months = int(input('How many months do you want to see the results for?\n'))

monthly_rate = apr / 100 / 12

for i in range(months):

    #Calculate interest to pay
    interest_paid = money_owed * monthly_rate

    # Add in interest
    money_owed = money_owed + interest_paid

    # Make payment
    money_owed = money_owed - payment

    print('Paid', payment, 'of which', interest_paid, 'was interest')
    print('Now I owe', money_owed)