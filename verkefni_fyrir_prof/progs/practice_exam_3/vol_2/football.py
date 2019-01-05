"""
Í þessu verkefni eigið þið að útfæra klasann FootballPlayer og tvö föll utan klasans þannig að hin gefna beinagrind keyri rétt.
Klasinn á sér tvær tilvikabreytur (attributes): number (númer leikmanns) og points (skoruð stig).

Í klasanum eru fjögur föll (methods).  Hér er aðeins lýsing fyrir eitt þeirra:

shoot_ball(): Þetta fall velur af handahófi hvort leikmaðurinn hitti eða hitti ekki í markið í skottilraun (1/30 líkur).
Notið random.randint() til að ákvarða hvort leikmaður hitti eða hitti ekki.  Ef leikmaður hittir þá bætir hann við sig einu stigi, annars 0.
Fallið skilar viðbættum stigum.


Athugið:

Klasinn Team er gefinn - þið þurfið EKKI að útfæra neina aukavirkni í honum.
randint(a,b): Býr til heiltölu N af handahófi á bilinu a <= N <= b.


Hvernig útkoman á að vera:

KR won!

Fjölnir scored 0 points!
KR scored 1 points!

Fjölnir scoring:
None
KR scoring:
Number: 4 Points: 1

Fjölnir highest scoring player:
None
KR highest scoring player:
Number: 4 Points: 1

"""


import random

TEAM_SIZE = 11
GAME_LENGTH = 90


class Team:
    def __init__(self, name):
        self.__name = name
        self.__team = []
        self.__points = 0
        for i in range(TEAM_SIZE):
            player = FootballPlayer(i + 1)  # i+1 is the number for the player
            self.__team.append(player)

    def play_offence(self):
        random_index = random.randint(0, TEAM_SIZE - 1)
        self.__points += self.__team[random_index].shoot_ball()

    def get_player_with_highest_score(self):
        if self.__points == 0:
            return "None"
        highest_player = self.__team[0]
        for player in self.__team:
            if player > highest_player:
                highest_player = player
        return highest_player

    def get_team(self):
        return self.__team

    def get_name(self):
        return self.__name

    def get_points(self):
        return self.__points

    def __str__(self):
        the_str = ''
        if self.__points == 0:
            return "None"
        for player in self.__team:
            if player.points != 0:
                the_str += str(player)
        return the_str


class FootballPlayer:
    def __init__(self, number=0):
        self.__number = number
        self.points = 0

    def shoot_ball(self):
        goal = random.randint(1, 50)
        if goal == 1:
            self.points += 1
            return 1
        else:
            return 0

    def __gt__(self, other):
        if self.points > other.points:
            return True
        if self.points < other.points:
            return False

    def __str__(self):
        return str(self.__number)

    def get_number(self):
        return self.__number


def print_winner(team_a, team_b):
    ''' You need to implement this function. Print out:
        which team won (if tie, print "Tie!")
    '''
    team_a_goals = team_a.get_points()
    team_b_goals = team_b.get_points()
    if team_a_goals > team_b_goals:
        print("{} wins!\n".format(team_a.get_name()))
    if team_a_goals < team_b_goals:
        print("{} wins!\n".format(team_b.get_name()))
    if team_a_goals == team_b_goals:
        print("Tie!\n")


def print_scores(team_a, team_b):
    """ You need to implement this function.  Print out:
        how many points each team scored
        the scoring of each player in each team
        the highest scoring player in each team
    """

    print("{} scored {} points!".format(team_a.get_name(), team_a.get_points()))
    print("{} scored {} points!\n".format(team_b.get_name(), team_b.get_points()))

    team_scoring(team_a, team_b)
    highest_scoring_player(team_a, team_b)


def team_scoring(team_a, team_b):
    team_a_strikers = []
    for player in team_a.get_team():
        if player.points != 0:
            team_a_strikers.append(player)

    print("{} scoring:".format(team_a.get_name()))
    for man in team_a_strikers:
        print("Number: {} Points: {}".format(man.get_number(), man.points))

    team_a_strikers = []
    for player in team_b.get_team():
        if player.points != 0:
            team_a_strikers.append(player)

    print("{} scoring:".format(team_b.get_name()))
    for man in team_a_strikers:
        print("Number: {} Points: {}".format(man.get_number(), man.points))


def highest_scoring_player(team_a, team_b):
    print("\n{} highest scoring player:".format(team_a.get_name()))
    if team_a.get_points() == 0:
        print("None")
    else:
        print("Number: {} points: {}".format(team_a.get_player_with_highest_score(), team_a.get_player_with_highest_score().points))
    print("{} highest scoring player:".format(team_b.get_name()))
    if team_b.get_points() == 0:
        print("None")
    else:
        print("Number: {} points: {}".format(team_b.get_player_with_highest_score(), team_b.get_player_with_highest_score().points))


def play(team_a, team_b):
    for _ in range(GAME_LENGTH):
        team_a.play_offence()
        team_b.play_offence()


def random_seed():
    random.seed(input())


def main():
    # You are not allowed to change this main function
    random_seed()
    team1 = Team("Fjölnir")
    team2 = Team("KR")

    play(team1, team2)
    print_winner(team1, team2)
    print_scores(team1, team2)


main()