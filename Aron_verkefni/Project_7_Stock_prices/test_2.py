def find_file():
    """A function that askes for a file name and tries to open that file. If unable, returns False"""
    file_name = input("Enter filename: ")
    try:
        a_file = open(file_name,"r")
        return a_file
    except FileNotFoundError:
        print("Filename {} not found!".format(file_name))
        return False

def get_data_list(some_file):
    """A file that recives an open file and creates a stripped list"""
    data_list = []
    for lines in some_file:
        data_list.append(lines.strip().split(","))
    return data_list

def month_average(a_list):
    """Finds the average price each month and prints it"""
    #Lists:
    year_list = [] 
    list_of_months = []
    #Counter:
    number_of_month = 0
    #Indexes:
    ADJ_CLOSE_INDEX = 5
    RAW_VOLUME_INDEX = 6
    ORG_DATE_INDEX = 0
    AVERAGE_INDEX = 1
    VOLUME_INDEX = 2
    #The main code of the function:

    #Runs through the list.
    for numb in range(1,len(a_list)):

        month = a_list[numb][ORG_DATE_INDEX][:-3] # Remove the last 3 digits from the string to end up with only the year and month.
        day_price = float(a_list[numb][ADJ_CLOSE_INDEX])
        day_volume = int(a_list[numb][RAW_VOLUME_INDEX])
        day_average = day_volume * day_price
        #A setup run only once per month
        if month not in list_of_months:

            list_of_months.append(month)
            month_list = [month]
            average_list = [day_average]
            year_list.append(month_list)
            year_list[number_of_month].append(average_list)
            year_list[number_of_month].append(day_volume)
            number_of_month += 1
        #Updates the information the current month holds, if it has aldready been creeated.
        else:
            year_list[number_of_month-1][AVERAGE_INDEX].append(day_average)
            year_list[number_of_month-1][VOLUME_INDEX] += day_volume
    #Calculates the average price each month and prints it out.
    for current_month in range(0,len(year_list)):
        month_sum = sum(year_list[current_month][AVERAGE_INDEX])
        answer = month_sum/year_list[current_month][VOLUME_INDEX]

        tupla = (year_list[current_month][ORG_DATE_INDEX],answer)
        print("{:<10s}{:>7.2f}".format(tupla[ORG_DATE_INDEX],(tupla[AVERAGE_INDEX])))
    
def date_price_tuples(raw_list):
    """A function that creates a list of tuples, containing the date and price each day, from the original list"""
    DATE_INDEX = 0
    PRICE_INDEX = 5
    list_of_tuples = []
    for line_number in range (1,len(raw_list)): #starts at index 1 to skip the first line (that holds the header)
        a_tuple = (float(raw_list[line_number][PRICE_INDEX]) , raw_list[line_number][DATE_INDEX])
        list_of_tuples.append(a_tuple)
    return list_of_tuples

def print_max_day(tuples):
    """A function that finds the max price and date """
    maximum = max(tuples)
    print("Highest price {} on day {}".format(round(maximum[0],2),maximum[1]))

def main():
    """The main code"""
    the_file = find_file()
    if the_file:
        the_list = get_data_list(the_file)
        print("{:<10s}{:>7s}".format("Month","Price"))
        month_average(the_list)
        tuple_list = date_price_tuples(the_list)
        print_max_day(tuple_list)
        the_file.close
    
main()