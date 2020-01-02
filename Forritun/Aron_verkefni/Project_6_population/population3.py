def read_file():
    """Askes the user for a file name and tries to open it"""

    file_name = input("Enter filename: ")
    try:
        the_file = open(file_name,"r")
        return the_file
    except FileNotFoundError:
        print("Filename {} not found!".format(file_name))

def file_to_list(file_to_read): #comment more
    """Recives a file and creates a nested list"""

    nested_list = []
    first_line = file_to_read.readline()
    first_line = first_line.split()
    rows = len(first_line)
    for lines in file_to_read:
        lines = lines.split()

        if len(lines) > rows:
            lines[0] = lines[0] + " " + lines[1]
            del lines[1]

        for ind in range (1,len(lines)):
            lines[ind] = int(lines[ind])

        nested_list.append(lines)
    nested_list.insert(0,first_line)
    return nested_list

def what_year(the_list):
    """Askes the user for a year and if the year is valid, return its index"""

    to_continue=True
    while to_continue:
        input_year = input("Enter year: ")

        if input_year in the_list[0]:
            to_continue = False
            year_index = the_list[0].index(input_year)
        else:
            print("Invalid year!")
    return year_index

def min_max_of_year(the_list,position):
    """Creates a list of tuples containing the states and their population,
     then finds the min/max values and corresponding state name"""
    final_list = []

    for states in range(1,len(the_list)):
        population = the_list[states][position]
        name = the_list[states][0]
        pop_and_name_tuple = (population,name)
        final_list.append(pop_and_name_tuple)

    max_tuple = max(final_list)
    min_tuple = min(final_list)
    return min_tuple,max_tuple
    
#The main code
target_file = read_file()
nested_list = file_to_list(target_file)
year_index = what_year(nested_list)
lowest, highest = min_max_of_year(nested_list, year_index)
print("Minimum: " , lowest)
print("Maximum: " , highest)