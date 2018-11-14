
def get_numbers():
    nums = [int(x) for x in input().split()]
    return nums


def get_lowest_number(nums):
    lowest_number = nums[0]
    for x in nums:
        if x < lowest_number:
            lowest_number = x
    return lowest_number


def main():
    nums = get_numbers()
    print(get_lowest_number(nums))


main()