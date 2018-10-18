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
    print(chess_players_dict)
    return chess_players_dict


def main():
    # 1.get name of file from user
    file_name = get_input("enter name of file: ")
    # 2.get data from file
    file_content = open_file(file_name)
    print("file content:", file_content)
    if file_content:
        create_dict_from_file_data(file_content)
    # 3.create dictionary from csv data, key = name
    file_content.close()



main()
