

def make_new_row(new_row):
    if len(new_row) == 0:
        return [1]
    if len(new_row) == 1:
        return [1,1]
    next_list = [1]
    for i in range(len(new_row)):
        if i == len(new_row) - 1:
            next_list.append(1)
        else:
            next_list.append(new_row[i] + new_row[i+1])
    return next_list


height = int(input("Height of Pascal's triangle (n>=1): "))
new_row = []
for i in range(height):
    new_row = make_new_row(new_row)
    print(new_row)


