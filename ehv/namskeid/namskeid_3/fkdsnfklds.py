loan = int(input("input loan"))
payment = float(input("input pay "))

month = 0
debt = loan

if loan <= 1000:
    rate = 1.5
else:
    rate = 2

intrest_rate = round(float((debt / 100) * rate), 2)

while debt >= 0:    
    if debt > payment:         
        debt = round(float(debt + intrest_rate - payment), 2)
    if debt < payment:
        payment -= 1.0
    month += 1    
    print("Month:", month,"Payment:", payment, "intrest paid:", intrest_rate, "Remaing debt:", debt)

print(month, round(intrest_rate, 2), debt)