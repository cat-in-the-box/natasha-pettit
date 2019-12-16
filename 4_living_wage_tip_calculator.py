## c) living wage tip calculator
## assume coffeeshop with 3 employees, 20 customers/hour, $5 average order
## minimum wage for tipped employees in Oregon is $10.75, and living wage in Portland is $14.59
## in order to provide a living wage, each customer would have to tip at least $0.58, or about 12% on a $5 order

# Name the program for the user
print("Living Wage Tip Calculator \n")

# Ask user for total order amount
total_bill = input("What was the total bill? ")

# Ask user how the service was, and account for typing and user errors by breaking the loop for incorrect answers
while True:
    service = input("Was your service amazing, good, eh, or shitty? ")
    if service.lower() not in ('amazing', 'good', 'eh', 'shitty'):
        print("\n ~*~*~ TRY AGAIN! Please type 'amazing,' 'good,' 'eh,' or 'shitty' ~*~*~")
    else:
        break


# Calculate tip and total amounts based on answer to service question
if service == "good":
    print("Your tip is $", "{:.2f}".format(float(total_bill) * 0.18 + 0.58), ", which brings your server up to a living wage and then adds 18% for good service. Your total bill including tip is $", "{:.2f}".format(float(total_bill) * 1.18 + 0.58))
    
elif service == "amazing":
    print("Your tip is $", "{:.2f}".format(float(total_bill) * 0.25 + 0.58), ", which brings your server up to a living wage and then adds 25% for great service. Your total bill including tip is $", "{:.2f}".format(float(total_bill) * 1.25 + 0.58))
    
elif service == "eh":
    print("Your tip is $", "{:.2f}".format(float(total_bill) * 0.1 + 0.58), ", which brings your server up to a living wage and then adds 10% for good-ish service. Your total bill including tip is $", "{:.2f}".format(float(total_bill) * 1.10 + 0.58))
    
elif service == "shitty":
    print("Your tip is $", 0.58, ", which brings your server up to a living wage and doesn't add anything on top for good service. Your total bill including tip is $", "{:.2f}".format(float(total_bill) + 0.58))


###################
    

## a) average minimum wage tip calculator
## since my state doesn't have a lower minumum wage for tipped employees (yay!), I'll just pretend for this example that tipped minimum wage is $4 and full minimum wage is $10.75.
## in order to provide minimum wage, each customer would have to tip at least $1.01, or about 20% on a $5 order

# Name the program for the user
print("\nMinimum Wage Tip Calculator \n")

# Ask user for total order amount
total_bill = input("What was the total bill? ")

# Ask user how the service was, and account for typing and user errors by breaking the loop for incorrect answers
while True:
    service = input("Was your service amazing, good, eh, or shitty? ")
    if service.lower() not in ('amazing', 'good', 'eh', 'shitty'):
        print("\n ~*~*~ TRY AGAIN! Please type 'amazing,' 'good,' 'eh,' or 'shitty' ~*~*~")
    else:
        break


# Calculate tip and total amounts based on answer to service question
if service == "good":
    print("Your tip is $", "{:.2f}".format(float(total_bill) * 0.15 + 1.01), ", which brings your server up to minimum wage and then adds 15% for good service. Your total bill including tip is $", "{:.2f}".format(float(total_bill) * 1.15 + 1.01))
    
elif service == "amazing":
    print("Your tip is $", "{:.2f}".format(float(total_bill) * 0.25 + 1.01), ", which brings your server up to minimum wage and then adds 25% for great service. Your total bill including tip is $", "{:.2f}".format(float(total_bill) * 1.25 + 1.01))
    
elif service == "eh":
    print("Your tip is $", 1.01, ", which brings your server up to minimum wage and doesn't add any tip on top for good service. Your total bill including tip is $", "{:.2f}".format(float(total_bill) + 1.01))
    
elif service == "shitty":
    print("Your tip is $", 0.50, ", which brings your server close to (but not up to) minimum wage and doesn't add anything on top for good service. Your total bill including tip is $", "{:.2f}".format(float(total_bill) + 0.50))

