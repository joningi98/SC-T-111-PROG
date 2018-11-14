def get_list():
    size = int(input("How many numbers will be inn the list? "))
    try:
        nums = [int(x) for x in input().split()]
        if len(nums) > size:
            print("not the correct size idiot")
        return nums
    except ValueError:
        print("Enter only integers")


def find_smallest_value(nums):
    print("The smallest number is {}".format(min(nums)))


def main():
    nums = get_list()
    find_smallest_value(nums)


main()
