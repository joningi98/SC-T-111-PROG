import random
import string


def get_word_string(filename):
    try:
        with open(filename, 'r') as file:
            word_string = ''
            for line in file:
                word_string += line
            return word_string
    except FileNotFoundError:
        print('{} {} {}'.format("File", filename, "not found"))


def scramble_string(word_string):
    word_list = word_string.strip().split()
    scramble_list = []
    for word in word_list:
        last = word[-1]
        if last in string.punctuation:
            if len(word) <= 4:
                scramble_list.append(word)
            else:
                first, mid, last = word[0], list(word[1:-2]), word[-2:]
                random.shuffle(mid)
                new_word = first + ''.join(mid) + last
                scramble_list.append(new_word)
        elif len(word) >= 4 and last not in string.punctuation:
            first, mid, last = word[0], list(word[1:-1]), word[-1]
            random.shuffle(mid)
            new_word = first + ''.join(mid) + last
            scramble_list.append(new_word)
        else:
            scramble_list.append(word)
    return ' '.join(scramble_list)


# Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)
