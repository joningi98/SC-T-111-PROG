class IntList(list):
    def __init__(self, size=0):
        super().__init__()
        self.size = size

    def add(self, num):
        if self.full():
            self.append(num)

    def full(self):
        if len(self) < self.size:
            return True

    def __add__(self, other):
        if self.size > other.size:
            new_list = IntList(other.size)
        if self.size < other.size:
            new_list = IntList(self.size)
        new_list = [x + y for x, y in zip(self, other)]
        return new_list


# Main program starts here
list1 = IntList(5) 	# Constructs an IntList that can hold 5 integers
list2 = IntList(12) 	# Constructs an IntList that can hold 12 integers

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