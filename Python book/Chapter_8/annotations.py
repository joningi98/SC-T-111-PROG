def my_func(param1 : int, param2 : float) -> None :
    print('Result is :', param1 + param2)
    my_func.__annotations__




print(my_func(1, 2.0))
print(my_func('a', 'b'))