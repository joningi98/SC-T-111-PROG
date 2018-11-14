num_of_tests = int(input())

my_list = []

for x in range(num_of_tests):
    my_list.append(0)
print(my_list)

for x in range(1, num_of_tests + 1):
    a, b = input().split()
    b = int(b)
    a = int(a)
    my_list[a-1] = b
    if 0 in my_list:
        print("Case #{}: OFF".format(x))
    if 0 not in my_list:
        print("Case #{}: ON".format(x))

    print(my_list)
