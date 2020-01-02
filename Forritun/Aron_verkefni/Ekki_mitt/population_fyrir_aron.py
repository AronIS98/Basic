def read_file():
    """convert file to list"""   
    filename = input("Enter filename: ")
    try:
        open_file = open(filename, "r")
        list_state_year = []
        first_line = open_file.readline().split()
        row = len(first_line)
        for line in open_file:
            line=line.split()
            if len(line) > row :
                line[0]=line[0]+ ' ' + line[1]
                del line[1]
            for objects in range(1,len(line)):
                line[objects]=int(line[objects])
            list_state_year.append(line)
        list_state_year.insert(0,first_line)
        open_file.close()
    except FileNotFoundError:
        print("Filename {} not found!".format(filename))   
    return list_state_year

def one_year(list_states_years):
    """choseing"""
    req=True
    while req:
        year = input("Enter year: ")
        if year in list_states_years[0]:
            position = list_states_years[0].index(year)
            req=False
        else:
            print("Invalid year!")
    return position

def year_and_states_tubule(position):
    """returnes many tubules 
    inside a list"""
    num_year = []
    num_state = []
    final_list=[]
    for each in range(1,len(list_states_years)):
        num_year = list_states_years[each][position]
        num_state = list_states_years[each][0]   
        final_tubule = (num_year,num_state)
        final_list.append(final_tubule)
    return final_list



list_states_years = read_file()
position = one_year(list_states_years) 
state_and_year = year_and_states_tubule(position)
most_people=max(state_and_year)
less_people=min(state_and_year)
print("Minimum:",less_people)
print("Maximum:",most_people)
print(list_states_years)
