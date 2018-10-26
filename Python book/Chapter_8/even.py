
def evens(n):
    evens_list = []
    for i in range(1,n+1):
        evens_list.append(2*i)
    return evens_list

# or

def evens2(n):
    return [2*i for i in range(1, n+1)]

print(evens(5))
print(evens2(5))

#######################################

def mirror(pair):
    return pair[1], pair[0] 

first, second = mirror((2,3))

mirror((2,3))

print(first)
print(second)
print(first,second)

a_tuple = mirror((2,3))
print(a_tuple)

########################################

def func1(param_required, param_default = 2):
    print(param_required, param_default)

print(func1(5,6))
print(func1(5))
