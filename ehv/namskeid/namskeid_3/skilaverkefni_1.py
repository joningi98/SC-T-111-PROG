loan = int(input("Please enter the loan aount in $: "))
monthly_payment = int(input("Please enter your monthly payment $: "))
    
if loan < 1000:
    m_rate = 1.5
if loan > 1000:
    m_rate = 2.0

intrest_rate = loan/ 100 * m_rate



while loan < 0:
    (loan + intrest_rate) - monthly_payment 

print(loan)

