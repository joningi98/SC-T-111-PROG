nums_of_trips = int(input())

cities = []

for x in range(nums_of_trips):
    num_of_cities = int(input())
    cities = []
    for y in range(num_of_cities):
        city_name = input()
        cities.append(city_name)
    print(len(set(cities)))



