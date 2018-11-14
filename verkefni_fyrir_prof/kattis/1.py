num = int(input())

my_list = []

for x in range(1, num + 1):
    print("Test {}".format(x))
    a, b = input().split()
    a = int(a)
    b = int(b)
    my_list = []
    for y in range(a):
        star = input()
        my_list.append(star)
    my_list.reverse()
    for x in my_list:
        print(x[::-1])