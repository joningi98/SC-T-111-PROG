loan = int(input("input loan"))
payment = int(input("input pay "))

month = 0
debt = loan

a_rate = 1.5
i_rate = round(float((loan / 100) * a_rate), 2)

while debt >= 0:
    if debt < payment:
        payment -= 1      
    else:       
        debt = round(float((debt + i_rate) - payment), 2)
   
    month += 1    
    print("Month:", month,"Payment:", payment, "intrest paid:", i_rate, "Remaing debt:", debt)

#print(month, round(i_rate, 2), i)

