my_dict = {'a': 2, 3: ['x', 'y'], 'Joe': 'Smith'}
print(my_dict)
print(my_dict['a'])  # Use square brackets to index
print('a' in my_dict)
print(2 in my_dict)
print(len(my_dict))  # Number of key : value pairs

for key in my_dict:  # Membership of keys
    print(key)

for key in my_dict:  # Print key and value
    print(key, my_dict[key])

# items(): all the key-value pairs as a list of tuples
# keys(): all the keys as a list
# values(): all the values as a list

for key, val in my_dict.items():
    print('Key: {:<7}, Value:{}'.format(key, val))

for key in my_dict.keys():
    print(key)

dict_value_view = my_dict.values()
print(dict_value_view)
print(type(dict_value_view))
for val in dict_value_view:
    print(val)

my_dict['new_kay'] = 'new_value'        # Add new value to the dictionary
print(dict_value_view)
dict_key_view = my_dict.keys()
print(dict_key_view)
print(dict_value_view)

############## COPY ##############

new_dict = my_dict.copy()
new_dict['a'] = 'new_value'
print(my_dict)
print(new_dict)
a_value = new_dict[3]
print(a_value)
a_value[0] = 'new_element'
print(new_dict)
print(my_dict)
