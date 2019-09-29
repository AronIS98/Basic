import string

def open_file():
    """A function that takes the name of a file as an input and opens it"""
    name = input("Enter name of file: ")
    try:
        my_file = open(name,"r")
        return my_file
    except FileNotFoundError:
        print(("File {} not found!").format(name))

def scramble_middle(texti):
    """A function that "scrambles" words by swapping adjacent characters from left to right, 
        but leaves the first and last character untouched"""
    shuffled_str = ""
    punct = ""
    final_char = ""
    place = 0
    
    if texti[-1] in string.punctuation:
        punct = texti[-1]
        str_cleaned = texti[0:-1]
    else:
        str_cleaned = texti

    first_char = str_cleaned[0]
    middle = str_cleaned[1:-1]
    reps = len(middle)//2

    if len(str_cleaned)>1:
        if len(str_cleaned) % 2 == 0:
            final_char = str_cleaned[-1]
        else:
            final_char=str_cleaned[-2::]
    #A loop in which the scrambling it self occurs:
    while reps>0:
        letter_1 = middle[(0 + place)]
        letter_2 = middle[(1 + place)]
        shuffled_str += (letter_2 + letter_1)
        reps -= 1
        place += 2
    return (first_char + shuffled_str + final_char + punct)

#The main program starts here ---------------------------------------
outcome = ""
text_file = open_file()

#Each line is scrambled and a single line text is created:
for lines in text_file:
    lines = lines.rstrip()
    outcome += (scramble_middle(lines)+" ")
print(outcome)