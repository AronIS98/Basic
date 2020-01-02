travelers = {}
nafna_listi = []
nafna_listi_unsorted = []


def print_values(my_dict, nafna_listi):
    for key in nafna_listi:
        print(key + ":")
        for country in my_dict[key]:
            print("\t" + country)


def print_most_values(my_dict, nafna_listi, nafna_listi_unsorted):
    lengd = 0
    maxid = ""
    for key in nafna_listi:
        if len(my_dict[key]) > lengd:
            lengd = len(my_dict[key])
            maxid = key
        elif len(my_dict[key]) == lengd:
            for persons in nafna_listi_unsorted:
                if persons == maxid:
                    break
                elif persons == key:
                    maxid = key
                    break

    print(maxid, "has been to", lengd, "countries")


f = open("flights.txt", "r")
file = f.read().split("\n")

for line in file:
    if line != "":
        name, country = line.split()
        if name not in travelers:
            travelers[name] = []
            nafna_listi.append(name)
            nafna_listi_unsorted.append(name)

    if country not in travelers[name]:
        travelers[name].append(country)
        travelers[name].sort()
nafna_listi.sort()

print_values(travelers, nafna_listi)
print_most_values(travelers, nafna_listi, nafna_listi_unsorted)
