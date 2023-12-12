from domain.mobilier import Mobilier

class RepoMobilier:
    def __init__(self):
        self._mobila = {}
    
    def get_all(self):
        return [self._mobila[mobila] for mobila in self._mobila]

class FileRepoMobilier(RepoMobilier):
    
    
    def __read_all_from_file(self):
        with open(self.__file_path,"r") as f:
            self._mobila.clear()
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                parts = line.split(",")
                cod = parts[0]
                tip = parts[1]
                nume = parts[2]
                stoc = int(parts[3])
                pret = float(parts[4])
                mobilier = Mobilier(cod,tip,nume,stoc,pret)
                self._mobila[cod] = mobilier
    
    
    def __init__(self, file_path):
        RepoMobilier.__init__(self)
        self.__file_path = file_path
        self.__read_all_from_file()
        
    def get_all(self):
        self.__read_all_from_file()
        return RepoMobilier.get_all(self)
    



