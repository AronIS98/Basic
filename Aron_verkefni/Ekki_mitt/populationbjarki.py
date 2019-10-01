def open_file(filename):
    '''comment'''
    try:
        txt_file = open(filename)
        return txt_file
    except FileNotFoundError:
        print('Filename {} not found!'.format(filename))


def population():
    population_list = []
    for line in filename:
        line = line.strip()
        line_list = line.split()
        population_list.append(line_list)

        while len(line_list) > len(population_list[0]):
            line_list[0] = line_list[0] + ' ' + line_list[1]
            del line_list[1]
    return population_list


def year():
    done = False
    while not done:
        year_input = input('Enter year: ')
        if year_input in population_list[0]:
            counter = population_list[0].index(year_input)
            done = True
        else:
            print('Invalid year!')
    return counter


def min_max():
    min_max_list = []
    for i in range(1, len(population_list)):
        min_max_list.append(population_list[i][column])

    values = [int(num) for num in min_max_list]
    min_val = min(values)
    max_val = max(values)

    min_index = values.index(min_val) + 1
    max_index = values.index(max_val) + 1

    min_tuple = tuple([min_val, population_list[min_index][0]])
    max_tuple = tuple([max_val, population_list[max_index][0]])
    return min_tuple, max_tuple


def min_max_print():
    print('Minimum:', minimum)
    print('Maximum:', maximum)


# Main code starts here

filename = open_file(input('Enter filename: '))
population_list = population()
column = year()
minimum, maximum = min_max()
min_max_print()
strengur=" lala alala".rsplit()
print