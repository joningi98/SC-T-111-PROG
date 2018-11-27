def open_file():
    try:
        file_list = []
        with open("flights.txt", 'r') as file:
            for line in file.readlines():
                stripped_line = line.rstrip().split()
                file_list.append(stripped_line)
        return file_list
    except FileNotFoundError:
        print("File not found")


def name_list(flight_list):
    travel_dict = {}
    for name, country in flight_list:
        print(name)
        print(country)
        if name in travel_dict.keys() and country not in travel_dict.values():
            travel_dict[name] += " " + country
        else:
            travel_dict[name] = country
    return travel_dict


def count_trips(travels_dict):
    most_trips = ''
    traveler = ''
    for x in travels_dict.items():
        if x.values.split() > most_trips:
            most_trips = x.values
            traveler = x.keys()
    print(most_trips)


def main():
    flight_list = open_file()
    travel_dict = name_list(flight_list)
    count_trips(travel_dict)

main()



