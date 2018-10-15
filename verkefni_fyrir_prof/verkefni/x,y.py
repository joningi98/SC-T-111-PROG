n, m = [int(x) for x in input("enter numbers plz: ").split()]
arr = []

for x in range(n):
    st = input()
    arr.append(st)

for x in range(n):
    for y in range(len(arr)):
        print(arr[x][y])
