# 2.
# DIM = 4 # dimension of the board DIMxDIM
# EMPTYSLOT = 0
# QUIT = 0

# def initialize_board():
#     ''' Creates the initial board according to the user input.
#     The board is a list of lists.
#     The list contains DIM elements (rows), each of which contains DIM elements (columns)'''
#     numbers = input().split()
#     numbers = [int(number) for number in numbers]
#     puzzle_board = []
#     index = 0
#     for _ in range(DIM):
#         row = numbers[index:index + DIM]
#         index += DIM
#         puzzle_board.append(row)

#     return puzzle_board
    

# def display(puzzle_board):
#     ''' Display the board, printing it one row in each line '''
#     print()
#     for i in range(DIM):
#         for j in range(DIM):
#             if puzzle_board[i][j] == EMPTYSLOT:
#                 print("\t", end="")
#             else:
#                 print(str(puzzle_board[i][j]) + "\t", end="")
#         print()
#     print()

# def order(nested_list):
#     order = int(input())
#     #Dictates when to stop
#     if order == 0:
#         return False
#     else:
#         return order

# def find_index(order,grid):
#     for y_axis in range(DIM):
#         for x_axis in range(DIM):
#             if grid[y_axis][x_axis] == order:
#                 return (y_axis,x_axis)
#     return None

# def move(empty_index,number_index,grid,order):
#     grid[empty_index[0]][empty_index[1]] = order
#     grid[number_index[0]][number_index[1]] = 0
#     return grid
    
# def main():
#     command = True
#     board = initialize_board()
#     while  command != False:
#         display(board)
#         command = order(board)
#         empty_index = find_index(EMPTYSLOT,board)
#         number_index = find_index(command,board)
#         if number_index != None:
#             board = move(empty_index,number_index,board,command)
# main()

#-------------------------------------------------------    question 3  -------------------------------
#3.
class StringSet:
    def __init__(self,other):
        temp = other.split()
        self.__words = []
        for each in temp:
            if each not in self.__words:
                self.__words.append(each)

    def size(self):
        self.__words
        return len(self.__words)
    
    def __str__(self):
        answer = ""
        for words in self.__words:
            answer += words + " "
        answer = answer.strip()
        return answer
        
    def __add__(self,other):
        temp = str(other)
        temp = temp.split()
        for words in temp:
            if words not in self.__words:
                self.__words.append(words)
        return self

    def at(self,other):
        return self.__words[other]
        
    def find(self,other):
        if other in self.__words:
            return True
        else:
            return False







#Testcode:
def main():
    str1 = 'chocolate ice cream and chocolate candy ice bars are my favorite'
    set1 = StringSet(str1)
    str2 = 'I like to eat broccoli and fish and ice cream and brussel fish sprouts'
    set2 = StringSet(str2)
    print("Set1:", set1)
    print("Set2:", set2)
    print("Set1 size:", set1.size())
    print("Set2 size:", set2.size())
    the_union = set1 + set2
    print("Union:", the_union)
    print("Union size:", the_union.size())

    query = StringSet('chocolate cream fish good rubbish')
    print("Query:", query)
    count = 0
    for i in range(query.size()):
        if the_union.find(query.at(i)):
            count += 1
    
    print("Query size:", query.size())
    print("Found in union:", count)

main()