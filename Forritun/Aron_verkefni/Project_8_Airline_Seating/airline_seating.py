import string
def user_input():
    """Askes the user for rows and number of seats, and returns them as ints."""
    rows = int(input("Enter number of rows: "))
    seats_in_rows = int(input("Enter number of seats in each row: "))
    return rows , seats_in_rows

def seat_nr_input():
    """Askes for a seat number, if an error occurs, sends a invalid tuple that will be caught by the
    book seat validation code"""
    seat_info = input("Input seat number (row seat): ").split()
    try:
        seat_row = int(seat_info[0])
    except ValueError:
        return False #will fail the valid input test

    seat_char = seat_info[1].upper()
    return (seat_row,seat_char)

def setup(rows, seat_in_rows):
    """Creates the grid (main list), calculates total space and
    assigns letters to the seats."""
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
    """Recives the list and prints it out in the requested format."""
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

def book_seat(some_list,reff,order_tuple,total_booked):
    """Books seat if the seat exists and is unbooked. If it doesnt, tells you if selected seat
    is already booked or invalid."""
    again = True
    valid_choice = False
    row_nr_index = 0
    seat_nr_index = 1
    if order_tuple !=False and len(some_list)>= order_tuple[row_nr_index]:#Checks if the row containing the seat exists and if the order_tuple is not False.
        row_index = order_tuple[row_nr_index] - 1
        seat = order_tuple[seat_nr_index]

        if seat in some_list[row_index]:#If the seat exists and is not booked, books it.
            place = some_list[row_index].index(seat)
            some_list[row_index][place] = "X"
            again = False
            valid_choice = True
            total_booked += 1

        elif order_tuple[1] in reff[row_index]:#If the seat is not available but was available in the original list it must be booked.
            print("That seat is taken!")
        else:
            print("Seat number is invalid!")#If the seat is not available and was never created to begin with, the seat number is invalid. 
    else:
        print("Seat number is invalid!")#If the row containing said seat number does not exist, the seat number must be invalid.
    return some_list,again,valid_choice,total_booked

def to_repeat(repeat):
    """Askes if the user wants to repeat again and returns a bool"""
    responce = input("More seats (y/n)? ")
    if responce == "y":
        repeat = True
    return repeat

def main():
    """The main function"""
    total_booked = 0
    again = True
    valid = False

    first,second = user_input()
    the_list,total_space = setup(first,second)#This list will be modified.
    refference_list = setup(first,second)
    reference_tuple = tuple(refference_list) #Only for refference, not intended to be modified.

    print_seats(the_list)
    while again:
        seat_address_tuple = seat_nr_input()
        the_list,again,valid,total_booked = book_seat(the_list,reference_tuple,seat_address_tuple,total_booked)
        if valid:# if the seat booking was valid, proceed.
            print_seats(the_list)
            if total_space > total_booked:#if the plain is full, prevent further booking.
                again = to_repeat(again)

main()