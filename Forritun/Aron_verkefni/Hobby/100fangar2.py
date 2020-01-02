dagur=0
light_bulp_on = False
class fangar():
    """
    OMG FUCKN BULLSHIT
    """
    def __init__(self):
        self.has_switched_on_light_bulb=False

    def interrigated(self):
        """
        Athugar stöðu ljóss, breytir nr. hvaða dagur er
        """
        dagur=dagur+1
        #eftir þessa 50 daga
        if dagur>50 and light_bulp_on==False:
            light_bulp_on=True
            has_switched_on_light_bulb=True
        #ef allir 50 dagar tókust
        elif dagur==50 and light_bulp_on==False:
            light_bulp_on=True
            has_switched_on_light_bulb=True
            is_master=True
            counter=50
        elif dagur
        #ef dagur er minni en 50 og light on = false ekki gera neitt
    


