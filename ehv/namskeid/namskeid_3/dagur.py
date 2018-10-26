top_num = int(input("Input a number between 0 and 999: "))

for num in range(0, top_num):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    
    if num = sum:
        print(num)