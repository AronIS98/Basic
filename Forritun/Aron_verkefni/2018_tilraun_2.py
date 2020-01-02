# #file name =  flights.txt
# def open_file(file_name):
#     try:
#         the_file = open(file_name,"r")
#         return the_file
#     except FileNotFoundError:
#         return None

# def file_to_list(a_file):
#     file_list = []
#     for lines in a_file:
#         file_list.append(lines)
#     return file_list


# def organize(nested_list):
#     name_list =  []
#     a_dict = {}

#     for lines in nested_list:
#         name , country = lines.split()

#         if name not in a_dict:
#             a_dict.update({name : [country]})
#             name_list.append(name)
#         if name in a_dict:
#             if country not in a_dict[name]:
#                 a_dict[name].append(country)
#     return name_list , a_dict



# def print_list(name_list,a_dict):
#     name_list.sort()
#     for names in name_list:
#         print("{}:".format(names))
#         a_dict[names].sort()
#         for countries in a_dict[names]:
#             print("\t{}".format(countries))


# def main():
#     file_to_open = "flights.txt"
#     a_file = open_file(file_to_open)
#     if a_file != None:
#         the_list = file_to_list(a_file)
#         names, the_dict = organize(the_list)
#         print_list(names,the_dict)
#     a_file.close

# main()

#2.

# Constants to be used in the implementation
# DIM = 5
# POSITION = 'o'
# EMPTY = 'x'
# LEFT = 'l'
# RIGHT = 'r'
# UP = 'u'
# DOWN = 'd'
# QUIT = 'q'

# def get_move():
#     ''' Returns a move corresponding to the user input direction '''
#     move = input('Move: ')
    
#     if move not in [LEFT, RIGHT, UP, DOWN]:
#         return QUIT
#     else:
#         return move

# def initialize_grid():
#     ''' Returns an initialized grid for the given dimension '''
#     grid = []

#     for i in range(DIM):
#         sublist = []
#         for j in range(DIM):
#             sublist.append(EMPTY)
#         grid.append(sublist)

#     grid[0][0] = POSITION  # Current position
#     return grid

# def print_grid(grid):
#     for lines in grid:
#         for items in lines:
#             print(items,end =" ")
#         print("")
#     print("")

# def find_position(grid):
#     for y in range (DIM):
#         for x in range(DIM):
#             if grid[y][x] == POSITION:
#                 return (y,x)

# def is_outside(move,pos,grid):
#     Y = pos[0]
#     X = pos[1]
#     unchanged = True
#     if X > 3 and move == RIGHT:
#         X -= 4
#         unchanged = False
#     if X < 1 and move == LEFT:
#         X += 4
#         unchanged = False
#     if Y < 1 and move == UP:
#         Y += 4
#         unchanged = False
#     if Y > 3 and move == DOWN:
#         Y -= 4
#         unchanged = False
    
#     grid[pos[0]][pos[1]] = EMPTY
#     grid[Y][X] = POSITION

#     return grid,unchanged


# def change_position(move,grid,pos):
#     y_axis = pos[0]
#     x_axis = pos[1]
#     grid[y_axis][x_axis] = EMPTY
#     if move == UP:
#         grid[y_axis-1][x_axis] = POSITION
#     elif move == DOWN:
#         grid[y_axis+1][x_axis] = POSITION
#     elif move == LEFT:
#         grid[y_axis][x_axis-1] = POSITION
#     elif move == RIGHT:
#         grid[y_axis][x_axis+1] = POSITION
#     return grid
    

# def main():
#     move = ""
#     grid = initialize_grid()
#     print_grid(grid)
#     while move != QUIT:
#         current_pos = find_position(grid)
#         move = get_move()
#         if move != QUIT:
#             grid , unchanged = is_outside(move,current_pos,grid)
#             if unchanged:
#                 grid = change_position(move,grid,current_pos)
#             print_grid(grid)

# main()

# # 3.
# import random

# TEAM_SIZE = 5
# GAME_LENGTH = 48

# class Team:
#     def __init__(self, name):
#         self.__name = name
#         self.__team = []
#         self.points = 0
#         for i in range(TEAM_SIZE):
#             player = BasketballPlayer(i+1) # i+1 is the number for the player
#             self.__team.append(player)
            
#     def play_offence(self):
#         random_index = random.randint(0, TEAM_SIZE-1)
#         self.points += self.__team[random_index].shoot_ball()

#     def get_player_with_highest_score(self):
#         highest_player = self.__team[0]
#         for player in self.__team:
#             if player > highest_player:
#                 highest_player = player
#         return highest_player

#     def get_name(self):
#         return self.__name

#     def get_points(self):
#         return self.points

#     def __str__(self):
#         the_str = ''
#         for player in self.__team:
#             the_str += str(player)
#         return the_str


# class BasketballPlayer:
#     def __init__(self,other):
#         self.__number = other
#         self.points = 0
#         self.name = "Number: {}".format(str(self.__number))

#     def shoot_ball(self):
#         scored = random.randint(0,1)
#         self.points += scored*2
#         return (scored*2)

#     def __gt__(self,other):
#         return(self.points > other.points)

#     def __str__(self):
#         return self.name
    

    

# def print_winner(team_a, team_b):
#     if team_a.get_points() > team_b.get_points(): 
#       print (team_a.get_name() + " won!")
#     elif team_a.get_points() < team_b.get_points():
#       print (team_b.get_name() + " won!")   
#     else: 
#       print ("Tie!")

# def print_scores(team_a, team_b):
#     print ("")
#     print (team_a.get_name() + " scored " +str(team_a.get_points() )+" points!"  )
#     print (team_b.get_name() + " scored " +str(team_b.get_points() )+" points!"  )

#     print ("")
#     print (team_a.get_name() +" scoring:")
#     for player in team_a._Team__team:
#         print (player.name + " Points: "+str(player.points))

#     print ("")
#     print (team_b.get_name() +" scoring:")
#     for player in team_b._Team__team:
#         print (player.name + " Points: "+str(player.points))
   
#     print ("")
#     print (team_a.get_name() +" highest scoring player:")
#     highest = team_a.get_player_with_highest_score()
 
#     print (highest.name + " Points: "+str(highest.points) )

#     print ("")
#     print (team_b.get_name() +" highest scoring player:")
#     highest = team_b.get_player_with_highest_score()
#     print (highest.name + " Points: "+str(highest.points) )
#     print ("")


# def play(team_a, team_b):
#     for _ in range(GAME_LENGTH):
#         team_a.play_offence()    
#         team_b.play_offence()
        
# def random_seed():
#     seed = int(input("Random seed: "))
#     random.seed(seed)

# def main():
#     # You are not allowed to change this main function
#     random_seed()
#     chicago_bulls = Team("Chicago Bulls")
#     la_lakers = Team("LA Lakers")

#     play(chicago_bulls, la_lakers)
#     print_winner(chicago_bulls, la_lakers)
#     print_scores(chicago_bulls, la_lakers)

# main()





import random
# Constants to be used in the implementation
WORD_LIST = [
"lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
 "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"]
MAX_GUESS = 12
CHAR_PLACEHOLDER = '-'

def random_seed():
    seed = int(input("Random seed: "))
    random.seed(seed)

# Main program starts here
def choose_word(list_of_words):
	word = random.choice(list_of_words)
	return word
def word_to_list(word):
    word_in_list = [letter for letter in word]
    return word_in_list

def guess(used_letters,word_as_a_list,correct_guesses):
    guess = input("Choose a letter: ")
    if guess not in used_letters:
        used_letters.append(guess)

        if guess in word_as_a_list:
            print("You guessed correctly!")
            correct_guesses.append(guess)
        else:
            print("The letter is not in the word!!")
            
    else:
        print("You have already guessed that letter!")

    return used_letters,word_as_a_list,correct_guesses

def word_progress(correct_guesses,word_as_a_list):
    to_print = ""
    for letters in word_as_a_list:
        if letters in correct_guesses:
            to_print += letters + " "
        else:
            to_print += CHAR_PLACEHOLDER + " "
    to_print.strip()
    return to_print

def has_won(to_print):
    check = [letters for letters in to_print]
    if CHAR_PLACEHOLDER not in check:
        return True
    else:
        return False

	
def main():
    random_seed()
    used_letters = []
    correct_guesses = []
    word = choose_word(WORD_LIST)
    word_as_a_list = word_to_list(word)
    print("The word you need to guess has {} characters".format(len(word_as_a_list)))
    turn = 1
    victory = False
    while turn < MAX_GUESS  and victory == False:
        used_letters,word_as_a_list,correct_guesses = guess(used_letters,word_as_a_list,correct_guesses)
        turn += 1
        to_print = word_progress(correct_guesses,word_as_a_list)
        print("You are on guess {}/12".format(turn))
        print(to_print)
        victory = has_won(to_print)

    if victory == False:
        print("You lost! The secret word was {}".format(word))
    elif victory:
        print("You won!")
        print("Word to guess: {}".format(to_print))

main()