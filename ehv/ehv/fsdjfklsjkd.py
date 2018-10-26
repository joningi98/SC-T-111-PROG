the_sum = 0

for number in range(1, 101):
    the_sum = the_sum + number
print("Sum is:", the_sum)

import pylab

list_of_ints = []
for counter in range(10):
    list_of_ints.append(counter*2)

print(list_of_ints)
print(len(list_of_ints))

import math
import pylab

y_values = []
x_values = []
number = 0.0

while number < math.pi * 4:
    y_values.append(math.sin(number))
    x_values.append(number)
    number += 0.1
pylab.plot(x_values,y_values,'ro')
pylab.show()
