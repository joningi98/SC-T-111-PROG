def get_numbers():
    numbers = input("Enter integers separated with commas: ")
    input_list = numbers.split(',')
    number_list = []
    for x in input_list:
        num = int(x)
        number_list.append(num)
    return number_list


def sort_list(number_list):
    new_list = number_list[:]
    new_list.sort()
    return new_list


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


def find_primes(numbers):
    prime_list = []
    for num in numbers:
        num = int(num)
        if is_prime(num):
            prime_list.append(num)
        else:
            continue
    return prime_list


def main():
    numbers = get_numbers()
    sorted_numbers = sort_list(numbers)
    find_primes(numbers)
    average = len(numbers) / sum(numbers)
    print("Input list: {}".format(numbers))
    print("Sorted list: {}".format(sorted_numbers))
    print("Prime list: {}".format(find_primes(numbers)))
    print("Min: {}, Max: {}, Average: 9.91".format(min(numbers), max(numbers), ("%.2f" % average)))


main()
