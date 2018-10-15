def open_file(filename):
    try:
        with open(filename, 'r') as f:
            data_in_states = []
            lines = f.readlines()
            for line in lines:
                data_in_states.append(line.replace("%", "").strip().split(','))
            return data_in_states
    except FileNotFoundError:
        print("Cannot find file", filename)
        print('{:<33}{:<21}{:>6}{:^6}{:<15}{:>6}'.format("Indicator", "Min", "", "", "Max", ""))
        print("-" * 87)
        quit()


def data(opened_file, num):
    array = []
    for x in opened_file:
        if x[0] == "State":
            continue
        array.append(float(x[num]))
    return array


def state(open_file, num, maxi):
    for line in range(len(open_file)):
        if open_file[line] == open_file[0]:
            continue
        elif float(open_file[line][num]) == maxi:
            return str(open_file[line][0])


filename = input("Enter filename containing csv data: ")
opened_file = open_file(filename)
disease = [1, 5, 7, 11, 13]

print('{:<33}{:<21}{:>6}{:^6}{:<15}{:>6}'.format("Indicator", "Min", "", "", "Max", ""))
print("-" * 87)

for x in disease:
    maxi = max(data(opened_file, x))
    mini = min(data(opened_file, x))
    print('{:<33}{:<21}{:>6}{:^6}{:<15}{:>6}'.format(opened_file[0][x], state(opened_file, x, mini), mini, "", state(opened_file, x, maxi), maxi))

