initial_value = int(input("Enter the initial value: "))
step = int(input("Enter the step: "))

nums = []

for x in range(initial_value, 100, step):
    if sum(nums) >= 100:
        print(*nums)
        print("Sum of series: " + str(sum(nums)))
        break
    else:
        nums.append(x)
