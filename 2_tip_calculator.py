##Calculate tip, quantitative

bill_total = input("How much was the meal? ")

percentage = input("What percent would you like to tip? ")

print("Your tip is $", float(bill_total) * float(percentage) * 0.01, ", and your total bill including tip is $", float(bill_total) + (float(bill_total) * float(percentage) * 0.01))

print("-------------------------------")

##Calculate tip, qualitative

total_bill = input("What was the total bill? ")

service = input("Was your service amazing, good, eh, or shitty? ")

if service == "good":
    print("Your tip is $", float(total_bill) * 0.22, ", and your total bill including tip is $", float(total_bill) * 1.22)
    
elif service == "amazing":
    print("Your tip is $", float(total_bill) * 0.28, ", and your total bill including tip is $", float(total_bill) * 1.28)
    
elif service == "eh":
    print("Your tip is $", float(total_bill) * 0.18, ", and your total bill including tip is $", float(total_bill) * 1.18)
    
elif service == "shitty":
    print("Your tip is $", float(total_bill) * 0.1, ", and your total bill including tip is $", float(total_bill) * 1.1)
