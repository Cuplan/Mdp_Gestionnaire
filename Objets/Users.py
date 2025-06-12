# Users de l'application; car il faudra se connecter ! 
import hashlib

class Users:
    
    # Initialisation d'une classe  
    def __init__(self,id: int, ndc:str, mdp:str):
        self._id = id
        self._ndc = ndc 
        self.__mdp = mdp
        
        
    # Permet de valider le mdp sans le montrer! :P 
    # PLUS TARD: ajouter hashlib ! 
    def validationMdp(self, essaie: str) -> bool:
        mdp_essaye = hashlib.sha256(essaie.encode()).hexdigest()
        return self.__mdp == mdp_essaye
    
    def validationNdc(self,essaie: str) -> bool:
        return self._ndc == essaie
    
    def connexion(self, mdp: str) -> bool:
        return self.validationMdp(mdp)

