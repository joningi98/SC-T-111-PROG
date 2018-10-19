loan = float(input("Input the cost of the item in $: "))
debt = loan
payment = 50.0
month = 0

if loan > 1000:
    interest_rate = 2.0
else:
    interest_rate = 1.5

added_interest = (debt / 100) * interest_rate
total_interest = 0

while debt > 0:
    month += 1
    if payment <= debt:
        added_interest = (debt / 100) * interest_rate
        debt = added_interest + debt - payment
    elif payment >= added_interest + debt:
        added_interest = (debt / 100) * interest_rate
        payment -= added_interest + debt
        debt = 0.0
    total_interest += added_interest
    print('-' * 78)
    print('Month: {}  Payment {}  Interest paid: {}  Remaining debt: {}'.format(month, round(payment, 2), round(added_interest, 2), round(debt, 2)))
print('-' * 78)
print("Number of months", month)
print("Total interest paid", round(total_interest, 2))
