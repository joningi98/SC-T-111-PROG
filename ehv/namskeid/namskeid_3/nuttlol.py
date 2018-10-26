loan = float(input("input loan "))
payment = 50

month = 0
debt = loan

if loan <= 1000:
    rate = 1.5
else:
    rate = 2

intrest_rate = float((debt / 100) * rate)

while debt > 0:
    if payment <= debt:
        intrest_rate = float((debt / 100) * rate)
        debt = float(debt + intrest_rate - payment)
    else:
        intrest_rate = float((debt / 100) * rate)
        debt = float(payment - debt + intrest_rate)
        payment = debt + intrest_rate
        break
        
   
            
    month += 1
    print("Month:", month, "Payment:", round((payment) ,2), "intrest paid:", round((intrest_rate), 2), "Remaing debt:", round((debt), 2))
