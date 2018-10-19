


def mutate_list(a_list, index_num, v):
    ''' Inserts v at index index_num in a_list'''
    a_list.insert(index_num, v)
    
def remove_ch(a_list, index_num):
    ''' Removes character at index_num from a_list'''
    a_list.pop(index_num)
    
def get_list():
    ''' Reads in values for a list and returns the list '''
    user_list = input("Enter values in list separated by commas: ")
    user_list = user_list.split(",")
    user_list = [int(i) for i in user_list]
    return user_list



user_list = get_list()
print(user_list)
m_or_r = input("Enter choice (m,r): ")
if m_or_r == 'm':
    user_pick = input('')
    index_num, v = user_pick.split(",")
    index_num = int(index_num)
    v = int(v)
    mutate_list(user_list, index_num, v)
    print(user_list)
elif m_or_r == 'r':
    index_num = int(input(''))
    remove_ch(user_list, index_num)
    print(user_list)
else:
    print(user_list)


