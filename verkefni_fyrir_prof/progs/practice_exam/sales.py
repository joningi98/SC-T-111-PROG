

def open_file(file):
    try:
        sales_list = []
        with open(file, "r") as data:
            for line in data.readlines():
                sale = []
                for num in line.split():
                    if num.isdigit():
                        sale.append(int(num))
                if sale:
                    sales_list.append(sale)
        return sales_list
    except FileNotFoundError:
        print("File not found!")


def calc_average(sales_list):
    average_sales = []
    for sales in sales_list:
        total_value = 0
        for sale in sales:
            total_value += sale
        average_sales.append(total_value / len(sales))
    return average_sales


def print_sales(average_sales):
    count = 1
    print("Average sales:")
    for sale in average_sales:
        print("Department no. {}: {:.1f}".format(count, sale))
        count += 1


def main():
    file_name = input("Enter file name: ")
    data = open_file(file_name)
    average_sale = calc_average(data)
    print_sales(average_sale)

main()