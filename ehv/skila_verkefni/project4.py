while True:
    try:
        shares = float(input("Enter number of shares: "))
        while True:
            try:
                price, numerator, denominator = input("Enter price (dollars, numerator, denominator): ").split(' ')
                price_int = float(price)
                numerator_int = float(numerator)
                denominator_int = float(denominator)
                total_value = float(shares * (price_int + (numerator_int / denominator_int)))
                total_value = ("%.2f" % total_value)
                print(str(round(shares)) + " shares with market price " + str(price) + " " + str(numerator) + "/" + str(denominator) + " have value $" + str(total_value))
                break
            except ValueError:
                print("Invalid price!")
                continue
    except ValueError:
        print("Invalid number!")
        continue

    resume = input("Continue: ")

    if resume != 'y':
        break