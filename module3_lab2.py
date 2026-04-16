income = float(input("Enter the annual income: "))  #code will read users income and then use to predict tax 

if income >= 1 and income <= 85528:

    tax = ((income*0.18)-556.02)

elif income >= 85529 and income <=999999: 
    tax = (14839.02*0.18) + (((income-85528)*0.32)*0.18) 
    
if income >= 1000000:
    tax = (income*0.40)

else: 
    print("Invalid income, or no tax to be paid")

tax = round(tax, 0)

print("The tax is:", tax, "thalers")
