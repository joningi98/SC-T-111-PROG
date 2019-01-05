class IntList(list):
    def __init__(self, size=0):
        super().__init__()
        self.__size = size

    def add(self, other):
        if not self.full():
            self.append(other)

    def __len__(self):
        count = 0
        for x in self:
            count += 1
        return count

    def full(self):
        if len(self) == self.__size:
            return True
        else:
            return False

    def __add__(self, other):
        if self.__size > other.__size:
            new_list = IntList(other.__size)
        if self.__size < other.__size:
            new_list = IntList(self.__size)

        new_list = [x + y for x, y in zip(self, other)]

        return new_list


# Main program starts here
list1 = IntList(5)  # Constructs an IntList that can hold 5 integers
list2 = IntList(12)  # Constructs and IntList that can hold 12 integers

for i in range(10):
    list1.add(i)
    list2.add(i)

print(list1)
print(list2)

print("Length of list1 is: {}".format(len(list1)))
print("Length of list2 is: {}".format(len(list2)))

if list1.full():
    print("list1 is full")
if list2.full():
    print("list2 is full")

list3 = list1 + list2
print(list3)

list4 = list2 + list1
print(list4)