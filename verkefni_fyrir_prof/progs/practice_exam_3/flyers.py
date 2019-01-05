
def open_file(filename):
    try:
        flights = []
        with open(filename, "r") as file:
            for line in file.readlines():
                flights.append(line.strip().split())
        return flights
    except FileNotFoundError:
        print("File {} not found!".format(filename))


def make_dict(flights):
    flight_dict = {}
    for name, country in flights:
        if name in flight_dict.keys():
            if country in flight_dict[name]:
                pass
            else:
                flight_dict[name].append(country)
        else:
            flight_dict[name] = [country]
    return flight_dict


def count_trips(fly_dict):
    most_trips = 0
    frequent_flier = ''
    for name, trips in fly_dict.items():
        if len(trips) > most_trips:
            most_trips = len(trips)
            frequent_flier = name
    return most_trips, frequent_flier


def print_dict(fly_dict):
    for name, trips in fly_dict.items():
        print(name + ":")
        for trip in sorted(trips):
            print("\t", trip)


def main():
    file_name = "flights.txt"
    flights = open_file(file_name)
    flight_dict = make_dict(flights)
    number_trips, name = count_trips(flight_dict)
    print_dict(flight_dict)
    print("\n\n{} has been to {} countries".format(name, number_trips))


main()

