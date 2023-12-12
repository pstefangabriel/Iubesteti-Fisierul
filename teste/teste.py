from persistenta.repo_mobilier import FileRepoMobilier
from validare.validator import ValidatorService
from business.service_mobilier import ServiceMobilier
class Teste(object):
    
    
    def run_all_tests(self):
        print("starts tests...")
        file_path = "C:\\Users\\stefan\\My Documents\\LiClipse Workspace\\IubesteFisierul\\teste\\test_mobilier.txt"
        repo = FileRepoMobilier(file_path)
        assert len(repo.get_all())==3
        validator = ValidatorService()
        service = ServiceMobilier(repo,validator)
        tip_cautat = "scaun"
        mobilier_gasit = service.gaseste_dupa_tip(tip_cautat)
        assert len(mobilier_gasit)==1
    
    



