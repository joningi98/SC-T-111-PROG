

def populate_list(my_list):
    word = input("Enter value to be added to list: ")
    while word.lower() != 'exit':
        my_list.append(word)
        word = input("Enter value to be added to list: ")

def triple_list(initial_list):
        return initial_list * 3

initial_list = []
populate_list(initial_list)
new_list = triple_list(initial_list)

for items in new_list:
    print(items)

