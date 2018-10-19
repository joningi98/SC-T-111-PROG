def resume():
    x = input("Continue: ")
    if x != 'y':
        exit()


def stock():
    while True:
        try:
            shares = input("Enter number of shares: ")
            calculate_total_value(shares)
            break
        except ValueError:
            print("Invalid price!")


def calculate_total_value(shares):
    while True:
        try:
            p, n, d = input("Enter price (dollars, numerator, denominator): ").split()
            dollars, numerator, denominator = float(p), float(n), float(d)
            total_value = float(shares) * (dollars + (numerator / denominator))
            total_value = ("%.2f" % total_value)
            print(shares + " Shares with market price", round(dollars), str(round(numerator)) + "/" + str(round(denominator)), "have value $" + total_value)
            break
        except ValueError:
            print("Invalid price!")


while True:
    stock()
    resume()





