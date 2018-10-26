##### FORMAT STIRNG, ELEMENT, TYPE #####

for element in ['abc', 12, 3.14159, True]:
    print("{:<7} which is type {}".format(element, type(element)))


##### REVERSE A STRING ANG JOIN ######

my_str = 'This is a test'
string_elements = my_str.split()  # list of words
print(string_elements)
reversed_elements = []

for element in string_elements:    # fo r each word
    reversed_elements.append(element[::-1])   # reverse , append

print(reversed_elements)
new_str = ' '.join(reversed_elements)

print(new_str)


######### LIST THING ? #########

my_list = [1.6, 2.7, 3.8, 4.9]
new_list = []
a_list = []
for val in my_list:
    temp = str(val)
    a_list.append(temp.split('.'))

for val in a_list:
    new_list.append(int(val[0]))
    my_str = ':'.join(val)
    
print(my_list) # Line 1
print(a_list) # Line 2
print(new_list) # Line 3
print(val) # Line 4
print(my_str) # Line 5


##########