import string
def open_file():
    name = input("Enter name of file: ")
    try:
        skra = open(name,"r")
        return skra
    except FileNotFoundError:
        print(("File {} not found!").format(name))


def scramble_middle(texti):
    """A function that "scrambles" words by swapping adjacent characters from left to right, but leaves the first and last character untouched"""
    nota = ""
    utkoma = ""
    punct = ""
    place = 0
    
    if texti[-1] in string.punctuation:
        punct = texti[-1]
        nota = texti[0:-1]
    else:
        nota = texti[0:len(texti)]

    byrjun = nota[0]
    midja = nota[1:-1]
    reps = len(midja)//2

    if len(nota)>1:
        if len(nota) % 2 == 0:
            lok = nota[-1]
        else:
            lok=nota[-2::]
    else:
        lok = ""

    while reps>0:
        stafur_1 = midja[(0+place)]
        stafur_2 = midja[(1+place)]
        utkoma += (stafur_2+stafur_1)
        reps -= 1
        place += 2
    return (byrjun + utkoma + lok + punct)

#The main 
outcome = ""
skra = open_file()

#Each line is scrambled and a single line text is created.
for lines in skra:
    lines = lines.rstrip()
    outcome += (scramble_middle(lines)+" ")
print(outcome)