RANK = 0
COUNTRY = 1
RATING = 2
BYEAR = 3
NUM_ATTRIBUTES = 4

def open_file(file_name):
    try:
        file_stream = open(file_name,"r")
        return file_stream
    except FileNotFoundError:
        return None

def create_players_dict(file_stream):
    the_dict = {}
    for line in file_stream:
        rank,name, country, rating, bday = line.strip().split(";")
        last_name,first_name = name.split(", ")
        first_name.rstrip()

        key = "{}{}".format(first_name,last_name)
        the_dict[key] = (int(rank), country.strip(), int(rating), int(bday))
    return the_dict


def create_countries_dict(dict_players):
    country_dict = {}
    for a_tuple in dict_players.items():
        chess_player = a_tuple[0]
        # The data is a list
        chess_player_data = a_tuple[1]
        country = chess_player_data[COUNTRY]
        if country in country_dict:
            name_list = country_dict[country]
            name_list.append(chess_player)
        else:
            name_list = [chess_player]
            country_dict[country] = name_list

    return country_dict

def get_average_rating(players, dict_players):
    ratings = [ dict_players[player][RATING] for player in players]
    average = sum(ratings)/len(ratings)
    return average

def print_sorted(the_dict, dict_players):
    ''' Prints information sorted on the key of the_dict '''
    sorted_dict = sorted(the_dict.items())
    for key, players in sorted_dict:
        average_rating = get_average_rating(players, dict_players)
        print("{} ({}) ({:.1f}):".format(key, len(players), average_rating))
        for player in players:
            rating = dict_players[player][RATING]
            print("{:>41}{:>10d}".format(player, rating))

def print_header(title):
    print(title)
    dashes = '-' * len(title)
    print(dashes)

def main():
    print_header("Players by country")
    file_name = input("Enter filename: ")
    file_stream = open_file(file_name)
    if file_stream:
        dict_players = create_players_dict(file_stream)
        dict_countries = create_countries_dict(dict_players)
        print_sorted(dict_countries,dict_players)
    file_stream.close

main()