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