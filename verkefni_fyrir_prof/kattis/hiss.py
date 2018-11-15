word = input()


hiss = False


for x in range(len(word)):
    if x + 1 >= len(word):
        break
    elif word[x] == 's' and word[x+1] == 's':
        hiss = True


if hiss == True:
    print("hiss")
else:
    print("no hiss")






