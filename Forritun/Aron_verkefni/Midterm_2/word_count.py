def open_file():
    """A function that tries to open a file with the same name as the user inputs"""
    try:
        file_name = input("Enter filename: ")
        the_file=open(file_name,"r")
    except FileNotFoundError:
        print("File {} not found!".format(file_name))
    return the_file

def word_counter(a_file):
    """A function that counts the words in a file but counts special characters as their own words"""
    word_count = 0
    special_chars = ",.!?"
    # Checks each line in the file.
    for lines in a_file: 
        word_list = lines.split() 

        #checks if any of the special characters are in the words and if so, counts them as its own word.
        for current_word in word_list:

            for current_special_char in special_chars: #Runs once for each special character
                
                if current_special_char in current_word: # If it finds a special char, count it as a seperate word
                    word_count += 1

            word_count += 1
    return word_count

FIle_TO_USE = open_file()
TOTAL_WORDS = word_counter(FIle_TO_USE)
print(TOTAL_WORDS)