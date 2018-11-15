def make_list(word):
    my_list = []
    for x in word:
        if x == ' ':
            continue
        my_list.append(x)
    return my_list


def encoding(my_list):
    for x in my_list:
        print(x, my_list.count(x), end='')



def decoding(my_list):
    for i, j in enumerate(my_list):
        if j.isdigit():
            j = int(j)
            print(word[i - 1] * j, end='')


word = input()
my_list = make_list(word)

if word[0] == 'E':
    encoding(word)
if word[0] == 'D':
    decoding(word)
