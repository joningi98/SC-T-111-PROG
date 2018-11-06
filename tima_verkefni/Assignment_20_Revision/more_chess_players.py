class ChessPlayers(object):
    def __init__(self, name='', birth=0, chess_rating=0):
        self.name = name
        self.birth_year = birth
        self.chess_rating = chess_rating

    def __str__(self):
        return "Name: {}\nYear: {}\n Rating: {}".format(self.name, self.birth_year, self.chess_rating)


def get_highest_rated_player(players):
    highest_num = 0
    highest_player = ''
    for x in players:
        for key, value in x.items():
            if value[1] > highest_num:
                highest_num = value[1]
                highest_player = key, value
    return "Name: {}\nYear: {}\nRating: {}".format(highest_player[0], highest_player[1][0], highest_num)


def get_average_rating(players):
    rating_list = []
    for x in players:
        for value in x.items():
            rating_list.append(value[1][1])
    return sum(rating_list) / len(rating_list)


def main():
    number_of_players = int(input("Number of players: "))
    players = []

    print("--- Reading players ---")
    # here you should get info from the user about
    # number_of_players many chess player
    # code goes here....
    chess_dict = {}
    for x in range(number_of_players):
        ChessPlayers.name = input("Enter Name: ")
        ChessPlayers.birth_year = int(input("Enter Year: "))
        ChessPlayers.chess_rating = int(input("Enter Rating: "))
        print("")
        chess_dict[ChessPlayers.name] = (ChessPlayers.birth_year, ChessPlayers.chess_rating)
    players.append(chess_dict)

    print("--- Displaying players --- ")
    for key, value in chess_dict.items():
        print("Name: {}".format(key))
        print("Year: {}".format(value[0]))
        print("Rating: {}".format(value[1]))
        print("")
    # here you should print each player
    # code goes here....

    highest_rated_player = get_highest_rated_player(players)
    print("Highest rated player: ")
    print(highest_rated_player)

    average_rating = get_average_rating(players)
    print("Average rating:", "%.2f" % average_rating)


main()