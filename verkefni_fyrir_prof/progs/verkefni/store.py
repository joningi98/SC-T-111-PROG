

def open_file(file_name):
    cost = []
    with open(file_name, "r") as file:
        for price in file.readlines():
            cost.append(int(price))
    return cost


def main():
    file_name = "list.txt"
    cost = open_file(file_name)
    price = sum(cost)
    discount = price * 0.10
    if price >= 10000:
        total_price = price - discount
    else:
        total_price = price

    print("Price:\t{:14}".format(round(price)))
    print("Discount:\t{:10}".format(round(discount)))
    print("-" * 22)
    print("Total price:{:>10}".format(round(total_price)))

main()
