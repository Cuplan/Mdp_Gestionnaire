# Interface graphique de l'application
from .Users import Users
from .Stockage import Stockage
from .GestionMdp import GestionMdp

import tkinter as tk

class Interface:

    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("Gestionnaire de mots de passe")
        self.fenetre.geometry("500x350")
        self.fenetre.configure(bg="#102a3b")

        self.afficher_accueil()

    def afficher_accueil(self):
        # Effacer l'ancien contenu s'il y en a
        for widget in self.fenetre.winfo_children():
            widget.destroy()

        # Frame principale centrée
        self.frame_accueil = tk.Frame(self.fenetre, bg="#102a3b")
        self.frame_accueil.pack(expand=True)

        # Titre
        titre = tk.Label(
            self.frame_accueil,
            text="Bienvenue dans le gestionnaire",
            font=("Helvetica", 16),
            bg="#102a3b",
            fg="white"
        )
        titre.pack(pady=(10, 20))

        # Champ nom de compte
        tk.Label(self.frame_accueil, text="Nom de compte:", bg="#102a3b", fg="white").pack()
        self.entre_ndc = tk.Entry(self.frame_accueil, width=30)
        self.entre_ndc.pack(pady=(0, 10))

        # Champ mot de passe
        tk.Label(self.frame_accueil, text="Mot de passe:", bg="#102a3b", fg="white").pack()
        self.entre_mdp = tk.Entry(self.frame_accueil, width=30, show="*")
        self.entre_mdp.pack(pady=(0, 20))

        # Boutons
        bouton_connexion = tk.Button(self.frame_accueil, text="Connexion", width=20, bg="#1c4966", fg="white", command=self.connexion)
        bouton_connexion.pack(pady=5)

        bouton_reset = tk.Button(self.frame_accueil, text="Reset", width=20, bg="#1c4966", fg="white", command=self.reset_champs)
        bouton_reset.pack(pady=5)

        bouton_creation = tk.Button(self.frame_accueil, text="Créer un compte", width=20, bg="#1c4966", fg="white", command=self.creer_compte)
        bouton_creation.pack(pady=5)

    # Fonction qui reset les champs 
    def reset_champs(self):
        self.entre_ndc.delete(0, tk.END)
        self.entre_mdp.delete(0, tk.END)
    # Fonction de connexion 
    def connexion(self):
        ndc = self.entre_ndc.get()
        mdp = self.entre_mdp.get()
        print(f"Tentative de connexion avec : {ndc} / {mdp}")
        # À compléter : logique de validation
        user = Users.authentification(ndc,mdp)

    # Fonction de création de compte 
    def creer_compte(self):
        print("Rediriger vers page création de compte (à venir)")
        # À compléter : changement de frame/page
        
    # Lance l'application ! :) 
    def lancer(self):
        self.fenetre.mainloop()
        
        
        
        
    
