def sort_list(my_list):
    return a_list.sort()

# sort_list() function goes here

a_list = []

def main():
    while True:
        try:
            num = input("")
            num = int(num)
            a_list.append(num)
        except ValueError:
            break


    # loop to accept integers until a non-digit is entered goes here

    ######Do not modify this part######
    print(a_list)
    print(sort_list(a_list))
    print(a_list)
    ######Do not modify this part######


main()
