

def list_to_tuple(a_list):
    while True:
        a_tuple = ()
        new_list = []
        try:
            for element in a_list:
                new_list.append(int(element))
            a_tuple = tuple(new_list)
            return a_tuple
        except ValueError:
            print("Error. Please enter only integers.")
            return a_tuple


a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_tuple(a_list)
print(a_tuple)