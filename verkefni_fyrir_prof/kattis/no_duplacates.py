sentence = input().split()

new_s = []

for x in sentence:
    if x not in new_s:
        new_s.append(x)

if sentence == new_s:
    print("yes")
if sentence != new_s:
    print("no")
