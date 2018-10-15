
############### Contacts #############

contacts = {'Bill': '353-1234', 'Rich': '269-1234', 'Jane': ' 352-1234'}
print(contacts)  # Print all contacts
print(contacts['Bill'])  # Print a specific info about a contact
contacts['Barb'] = '271-1234'  # Add a contact
print(contacts)  # Print updated contacts

############### DEMO ################

demo = {2: ['a', 'b', 'c'], (2, 4): 27, 'x': {1: 2.5, 'a': 3}}
print(demo)
print(demo[2])  # Different types of key words
print(demo[(2, 4)])
print(demo['x'])
print(demo['x'][1])  # Prints value of key word '1'

# [ ]: indexing using the key as the index value
# len(): the “length” is the number of key-value pairs in the dictionary
# in: Boolean test of membership; is the key in the dictionary (not the value)?
# for: iteration through keys in the dictionary


