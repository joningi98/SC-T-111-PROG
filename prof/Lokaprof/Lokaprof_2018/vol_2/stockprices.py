import time


def open_file():
    """
    Prompts the user for a file name.
    Returns the corresponding file stream or None if file not found
    """
    try:
        file_name = input("Enter file name: ")
        data = []
        filestream = open(file_name, "r")
        for line in filestream:
            if line[0].isdigit():
                data.append(line.strip())
        filestream.close()
        return data
    except FileNotFoundError:
        print("File not found!")
        quit()


def split_sales(sale):
    if ";" in sale:
        sales = sale.split(";")
    else:
        sales = sale.split()
    return sales


def make_dict(file_stream):
    sales_dict = {}
    for sale in file_stream:
        sales = split_sales(sale)
        date = sales[0][:7]
        money = float(sales[1])
        if date in sales_dict.keys():
            sales_dict[date].append(money)
        else:
            sales_dict[date] = [money]
    return sales_dict


def display_dict(sales_dict):
    for date, sale in reversed(sorted(sales_dict.items())):
        print("{} {:.2f}".format(date, sum(sale) / len(sale)))


def main():
    file_stream = open_file()
    sales_dict = make_dict(file_stream)
    display_dict(sales_dict)


main()
