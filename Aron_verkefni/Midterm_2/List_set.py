def input_to_int_sets():
    """Recives two inputs transforms them into two sets containing only integers"""
    set_1 = []
    set_2 = []
    input_1 = input("Enter elements of a list separated by space: ")
    input_2 = input("Enter elements of a list separated by space: ")

    input_list_1 = input_1.split()
    input_list_2 = input_2.split()

    #Creates a new lists without dublicates:
    for each_1 in input_list_1:
        if each_1 not in set_1:
            set_1.append(each_1)

    for each_2 in input_list_2:
        if each_2 not in set_2:
            set_2.append(each_2)

    #Converts the strings in the lists to intigers
    for each_string in range(0,len(set_1)):
        set_1[each_string] = int(set_1[each_string])

    for string_nr in range(0,len(set_2)):
        set_2[string_nr] = int(set_2[string_nr])
        
    set_1.sort()
    set_2.sort()

    return set_1,set_2

def intersect_union (list_1,list_2):
    """Recives two lists and returns two new lists containing their intersects and their union"""
    list_of_all_numbers = list_1 + list_2
    list_of_all_numbers.sort()
    intersect_list = []
    union_list =[]

    for numbers in list_of_all_numbers:
        if numbers not in union_list:
            union_list.append(numbers)

    for current_number in list_1:
        if current_number in list_2:
            intersect_list.append(current_number)
    return intersect_list,union_list

SET_LIST_1, SET_LIST_2 = input_to_int_sets()
INTERSECTION, UNION = intersect_union (SET_LIST_1, SET_LIST_2)

print("Set 1:",SET_LIST_1)
print("Set 2:",SET_LIST_2)
print("Intersection:",INTERSECTION)
print("Union:",UNION)


