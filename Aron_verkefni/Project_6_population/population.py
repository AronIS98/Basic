#Setup (functions)
def read_file():
    """Askes the user for a file name and tries to open it"""

    file_name=input("Enter filename: ")
    try:
        the_file=open(file_name,"r")
        return the_file
    except FileNotFoundError:
        print("Filename {} not found!".format(file_name))

def file_to_list(skra):
    """Takes in a file and creates a list"""

    big_list=[]
    first_line=skra.readline()
    first_line=first_line.split()
    rows=len(first_line)
    for lines in skra:
        lines=lines.split()
        if len(lines)>rows:
            lines[0] = lines[0] + " " + lines[1]
            del lines[1]
        for ind in range (1,len(lines)):
            lines[ind]=int(lines[ind])
        big_list.append(lines)
    big_list.insert(0,first_line)
    return big_list

def what_year(listi):
    """Askes the user for a year and checks if said year is in the list"""

    to_continue=True
    while to_continue:
        input_year=input("Enter year: ")
        if input_year in listi[0]:
            to_continue=False
            position = listi[0].index(input_year)
        else:
            print("Invalid year!")
    return position

def min_max_of_year(the_list,the_index):
    """returns the max/min values and corresponding names from a list and an index"""

    min_number = the_list[1][the_index]
    max_number = the_list[1][the_index]
    for each in range(1,len(the_list)):
        current_numb=the_list[each][the_index]
        current_name=the_list[each][0]

        if current_numb >= max_number:
            max_number = current_numb
            name_of_max = current_name
        if current_numb <= min_number:
            min_number = current_numb
            name_of_min = current_name
        
    minimum=(min_number,name_of_min)
    maximum=(max_number,name_of_max)
    return minimum,maximum

#The main code
skra=read_file()
big_list=file_to_list(skra)
to_index=what_year(big_list)
lowest,highest=min_max_of_year(big_list,to_index)
print("Minimum: {}".format(lowest))
print("Maximum: {}".format(highest))