def countcharacters(word):
    upper = 0
    lower = 0
    for x in range(len(word)):
        if word[x].isupper():
            upper += 1
        elif word[x].islower():
            lower += 1

    return upper, lower


user_input = input("Enter a string: ")

# Call the function here
upper, lower = countcharacters(user_input)
print("Upper case count: ", upper)
print("Lower case count: ", lower)