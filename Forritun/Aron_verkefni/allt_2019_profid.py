def get_input():
    """gets the input from the user"""
    user_input = input("Enter an ISBN: ")
    return user_input
    
def input_to_list(the_input):
    word_as_list = [item for item in the_input]
    return word_as_list

def is_valid(input_as_list,LENGTH_OF_ISBN,PLACEHOLDER_POSITION):
        if len(input_as_list) == LENGTH_OF_ISBN:#checks desired length
            for index in PLACEHOLDER_POSITION:
                if input_as_list[index] != "-":#checks if the placeholde ("-") is at the right place
                    return False
            for number in range(LENGTH_OF_ISBN-1):
                #Checks if the numbers are at the right places
                if number not in PLACEHOLDER_POSITION:
                    try:
                        int(input_as_list[number])
                    except ValueError:
                        return False
                    return True
        return False
                        
def main():
    LENGTH_OF_ISBN = 13 #A constant to change the desired length of ISBN with ease
    PLACEHOLDER_POSITION = [1,5,11] #List to change the positions of placeholders with ease.
    QUIT = "q"
    valid = False
    user_input = ""
    """the main function"""
    while user_input != QUIT:
        user_input = get_input()
        word_as_list = input_to_list(user_input)
        valid = is_valid(word_as_list,LENGTH_OF_ISBN,PLACEHOLDER_POSITION)
        if valid:
            print("Valid format!")
        elif user_input != QUIT:
            print("Invalid format!")



#The main function is executed.
main()

def open_file(filename):
    ''' Returns a file stream if filename found, otherwise None '''
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return None


def get_winning_numbers(NUMBERS_IN_LOTTO_ROW, HIGHEST_VALID_NUMBER):
    """askes for the winning numbers and makes sure they are valid."""
    winning_numbers = input("Enter winning numbers: ")
    test_list = winning_numbers.split()
    if len(test_list) != NUMBERS_IN_LOTTO_ROW:
        return False
    for numbs in test_list:
        try:
            numbs = int(numbs)
            
        except ValueError:
            return False
        if numbs > HIGHEST_VALID_NUMBER or numbs < 1:
            return False
    
    return test_list


def check_if_won(the_file_list,the_winning_numbers_list):
    """Checks if each line has winning numbers and adds a star next to winning numbers"""
    answer = []
    for lines in the_file_list:
        current_line_answer = ""
        lotto_numbers = lines.split()#splits the lines into a list of values
        
        for value in lotto_numbers:
            if value  in the_winning_numbers_list: # if the value is a winning number, put a star next to it
                current_line_answer += str(value)+ "* "
            else:
                current_line_answer += str(value) + " "
        answer.append(current_line_answer)
    return answer #one list containing the answers to each line.

def print_answer(answer):
    for lines in answer:
        print(lines)

def main():
    """the main function"""
    #You can change the max numbers in a lotto row and the highest valid number with these constants:
    NUMBERS_IN_LOTTO_ROW = 5
    HIGHEST_VALID_NUMBER = 40

    file_name = input("Enter file name: ") 
    a_file = open_file(file_name)
    #if file is found proceed, else return an error message.
    if a_file:
        winning_numbers = get_winning_numbers(NUMBERS_IN_LOTTO_ROW, HIGHEST_VALID_NUMBER)
        if winning_numbers:
            to_print = check_if_won(a_file,winning_numbers) #compares the numbers in the file to the winning numbers and puts a star where they match
            print_answer(to_print)#prints the results of each line
        else:
            print("Winning numbers are invalid!")
        a_file.close #Always close a file when done using it.

    #prints the error message if the file is not found.
    else:
        print("File {} not found!".format(file_name))

#Main program executed.
main()

class Distribution:
    
    def __init__(self,other = None):
        #if fed a data stream, creates a dictionary out of the information
        if other:
            the_file = other.read()
            file_stream_list = the_file.split()
            keys = set(file_stream_list)
            key_list = list(keys)
            key_list.sort()
            for keys in range(len(key_list)):
                key_list[keys] = int(key_list[keys])

            the_dict = {}
            for key_number in range(len(key_list)):
                key_amount = 0
                for a_number in file_stream_list:
                    if int(a_number) == key_list[key_number]:
                        key_amount +=1
                the_dict.update({key_list[key_number]:key_amount})
            self.__distribution = the_dict

        else: # if not fed anything, self.__distribution becomes None
            self.__distribution = other

    def set_distribution(self, distribution):
        #allows user to change the value of self.__distribution
        self.__distribution = distribution

    def average(self):
        #finds the average by multiplying every number by its counter and then devided by the sum of all the counters
        average = 0
        total_numbers = 0
        current_value = 0
        if self.__distribution != None:
            for each in self.__distribution:
                current_value += (self.__distribution[each])*each
                total_numbers += self.__distribution[each]
            average = current_value/total_numbers
        return average

    def __ge__(self, other):
        #allows you to compare two instances of this class by comparing their average.
        return self.average() >= other.average()
    
    def __add__(self,other):
        #allows you to add to gether two instances of the class by creating merging the dicts in self.__distribution and other.__distribution into a new dict
        #then returns a new instance of itself with the new dict as self.__distribution.
        temp_list = []
        temp_dict = {}
        #merging the dicts:
        for each in other.__distribution:
            if each in self.__distribution:
                self.__distribution[each] += other.__distribution[each]
            else:
                self.__distribution.update({each:other.__distribution[each]})
        
        for each in self.__distribution:
            temp_list.append([each,self.__distribution[each]])
        temp_list.sort()
        for each in temp_list:
            temp_dict.update({each[0]:each[1]})
        self.__distribution = temp_dict
        #returns a new instance of itself:
        return self

    def __str__(self):
        #delivers the data in self.__distribution as a neat string.
        string = ""
        if self.__distribution != None:
            for each in self.__distribution:
                string += ("{}: {}\n".format(each,self.__distribution[each]))
        return string