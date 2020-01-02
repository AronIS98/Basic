class starfsmadur:
    def __init__(self):
        self.employee_numb = 5221
        self.nafn = "Guðbrandur"
        self.salery = 2500
    
class yfirmadur(starfsmadur):
    def reka_starfsmann(self):
        self.employee_numb = 0
        self.nafn = ""
        self.salery = 0        

class ceo (yfirmadur):
    def mun_ekki_nota(self):
        print("ups")

stjori = ceo()
print(stjori.nafn)