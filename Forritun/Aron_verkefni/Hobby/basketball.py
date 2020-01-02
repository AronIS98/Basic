import random

TEAM_SIZE = 5
GAME_LENGTH = 48


class Team:
    def __init__(self, name):
        self.__name = name
        self.__team = []
        self.__points = 0
        for i in range(TEAM_SIZE):
            player = BasketballPlayer(i + 1)  # i+1 is the number for the player
            self.__team.append(player)

    def shoot_ball(self):
        shot = random.randin[1, 2]
        if shot % 2 == 0:
            self.__points += 2

    def play_offence(self):
        random_index = random.randint(0, TEAM_SIZE - 1)
        self.__points += self.__team[random_index].shoot_ball()

    def get_player_with_highest_score(self):
        highest_player = self.__team[0]
        for player in self.__team:
            if player > highest_player:
                highest_player = player
        return highest_player

    def get_name(self):
        return self.__name

    def get_points(self):
        return self.__points

    def __str__(self):
        the_str = ''
        for player in self.__team:
            the_str += str(player)
        return the_str


class BasketballPlayer:
    def __init__(self, number):
        self.number = number
        self.name = "Number: " + str(number)
        self.points = 0

    def shoot_ball(self):
        scored = random.randint(0, 1)
        self.points += scored * 2
        return (scored * 2)

    def __gt__(self, other):
        return (self.points > other.points)

    def __str__(self):
        return (self.name)


def print_winner(team_a, team_b):
    if team_a.get_points() > team_b.get_points():
        print(team_a.get_name() + " won!")
    elif team_a.get_points() < team_b.get_points():
        print(team_b.get_name() + " won!")
    else:
        print("Tie!")


def print_scores(team_a, team_b):
    print("")
    print(team_a.get_name() + " scored " + str(team_a.get_points()) + " points!")
    print(team_b.get_name() + " scored " + str(team_b.get_points()) + " points!")

    print("")
    print(team_a.get_name() + " scoring:")
    for player in team_a._Team__team:
        print(player.name + " Points: " + str(player.points))

    print("")
    print(team_b.get_name() + " scoring:")
    for player in team_b._Team__team:
        print(player.name + " Points: " + str(player.points))

    print("")
    print(team_a.get_name() + " highest scoring player:")
    highest = team_a.get_player_with_highest_score()

    print(highest.name + " Points: " + str(highest.points))

    print("")
    print(team_b.get_name() + " highest scoring player:")
    highest = team_b.get_player_with_highest_score()
    print(highest.name + " Points: " + str(highest.points))
    print("")


def play(team_a, team_b):
    for _ in range(GAME_LENGTH):
        team_a.play_offence()
        team_b.play_offence()


def random_seed():
    seed = int(input("Random seed: "))
    random.seed(seed)


def main():
    # You are not allowed to change this main function
    random_seed()
    chicago_bulls = Team("Chicago Bulls")
    la_lakers = Team("LA Lakers")

    play(chicago_bulls, la_lakers)
    print_winner(chicago_bulls, la_lakers)
    print_scores(chicago_bulls, la_lakers)


main()

