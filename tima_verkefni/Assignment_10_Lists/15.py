
def dot_product(vector1,vector2):
    totlal_sum = 0
    for i in range(len(vector1)):
        value = vector1[i] * vector2[i]
        totlal_sum += value
    return totlal_sum
def input_vector(size):
    base = []
    for i in range(size):
        element = float(input("Element no {}:".format(i+1)))
        base.append(element)
    return base

size = int(input("Input vector size: "))
vector1 = input_vector(size)
vector2 = input_vector(size)
print("Dot product is: ", dot_product(vector1, vector2))


