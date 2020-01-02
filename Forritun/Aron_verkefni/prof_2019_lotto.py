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