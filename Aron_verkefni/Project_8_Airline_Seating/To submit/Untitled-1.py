import string
def user_input():
    rows = int(input("Enter number of rows: "))
    seats_in_rows = int(input("Enter number of seats in each row: "))
    return rows , seats_in_rows

def seat_nr_input():
    seat_info = input("Input seat number (row seat): ").split()
    try:
        seat_row = int(seat_info[0])
    except ValueError:
        return (0," ") #will fail the valid input test
    seat_char = seat_info[1].upper()
    return (seat_row,seat_char)

def setup(rows, seat_in_rows):
    total_space = 0
    final_list = []
    counter = 0
    alphabet = list(string.ascii_uppercase)
    seat_used = alphabet[:seat_in_rows]
    while counter < rows:
        to_use = []
        for seats in seat_used:
            to_use.append(seats)
            total_space+=1
        final_list.append(to_use)
        counter+=1
    return final_list,total_space

def print_seats(any_list):
    ISLE = "  "
    splitter = int(len(any_list[0])/2)

    for number in range(0,len(any_list)):
        first_batch = ""
        second_batch = ""

        for seat_nr in range(0,splitter):
            first_batch += any_list[number][seat_nr] + " "
            second_batch += any_list[number][seat_nr + splitter] + " "

        first_batch[splitter].strip()
        second_batch.strip()
        print("{:>2}   {}{}{}".format(number+1,first_batch,ISLE,second_batch))

def book_seat(some_list,reff,a_tuple,total_booked):
    again = False
    if len(some_list)>= a_tuple[0]:#if the seat to change is in a valid row
        row_index = a_tuple[0]-1
        seat = a_tuple[1]
        print(a_tuple[1])
        print(reff)
        if seat in some_list[row_index]:
            place = some_list[row_index].index(seat)
            some_list[row_index][place] = "X"
            valid_choice = True
            total_booked +=1

        elif a_tuple[1] in reff[row_index]:
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
    return some_list,again,valid_choice,total_booked

def to_repeat(bolean):
    responce = input("More seats (y/n)? ")
    if responce == "y":
        bolean = True
    return bolean

def main():
    total_booked = 0
    again = True
    valid = False
    first,second = user_input()
    listi,total_space = setup(first,second)
    refference_list,total_space = setup(first,second)
    reference_tuple = tuple(refference_list) #only for refference, not intended to be modified.
    print_seats(listi)

    while again:
        tupla = seat_nr_input()
        listi,again,valid,total_booked = book_seat(listi,reference_tuple,tupla,total_booked)
        if valid:
            print_seats(listi)
            if total_space > total_booked:
                again = to_repeat(again)

main()