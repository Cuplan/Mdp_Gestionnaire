from Objets.security import generer_cle
generer_cle()

from Objets.GestionUsers import GestionUsers
GestionUsers.charger_utilisateurs()
# root du projet 

from Objets.Interface import Interface


if __name__ == "__main__":

    # Lance l'application graphique
    app = Interface()
    app.lancer()
    
