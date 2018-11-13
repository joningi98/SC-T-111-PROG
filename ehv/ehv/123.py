def get_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as data_file:
            data_list = []  # start with an empty list
            for line_str in data_file:
                data_list.append(line_str.replace("%", "").strip().split(','))
            return main(data_list)
    except FileNotFoundError:
        print("Cannot find file", file_name)
        header()


def find(file, stadur):
    listi = []
    for line in file:
        if line[0] == 'State':
            continue
        listi.append(float(line[stadur]))
    return listi


def find_state(file, value, stadur):
    for line in range(len(file)):
        if file[line] == file[0]:
            continue
        elif float(file[line][stadur]) == value:
            return str(file[line][0])


def header():
    print('{:<33}{:<21}{:>6}{:^6}{:<15}{:>6}'.format("Indicator", "Min", "", "", "Max", ""))
    print("-" * 87)


def main(data):
    header()
    for x in [1, 5, 7, 11, 13]:
        print('{:<33}{:<21}{:>6}{:^6}{:<15}{:>6}'.format(data[0][x] + ":", find_state(data, min(find(data, x)), x), round(min(find(data, x)), 1), "", find_state(data, max(find(data, x)), x), round(max(find(data, x)), 1)))


get_file(input("Enter filename containing csv data: "))
