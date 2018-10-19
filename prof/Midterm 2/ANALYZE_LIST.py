
def the_list():
    try:
        my_list = [int(x) for x in input("Enter integers separated with commas:").split(',')]
        return my_list
    except ValueError:
        print(" Incorrect input!")


def sort_list(my_list):
    sorted_list = my_list[:]
    sorted_list.sort()
    return sorted_list


def average_list(the_list):
    average_of_my_list = float(sum(the_list)) / float(len(the_list))
    average_of_my_list = ("%.2f" % average_of_my_list)
    return average_of_my_list


def is_prime(n):
    """Returns True if the given positive number is prime and False otherwise"""
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


def prime_list(sorted_list):
    prime_list = []
    unique_prime_list = []
    for num in sorted_list:
        if is_prime(num):
            prime_list.append(num)

    for num in prime_list:
        if num not in unique_prime_list:
            unique_prime_list.append(num)
    return unique_prime_list


def results():
    print(" Input list:", my_list)
    print("Sorted list: ", sorted_list)
    print("Prime list: ", primed_list)
    print('Min:', str(min(my_list)) + ',', "Max:", str(max(my_list)) + ',', "Average:", average_list)


my_list = the_list()
sorted_list = sort_list(my_list)
average_list = average_list(my_list)
primed_list = prime_list(sorted_list)

results()
