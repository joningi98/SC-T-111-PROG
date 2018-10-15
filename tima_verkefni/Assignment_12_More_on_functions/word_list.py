import string

#build_wordlist() function goes here
def build_wordlist(a_file):
    word_list = []
    for line_str in a_file:
        line_list = line_str.split()
        if string.punctuation in line_list:
            line_list.remove(string.punctuation)
        for word in line_list:
            word = word.strip()
            word_list.append(word)
    return word_list

#find_unique() function goes here
def find_unique(my_list):
    unique_list = []
    for word in my_list:
        if word not in unique_list:
            unique_list.append(word)
    return unique_list

def main():
    infile = open("test.txt", 'r')
    word_list = build_wordlist(infile)
    infile.close()
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print(new_wordlist)

main()
