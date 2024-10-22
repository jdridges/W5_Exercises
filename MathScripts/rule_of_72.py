# rule of 72 is 72/IR
current_savings = 100000.00
doubled_savings = current_savings * 2
interest_rate = 6
years_to_double = 72/interest_rate

print("At a "+ str(interest_rate)+ "%"+ " interest rate, your savings account will be worth "+ format(doubled_savings, ".2f")+" in "+ format(years_to_double, ".1f")+" years")