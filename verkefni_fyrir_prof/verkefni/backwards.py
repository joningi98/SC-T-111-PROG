my_string = input("enter here plz: ")


def reverse(my_string):
    for x in range(len(my_string)-1, -1, -1):
        print(my_string[x], end=" ")


reverse(my_string)
