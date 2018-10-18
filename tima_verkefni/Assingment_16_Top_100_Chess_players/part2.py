RANK = 0
NAME = 1
COUNTRY = 2
POINTS = 3
BIRTH_YEAR = 4


def get_input(user_prompt):
    user_input = input(user_prompt)
    return user_input


def open_file(filename):
    try:
        file_content = open(filename, 'r')
        return file_content
    except FileNotFoundError:
        return None


def create_key(data):
    last_name, first_name = data.split(',')
    last_name = last_name.strip()
    first_name = first_name.strip()
    return "{} {}".format(first_name, last_name)


def clean_data(data_list):
    rank = int(data_list[RANK].strip())
    country = data_list[COUNTRY].strip()
    points = int(data_list[POINTS].strip())
    birth_year = int(data_list[BIRTH_YEAR].strip())
    return [rank, country, points, birth_year]


def create_dict_from_file_data(file_content):
    chess_players_dict = {}
    for data in file_content:
        data = (data.split(';'))
        key = create_key(data[NAME])
        chess_players_dict[key] = clean_data(data)
    return chess_players_dict


def get_points_per_birth_year(chess_players_dict):
    my_dict = {}
    for chess_players_dict in chess_players_dict.items():
        birth_year = chess_players_dict[1][3]
        if birth_year in my_dict:
            my_dict[birth_year][0] += 1
            my_dict[birth_year][1] += chess_players_dict[1][2]
        else:
            data = [1, chess_players_dict[1][2]]
            my_dict[birth_year] = data
    return my_dict


def get_points_per_country(chess_players_dict):
    country_dict = {}
    for chess_players_dict in chess_players_dict.items():
        country = chess_players_dict[1][1]
        if country in country_dict:
            country_dict[country][0] += 1
            country_dict[country][1] += chess_players_dict[1][2]
        else:
            data = [1, chess_players_dict[1][2]]
            country_dict[country] = data
    return country_dict


def print_header(header_srt):
    print(header_srt)
    print("-" * len(header_srt))


def print_results(chess_players_dict, birth_year_dict):
    print(birth_year_dict)
    for birth_year in sorted(birth_year_dict.keys()):
        number_of_players = birth_year_dict[birth_year][0]
        total_points = birth_year_dict[birth_year][1]
        average = total_points / number_of_players
        print("{} ({}) ({:.1f}):".format(birth_year, number_of_players, average))
        for player in chess_players_dict.keys():
            if chess_players_dict[player][3] == birth_year:
                print("{:>40} {:>10}".format(player, chess_players_dict[player][2]))


def print_tes1(chess_players_dict, countries_dict):
    for country in sorted(countries_dict.keys()):
        number_of_players = countries_dict[country][0]
        total_points = countries_dict[country][1]
        average = total_points / number_of_players
        print("{} ({}) ({:.1f}):".format(country, number_of_players, average))
        for player in chess_players_dict.keys():
            if chess_players_dict[player][1] == country:
                print("{:>40} {:>10}".format(player, chess_players_dict[player][2]))


def main():
    # 1.get name of file from user
    file_name = get_input("Enter filename: ")
    # 2.get data from file
    file_content = open_file(file_name)
    if file_content:
        # 3.create dictionary from csv data, key = name
        chess_players_dict = create_dict_from_file_data(file_content)
        file_content.close()
        # 4. calculate average for each country
        birth_year_dict = get_points_per_birth_year(chess_players_dict)
        countries_dict = get_points_per_country(chess_players_dict)
        # 5. calculate numbers of each players for each country
        # 6. print results
        print_header("Players by country:")
        print_tes1(chess_players_dict, countries_dict)
        print_header("Players by birth year:")
        print_results(chess_players_dict, birth_year_dict)


main()
