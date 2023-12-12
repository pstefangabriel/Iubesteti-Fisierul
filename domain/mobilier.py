class Mobilier:
    
    
    def __init__(self, cod, tip, nume, stoc, pret):
        self.__cod = cod
        self.__tip = tip
        self.__nume = nume
        self.__stoc = stoc
        self.__pret = pret

    def get_cod(self):
        return self.__cod


    def get_tip(self):
        return self.__tip


    def get_nume(self):
        return self.__nume


    def get_stoc(self):
        return self.__stoc


    def get_pret(self):
        return self.__pret


    def set_tip(self, value):
        self.__tip = value


    def set_nume(self, value):
        self.__nume = value


    def set_stoc(self, value):
        self.__stoc = value


    def set_pret(self, value):
        self.__pret = value

    def __eq__(self,other):
        return self.__cod == other.__cod


