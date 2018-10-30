

class Sales(object):
    def __init__(self):


    def read_data_from_file(self, ):













def main():
    data = read_data_from_file("sales.txt")
    sales = Sales(data)
    average_sales = sales.get_average()
    print("Average sales: {:.2f}".format(average_sales))
    sales.add_sale(78.5)
    average_sales = sales.get_average()
    print("Average sales: {:.2f}".format(average_sales))

main()