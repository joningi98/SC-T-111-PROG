loan = float(input("Input the cost of the item in $: "))
payment = 50.0
 
month = 0
debt = loan
 
if loan <= 1000:
    rate = 1.5
else:
    rate = 2
 
intrest_rate = float((debt / 100) * rate)
total_intrest = 0
 
while debt > 0:
    if payment <= debt:
        intrest_rate = float((debt / 100) * rate)
        debt = float(debt + intrest_rate - payment)
    elif payment >= debt+intrest_rate:
        intrest_rate = float((debt / 100) * rate)
        payment = debt + intrest_rate
        debt = 0.0
    total_intrest += intrest_rate                  
                   
                           
    month += 1
    print("Month:", month, "Payment:", round((payment) ,2), "Interest paid:", round((intrest_rate), 2), "Remaining debt:", round((debt), 2))

print("Number of months:", month)
print("Total interest paid:", round((total_intrest), 2))