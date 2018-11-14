class Order(object):

    def __init__(self, product='', price=0, quantity=0, discount=0.00):
        self.product = product
        self.price = price
        self.quantity = quantity
        self.discount = discount

    def get_total(self):
        return self.quantity * self.price

    def get_discount_of_product(self):
        return (self.get_total() / 100) * self.discount


def print_total_order(my_order):
    header()
    for x in my_order:
        print("{:<8} {:<8} {:<12} {:<12} {:<10}".format(x.product, x.price, x.quantity, str(x.discount), round(x.get_total())))
    print("=" * 50)
    print("Total excluding discount: {:>22}".format(round(total_price_of_order(my_order))))
    print("Total discount: {:>30}".format(round(get_discount(my_order))))
    print("Total: {:>41}".format(round(total_price_of_order(my_order) - get_discount(my_order))))


def total_price_of_order(data):
    price = []
    for x in data:
        price.append(x.get_total())
    return sum(price)


def get_discount(data):
    discount = []
    for x in data:
        discount.append(x.get_discount_of_product())
    return sum(discount)


def header():
    print("{:<8} {:<8} {:<12} {:<12} {:<10}".format("Product", "Price", "Quantity", "Discount", "Total"))
    print("=" * 50)


def main():
    order_1 = Order("Eggs", 60, 12, 0)
    order_2 = Order("Bread", 200, 1, 10)
    order_3 = Order("Milk", 120, 2, 5)
    my_order = [order_1, order_2, order_3]
    print_total_order(my_order)


main()

