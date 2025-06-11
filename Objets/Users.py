# Users de l'application; car il faudra se connecter ! 
class Users:
    
    # Initialisation d'une classe  
    def __init__(self,id: int, ndc:str, mdp:str):
        self._id = id
        self._ndc = ndc 
        self.__mdp = mdp
        
        
    # Permet de valider le mdp sans le montrer! :P 
    # PLUS TARD: ajouter hashlib ! 
    def validationMdp(self, essaie: str) -> bool:
        return self.__mdp == essaie
    
    def validationNdc(self,essaie: str) -> bool:
        return self._ndc == essaie
    
    def connexion(self, ndc: str, mdp: str) -> bool:
            return self.validationNdc(ndc) and self.validationMdp(mdp)
