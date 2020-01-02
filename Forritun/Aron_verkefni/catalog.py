class Item:
    def __init__(self,name,category):
        self.name = name
        self.category = category

    def set_name(self,updated_name):
        self.name = updated_name
    
    def set_category(self,updated_category):
        self.category = updated_category

    def __str__(self):
        """Dictates how the item is printed"""
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
        """Goes through the list and returns the item if found, else returns None"""
        for each in self.items:
            if other == each.name:
                return each
        return None

    def clear(self):
        """Clears the list of items"""
        self.items = []

    def __str__(self):
        """Dictates how the catalog is printed. (how it is displayd as a string)"""
        string = ("Catalog {}:".format(self.name))
        if self.items:
            for each in self.items:
                string += "\n\t{}".format(each)
        return string