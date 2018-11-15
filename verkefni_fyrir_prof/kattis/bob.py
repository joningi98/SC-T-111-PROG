sentence = input().split()

new_s = []

for x in sentence:
    for y in x:
        if y not in new_s:
            new_s.append(y)


for j in new_s:
    print(j, end='')