import json
import os
from .Users import Users
import hashlib

@staticmethod
def hasher_mdp(mdp: str) -> str:
        return hashlib.sha256(mdp.encode()).hexdigest()

class GestionUsers:
    utilisateurs = []
    compteur_id = 1
    fichier = ".secrets/users.json"

    @classmethod
    def charger_utilisateurs(cls):
        if os.path.exists(cls.fichier):
            with open(cls.fichier, "r") as f:
                data = json.load(f)
                cls.utilisateurs = [
                    Users(u["id"], u["ndc"], u["mdp"]) for u in data
                ]
                if cls.utilisateurs:
                    cls.compteur_id = max(u._id for u in cls.utilisateurs) + 1

    @classmethod
    def sauvegarder_utilisateurs(cls):
        with open(cls.fichier, "w") as f:
            data = [
                {"id": u._id, "ndc": u._ndc, "mdp": u._Users__mdp}
                for u in cls.utilisateurs
            ]
            json.dump(data, f, indent=4)

    @classmethod
    def ajouter_user(cls, ndc, mdp):
        if cls.chercher_user(ndc) is not None:
            return False
        
        mdp_hache = hasher_mdp(mdp)
        nouvel_user = Users(cls.compteur_id, ndc, mdp_hache)
        cls.utilisateurs.append(nouvel_user)
        cls.compteur_id += 1
        cls.sauvegarder_utilisateurs()
        return True

    @classmethod
    def chercher_user(cls, ndc):
        for user in cls.utilisateurs:
            if user.validationNdc(ndc):
                return user
        return None

    @classmethod
    def authentifier(cls, ndc, mdp):
        user = cls.chercher_user(ndc)
        if user:
            return user.connexion(ndc, mdp)
        return False
    

