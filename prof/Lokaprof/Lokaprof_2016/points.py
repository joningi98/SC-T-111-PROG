def open_file(filename):
    try:
        with open(filename, 'r') as file:
            file_list = []
            for line in file.readlines():
                points = []
                x, y = line.rstrip().split()
                points.append(int(x))
                points.append(int(y))
                file_list.append(points)
        return file_list
    except FileNotFoundError:
        print("File {} not found".format(filename))


def find_range(data):
    nums_in_range = []
    for points in data:
        if points[0] <= 50 and points[1] <= 50:
            nums_in_range.append(points)
    return nums_in_range


def print_points(numbers):
    print("Points in the upper left quadrant are:")
    for x in numbers:
        print(*x)


def main():
    file_name = input("Enter name of file ")
    data = open_file(file_name)
    nums_in_range = find_range(data)
    print_points(nums_in_range)


main()



