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

    big_list=[]
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

    new_list=[]
    name_list=[]
    
    for each in range(1,len(the_list)):
        new_list.append(the_list[each][the_index])
        name_list.append(the_list[each][0])

    max_value=max(new_list)
    max_name_index=new_list.index(max_value)
    max_name=name_list[max_name_index]

    min_value=min(new_list)
    min_name_index=new_list.index(min_value)
    min_name=name_list[min_name_index]

    min_tuple = (min_value,min_name)
    max_tuple = (max_value,max_name)
    return min_tuple,max_tuple
    
#The main code
target_file=read_file()
big_list=file_to_list(target_file)
to_index=what_year(big_list)
lowest,highest=min_max_of_year(big_list,to_index)
print("Minimum: {}".format(lowest))
print("Maximum: {}".format(highest))