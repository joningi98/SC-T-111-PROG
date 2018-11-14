def readNumbers():
    nums = [int(x) for x in input().split()]
    return nums


def sum_of_even(nums):
    even_list = []
    for x in nums:
        if x % 2 == 0:
            even_list.append(x)
    return even_list


def main():
    list_of_number = readNumbers()
    even_list = sum_of_even(list_of_number)
    print("Sum of even numbers: {}".format(sum(even_list)))


main()