def open_file(filename):
    try:
        with open(filename, "r") as file:
            sales = []
            for line in file.readlines():
                company_sale = []
                for num in line.strip().split():
                    if num.isdigit():
                        company_sale.append(int(num))
                if len(company_sale) != 0:
                    sales.append(company_sale)
        return sales
    except FileNotFoundError:
        print("File not found")
        quit()


def average_sales(sales):
    count = 1
    print("Average sales:")
    for sale in sales:
        print("Department no. {}: {:.1f}".format(count, sum(sale) / len(sale)))
        count += 1


def main():
    file_name = input("Enter file name: ")
    sales = open_file(file_name)
    average_sales(sales)


main()