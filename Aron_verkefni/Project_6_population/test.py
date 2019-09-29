def read_file():
    """Askes the user for a file name and tries to open it"""

    file_name=input("Enter filename: ")
    try:
        the_file=open(file_name,"r")
        return the_file
    except FileNotFoundError:
        print("Filename {} not found!".format(file_name))


def file_to_list(file_to_read):
    """Takes in a file and creates a list"""

    nested_list=[]
    first_line=file_to_read.readline()
    first_line=first_line.split()
    rows=len(first_line)
    for lines in file_to_read:
        lines=lines.split()
        if len(lines)>rows:
            lines[0] = lines[0] + " " + lines[1]
            del lines[1]
        for ind in range (1,len(lines)):
            lines[ind]=int(lines[ind])
        nested_list.append(lines)
    nested_list.insert(0,first_line)
    return nested_list


def what_year(the_list):
    """Askes the user for a year and if the year is valid, returns lists for the states and population, of said year"""

    pop_list=[]
    name_list=[]
    to_continue=True

    #A loop that repeats until the user has typed a valid year
    while to_continue:
        input_year=input("Enter year: ")

        if input_year in the_list[0]:
            to_continue=False
            position = the_list[0].index(input_year)
        else:
            print("Invalid year!")
    #Creates creates the population list and the name of state list based on the selected year
    for each in range(1,len(the_list)):
        pop_list.append(the_list[each][position])
        name_list.append(the_list[each][0])

    return pop_list,name_list

def min_max_of_year(pop_list,name_list):
    """returns the max/min values and corresponding names from a list and an index"""
    
    max_value=max(pop_list)
    max_name_index=pop_list.index(max_value)
    max_name=name_list[max_name_index]
    

    min_value=min(pop_list)
    min_name_index=pop_list.index(min_value)
    min_name=name_list[min_name_index]

    min_tuple = (min_value,min_name)
    max_tuple = (max_value,max_name)
    return min_tuple,max_tuple
    
#The main code
target_file=read_file()
nested_list=file_to_list(target_file)
population,names=what_year(nested_list)
lowest,highest=min_max_of_year(population,names)
print("Minimum: {}".format(lowest))
print("Maximum: {}".format(highest))