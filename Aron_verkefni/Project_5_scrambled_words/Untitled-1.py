def open_file():
    try:
        name = "test.txt"
        with open(name,"r") as skra:
            a_file = skra
        return a_file
    except FileNotFoundError:
        print("File not found")
        return False
lala = open_file()
for each in lala:
    print(each)


    
#skráin er lokuð því við erum ekki lengur inní "with"