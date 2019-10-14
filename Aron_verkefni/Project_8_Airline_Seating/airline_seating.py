import string
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
    counter = 0
    alphabet = list(string.ascii_uppercase)
    seat_used = alphabet[:seat_in_rows]
    while counter < rows:
        to_use = []
        for seats in seat_used:
            to_use.append(seats)
        final_list.append(to_use)
        counter+=1
    return final_list

def print_seats(any_list):
    ISLE = "   " #Three spaces
    splitter = int(len(any_list[0])/2)
    for number in range(0,len(any_list)):
        first_batch = ""
        second_batch = ""
        for seat_nr in range(0,splitter):
            first_batch += any_list[number][seat_nr] + " "
            second_batch += any_list[number][seat_nr + splitter] + " "
        first_batch.rstrip()
        second_batch.rstrip()
        print("{:>2}  {}{}{}".format(number+1,first_batch,ISLE,second_batch))



def book_seat(some_list,reff,a_tuple):
    again = False
    if len(some_list)>= a_tuple[0]:#if the seat to change is in a valid row
        row_index = a_tuple[0]-1
        seat = a_tuple[1]

        if seat in some_list[row_index]:
            place = some_list[row_index].index(seat)
            some_list[row_index][place] = "X"
            valid_choice = True

        elif a_tuple[1] in reference_tuple[row_index]:
            print("That seat is taken!")
            again = True
            valid_choice = False
        else:
            print("Seat number is invalid!")
            again = True
            valid_choice = False
    else:
        print("Seat number is invalid!")
        valid_choice = False
        again = True
    return some_list,again,valid_choice

def to_repeat(bolean):
    responce = input("More seats (y/n)? ")
    if responce == "y":
        bolean = True
    return bolean

again = True
valid = False
first,second = user_input()
listi = setup(first,second)
reference_tuple = tuple(setup(first,second)) #only for refference, not intended to be modified.
print_seats(listi)

while again:
    tupla = seat_nr_input()
    listi,again,valid = book_seat(listi,reference_tuple,tupla)
    if valid:
        print_seats(listi)
        again = to_repeat(again)
