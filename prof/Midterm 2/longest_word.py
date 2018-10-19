# Function definitions start here
def open_file(filename):
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        print()

def get_longest_word(file_stream):
    data = file_stream.readlines()
    my_word = "a"
    for word in data:          # Read a file line by line
        word = word.strip()
        if len(word) > len(my_word):
            my_word = word
    return my_word


# The main program starts here
filename = input("Enter name of file: ")
file_stream = open_file(filename)
if file_stream:
    longest_word = get_longest_word(file_stream)
    print("Longest word is '{:s}' of length {:d}".format(longest_word, len(longest_word)))
    file_stream.close
else:
    print('File', filename, 'not found!')
