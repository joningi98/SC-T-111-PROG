cons = []

for x in range(5):
    nums = [int(x) for x in input().split()]
    cons.append(nums)


best_score = 0
best_con = 0


for i, j in enumerate(cons, start=1):
    if sum(j) > best_score:
        best_score = sum(j)
        best_con = i


print(best_con, best_score)