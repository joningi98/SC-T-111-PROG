# this is a string
# alice,elise,hello

def to_list(the_string):
    if ',' in the_string:
        return the_string.split(',')
    if ' ' in the_string:
        return the_string.split()
    return [the_string]


the_string = input("Enter the string: ")
the_list = to_list(the_string)
print(the_list)