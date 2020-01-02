def user_input():
    """a function that if given more than 2 inputs, creates a list of floats from the input"""
    from_user = input("Enter scores separated by space: ")
    input_list = from_user.split()
    if len(input_list) < 2:
        print("At least two scores needed!")
    else:
        for numbers in range(0,len(input_list)):
            input_list[numbers]=float(input_list[numbers])
    return input_list

def sum_highest(a_list):
    """A function that finds the sum of all the numbers excluding the lowest 2"""
    
    counter=0
    #Deletes the lowest two numbers from the list
    while counter < 2:
        current_lowest = min(a_list)
        to_del = a_list.index(current_lowest)
        del a_list[to_del]
        counter +=1
    #Sums up all the numbers in the list    
    sum_of_floats=0
    for floats in a_list:
        sum_of_floats += floats

    sum_of_floats = round(sum_of_floats,1) #Needs to round because the float calculations where sometimes off by way less than 1*10^-6
    return sum_of_floats

LIST_TO_USE=user_input()
SUM_OF_FLOATS = sum_highest(LIST_TO_USE)
print("Sum of scores (two lowest removed): ",SUM_OF_FLOATS)


