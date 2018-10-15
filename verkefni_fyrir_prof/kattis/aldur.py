n = int(input())  #How many friends
friend_list = []
for x in range(n):
    num = int(input())
    friend_list.append(num)
lowest = friend_list[0]

for x in friend_list:
    if x < lowest:
        lowest = x
print(lowest)
