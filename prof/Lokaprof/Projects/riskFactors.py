def get_file(filename):
    try:
        with open(filename, "r") as file:
            csv_list = []
            for line in file.readlines():
                csv_list.append(line.replace("%", "").strip().split(','))
        return main(csv_list)
    except FileNotFoundError:
        print("File {} not found.".format(filename))


def find_data(my_list, state):
    data_list = []
    for line in my_list:
        if line[0] == "State":
            continue
        data_list.append(float(line[state]))
    return data_list


def find_state(file, value, state):
    for line in range(len(file)):
        if file[line] == file[0]:
            continue
        elif float(file[line][state]) == value:
            return str(file[line][0])


def header():
    print('{:<33}{:<21}{:>6}{:^6}{:<15}{:>6}'.format("Indicator", "Min", "", "", "Max", ""))
    print('-' * 87)


def main(data):
    header()
    for x in [1, 5, 7, 11, 13]:
        print('{:<33}{:<21}{:>6}{:^6}{:<15}{:>6}'.format(data[0][x] + ":", find_state(data, min(find_data(data, x)), x), round(min(find_data(data, x)), 1), "", find_state(data, max(find_data(data, x)), x), round(max(find_data(data, x)), 1)))


get_file(input("Enter filename containing csv data: "))