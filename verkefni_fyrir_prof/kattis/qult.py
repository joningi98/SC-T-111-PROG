length = int(input())

life = []

for a in range(length):
    i, j = input().split()
    x = float(i)
    y = float(j)
    life.append(y * x)

print("%.3f" % sum(life))



