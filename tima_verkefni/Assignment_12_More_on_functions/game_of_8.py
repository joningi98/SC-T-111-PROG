

#game_of_eights() function goes here
def game_of_eights(a_list):
    for i in range(len(a_list)-1):
        if a_list[i] == a_list[i+1] and a_list[i] == '8':
            return True
    return False


def main():
    try:
        a_list = input("Enter elements of list separated by commas: ").split(',')
        for i in a_list:
            i = int(i)
    except ValueError:
        print("Error. Please enter only integers.")
        exit()
    print(game_of_eights(a_list))
    # remainder of main() goes here


main()
