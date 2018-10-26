# highest mileage data
# from http : / /www. fueleconomy . gov /FEG/ download . shtml

def create_mileage_list(epa_file):
    """ Create a l i s t of ca rs and mileage from epa file . """
    mileage_list = []

    for line in epa_file:
        if line[0:5] == 'CLASS' or\
            'VAN' in line or\
            'PICKUP' in line:
            continue
        line_list = line.split(',')
        car_tuple = (int(line_list[9]), line_list[1], line_list[2])
        mileage_list.append(car_tuple)
    return mileage_list

###### FUNCTION TO FIND MIN AND MAX #########

def find_max_min_mileage(mileage_list, max_mileage, min_mileage):
    max_mileage_list = []
    min_mileage_list = []

    for car_tuple in mileage_list:
        if car_tuple[0] == max_mileage:
            max_mileage_list.append(car_tuple)
        if car_tuple[0] == min_mileage:
            min_mileage_list.append(car_tuple)
    return max_mileage_list, min_mileage_list

# Open EPA file
epa_file = open("epaData.cvs", "r")

for line in epa_file:
    if "FERRARI" in line:
        print(line[:75])

epa_file = open("epaData.csv", "rU")
mileage_list = create_mileage_list(epa_file)

max_mileage = max(mileage_list) [0]
min_mileage = min(mileage_list) [0]

print("Max and Min Mileage: ", max_mileage, min_mileage)
print() # print blank line

max_mileage_list, min_mileage_list = find_max_min_mileage(mileage_list, max_mileage, min_mileage)
print("Maximum Mileage Cars:")
for car_tuple in max_mileage_list:
    print(" ", car_tuple[1], car_tuple[2])
print("Minimum Mileage Cars: ")
for car_tuple in min_mileage_list:
    print(" ", car_tuple[1], car_tuple[2])