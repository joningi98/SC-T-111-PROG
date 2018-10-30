
def read_data_from_file(file):
    data_list = []
    with open(file, 'r') as file:
        for num in file.readlines():
            new_num = num.strip()
            data_list.append(new_num)
        return data_list


class Sales(object):
    def __init__(self, data_list):
        self.__data = data_list

    def add_sale(self, num=0.0):
        return self.__data.append(num)

    def get_average(self):
        summa = 0
        for x in self.__data:
            summa += float(x)
        length = len(self.__data)
        average = summa / length
        return float(average)


def main():
    data = read_data_from_file("sales.txt")
    sales = Sales(data)
    average_sales = sales.get_average()
    print("Average sales: {:.2f}".format(average_sales))
    sales.add_sale(78.5)
    average_sales = sales.get_average()
    print("Average sales: {:.2f}".format(average_sales))

main()