class Item:
    def __init__(self,name,category):
        self.name = name
        self.category = category

    def set_name(self,updated_name):
        self.name = updated_name
    
    def set_category(self,updated_category):
        self.category = updated_category

    def __str__(self):
        return "Name: {}, Category: {}".format(self.name,self.category)

class Catalog:
    def __init__(self,named):
        self.name = named
        self.items = []
        
    def add(self,other):
        self.items.append(other)
    def remove(self,other):
        self.items.remove(other)

    def set_name(self,other):
        self.name = other
    
    def find_item_by_name(self,other):
        for each in self.items:
            if other == each.name:
                return(each)
            else:
                return None

    def clear(self):
        self.items = []

    def __str__(self):
        string = ""
        string+=("Catalog {}:".format(self.name))
        if self.items:
            string+="\n"
            for each in self.items:
                string += "\t{}\n".format(each)
            string.strip()
        return string
        

    

# ---------------------------------------test-------------------------------------------------------------------
# from catalog import Item
# from catalog import Catalog

item1 = Item("Green Book", "Biography")
print(item1)

item2 = Item("The God", "Crime")
print(item2)
item2.set_name("The Godfather")
print(item2)

item3 = Item("Schindler's List", "Biography")
print(item3)
item3.set_category("Drama")
print(item3)

catalog = Catalog('Films')
catalog.add(item1)
catalog.add(item2)
catalog.add(item3)
print(catalog)

catalog.remove(item2)
print(catalog)

catalog.set_name("Favorite Movies")
print(catalog)

print(catalog.find_item_by_name("Green Book"))
print(catalog.find_item_by_name("The Godfather"))

catalog.clear()
print(catalog)

