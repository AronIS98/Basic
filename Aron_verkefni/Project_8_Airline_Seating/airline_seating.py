def user_input():
    rows = int(input("Enter number of rows: "))
    seats_in_rows = int(input("Enter number of seats in each row: "))
    return rows , seats_in_rows

def seat_nr_input():
    seat_info = input("Input seat number (row seat): ").split()
    seat_char = seat_info[1].upper()
    seat_row = int(seat_info[0])
    return (seat_row,seat_char)

def setup(rows, seat_in_rows):
    final_list = []
    alphabet = ["A","B","C","D","E","F"]
    seat_used = alphabet[:seat_in_rows]
    for counter in range (0,rows):
        final_list.append(seat_used)
    return final_list

def print_seats(any_list):
    ISLE = "   " #Three spaces
    splitter = int(len(any_list[0])/2)
    for number in range(0,len(any_list)):
        first_batch = ""
        second_batch = ""
        for seat_nr in range(0,splitter):
            first_batch += any_list[number][seat_nr] + " "
            second_batch += any_list[number][seat_nr+splitter] + " "
        first_batch.rstrip()
        second_batch.rstrip()
        print("{:>2}  {}{}{}".format(number+1,first_batch,ISLE,second_batch))
    
#def book_seat(some_list,a_tuple):
#    if len(some_list)>= a_tuple[0]:
"""
Plan, hafa refference lista með óbreyttum gildum og einn sem breytist
ef stafur er í óbreytta en ekki breytta er búið að pannta það sæti áður
"""



first,second = user_input()
listi = setup(first,second)
#tupla = seat_nr_input()
#listi = book_seat(tupla)
#print(tupla)
print_seats(listi)