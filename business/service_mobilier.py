from erori.exceptii import ValidError
class ServiceMobilier:
    
    
    def __init__(self, __repo, __validator):
        self.__repo = __repo
        self.__validator = __validator
        
    
    def gaseste_dupa_tip(self,tip):
        mobilier = self.__repo.get_all()
        tipuri = [_mobilier.get_tip() for _mobilier in mobilier]
        if tip not in tipuri:
            raise ValidError("nu exista tipul!")
        return [_mobilier for _mobilier in mobilier if _mobilier.get_tip()==tip]
    
    
    def top_k_mobilier_dupa_pret(self,k):
        mobilier = self.__repo.get_all()
        mobilier.sort(key = lambda x: x.get_pret(),reverse = True)
        return mobilier[:k]
    
    
    
    



