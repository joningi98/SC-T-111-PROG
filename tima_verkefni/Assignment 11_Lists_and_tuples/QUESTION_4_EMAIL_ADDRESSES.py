
def get_emails():
    email_list = []
    while True:
        email = input("Email address:")
        if email != "q":
            email_list.append(email)
        else:
            break
    return email_list

def get_names_and_domains(email_list):
    new_list = []
    for element in email_list:
        split_email = element.split('@')
        split_email = tuple(split_email)
        new_list.append(split_email)
    return new_list


# Main program starts here - DO NOT change it

email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)