class Contacts(object):
    def __init__(self, name='', number=0, address=''):
        self.__name = name
        self.__number = number
        self.__address = address

    phone_book = {}

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def set_address(self, address):
        self.__address = address

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    def get_address(self):
        return self.__address

    def __str__(self):
        return "Name: {}\nNumber: {}\nAddress: {}".format(self.__name, self.__number, self.__address)


def add_contact():
    while True:
        try:
            name = input("Enter name: ")
            number = int(input("Enter number: "))
            address = input("Enter address: ")
            Contacts(name, number, address)
            Contacts.phone_book[name] = [number, address]
            break
        except ValueError:
            print("Incorrect input\n")


def edit_contact():
    try:
        print("1. Edit name\n2. Edit number and address\n3. Back")
        user_choice = int(input(""))
        if user_choice == 1:
            old_name = input("Enter name to edit: ")
            if old_name not in Contacts.phone_book.keys():
                print("Name not found\n")
            else:
                new_name = input("Enter new name: ")
                Contacts.phone_book[new_name] = Contacts.phone_book.pop(old_name)
        if user_choice == 2:
            old_name = input("Enter name to edit: ")
            new_number, new_address = input("Enter new number and address: ").split()
            new_number = int(new_number)
            Contacts.phone_book[old_name] = [new_number, new_address]
            print()
        if user_choice == 3:
            pass
    except ValueError:
        print("Incorrect input")


def remove_contact():
    contact_to_delete = input("What contact would you like to delete? ")
    if contact_to_delete in Contacts.phone_book.keys():
        del Contacts.phone_book[contact_to_delete]
        print("Contact {} deleted\n".format(contact_to_delete))
    else:
        print("Contact not found\n")


def print_contacts():
    for x, y in Contacts.phone_book.items():
        print("Name: {}\nNumber: {}\nAddress: {}\n".format(x, y[0], y[1]))


def choice():
    try:
        print("1. Add Contact\n2. Edit Contact\n3. Remove Contact\n4. Print Phonebook\n5. Exit")
        user_choice = int(input())
        if user_choice == 1:
            add_contact()
        elif user_choice == 2:
            edit_contact()
        elif user_choice == 3:
            remove_contact()
        elif user_choice == 4:
            print_contacts()
        elif user_choice == 5:
            quit()
        else:
            print("Invalid choice\n")
    except ValueError:
        print("Invalid choice\n")


def main():
    while True:
        choice()


main()
