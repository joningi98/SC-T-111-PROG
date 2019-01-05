def make_list():
    N = int(input())
    M = int(input())

    count = 1

    my_list = []

    for x in range(N):
        arr = []
        for y in range(M):
            arr.append(count)
            count += 1
        my_list.append(arr)

    print(my_list)


def some_list():
    matrix_len = int(input())

    my_list = []

    for _ in range(matrix_len):
        num = input("num: ").split()
        my_list.append([int(x) for x in num])
    return my_list


list1 = some_list()
list2 = some_list()
print(list1)
print(list2)


new_list = []

for x, y in zip(list1, list2):
    new_list.append(x + y)

print(new_list)

