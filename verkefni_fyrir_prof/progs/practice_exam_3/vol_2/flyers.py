def open_file(file_name):
    flights = []
    with open(file_name, "r") as file:
        for line in file.readlines():
            flights.append(line.split())
    return flights


def make_dict(flights):
    fly_dict = {}
    for name, country in flights:
        if name in fly_dict.keys() and country not in fly_dict[name]:
            fly_dict[name].append(country)
        else:
            fly_dict[name] = [country]
    return fly_dict


def count_trips(flights):
    most_trips = 0
    traveler = ""
    for name, trips in flights.items():
        if len(trips) > most_trips:
            most_trips = len(trips)
            traveler = name

    return most_trips, traveler


def main():
    file_name = "flights.txt"
    flights = open_file(file_name)
    fly_dict = make_dict(flights)
    trips, traveler = count_trips(fly_dict)
    for name, country in fly_dict.items():
        print("{}:".format(name))
        for x in country:
            print("\t\t{}".format(x))
    print("\n{} has been to {} countries".format(traveler, trips))


main()