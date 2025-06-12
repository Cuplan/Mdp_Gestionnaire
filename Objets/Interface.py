# Interface graphique de l'application
from .Users import Users
from .Generateur import Generateur
from .GestionUsers import GestionUsers
from .security import chiffrer_json, dechiffrer_json

import tkinter as tk
from tkinter import messagebox

class Interface:

    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("Gestionnaire de mots de passe")
        self.fenetre.geometry("750x500")
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
        
    def connexion(self):
        ndc = self.entre_ndc.get().strip()
        mdp = self.entre_mdp.get().strip()

        user = GestionUsers.chercher_user(ndc)

        if user:
            print(f"user trouvé : {user._ndc}")
            if user.connexion(mdp):  # ⬅️ uniquement le mot de passe
                messagebox.showinfo("Connexion réussie", f"Bienvenue {ndc}!")
                self.interface_utilisateur(user)
            else:
                messagebox.showerror("Erreur", "Mot de passe incorrect.")
        else:
            messagebox.showerror("Erreur", "Nom d'utilisateur introuvable.")
     
    def creer_compte(self):
        # Effacer les widgets existants
        for widget in self.fenetre.winfo_children():
            widget.destroy()

        frame_creation = tk.Frame(self.fenetre, bg="#102a3b")
        frame_creation.pack(expand=True)

        tk.Label(frame_creation, text="Créer un compte", font=("Helvetica", 16), bg="#102a3b", fg="white").pack(pady=(10, 20))

        # Champ nom d'utilisateur
        tk.Label(frame_creation, text="Nom d'utilisateur:", bg="#102a3b", fg="white").pack()
        entry_ndc = tk.Entry(frame_creation, width=30)
        entry_ndc.pack(pady=(0, 10))

        # Champ mot de passe
        tk.Label(frame_creation, text="Mot de passe:", bg="#102a3b", fg="white").pack()
        entry_mdp = tk.Entry(frame_creation, width=30, show="*")
        entry_mdp.pack(pady=(0, 10))

        # Champ copiable pour mot de passe généré
        entry_gen = tk.Entry(frame_creation, width=30)
        entry_gen.pack(pady=5)

        # --- Fonction imbriquée : générer mot de passe ---
        def generer():
            g = Generateur()
            mdp = g.genMdp()
            entry_mdp.delete(0, tk.END)
            entry_mdp.insert(0, mdp)
            entry_gen.delete(0, tk.END)
            entry_gen.insert(0, mdp)

        # --- Fonction imbriquée : copier mot de passe ---
        def copier_mdp():
            mdp = entry_gen.get()
            self.fenetre.clipboard_clear()
            self.fenetre.clipboard_append(mdp)
            messagebox.showinfo("Copié", "Mot de passe copié dans le presse-papier.")

        # --- Fonction imbriquée : valider création de compte ---
        def valider_creation():
            ndc = entry_ndc.get().strip()
            mdp = entry_mdp.get().strip()

            if not ndc or not mdp:
                messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
                return

            if GestionUsers.ajouter_user(ndc, mdp):
                messagebox.showinfo("Succès", "Compte créé avec succès!")
                self.afficher_accueil()
            else:
                messagebox.showerror("Erreur", "Nom d'utilisateur déjà utilisé.")



        # Boutons
        bouton_gen = tk.Button(frame_creation, text="Générer mot de passe", bg="#1c4966", fg="white", command=generer)
        bouton_gen.pack(pady=5)

        bouton_copier = tk.Button(frame_creation, text="Copier mot de passe", bg="#1c4966", fg="white", command=copier_mdp)
        bouton_copier.pack(pady=5)

        bouton_creer = tk.Button(frame_creation, text="Créer le compte", bg="#1c4966", fg="white", command=valider_creation)
        bouton_creer.pack(pady=5)

        bouton_retour = tk.Button(frame_creation, text="Retour", bg="#1c4966", fg="white", command=self.afficher_accueil)
        bouton_retour.pack(pady=10)
        
        
        
        
    def interface_utilisateur(self, user):
            
        # Nettoyer l'écran
        for widget in self.fenetre.winfo_children():
            widget.destroy()

        self.user_connecte = user  # Stocke l'utilisateur actuel

        self.frame_menu = tk.Frame(self.fenetre, bg="#102a3b")
        self.frame_menu.pack(expand=True, fill="both")

        # Titre
        tk.Label(
            self.frame_menu,
            text=f"Bienvenue {user._ndc}!",
            font=("Helvetica", 16),
            bg="#102a3b",
            fg="white"
        ).pack(pady=20)

        # Boutons du menu
        tk.Button(self.frame_menu, text="Gérer mes mots de passe", bg="#1c4966", fg="white", command=lambda: self.interface_stockage(user)).pack(pady=10)
        tk.Button(self.frame_menu, text="Générer un mot de passe", bg="#1c4966", fg="white", command=self.interface_generateur).pack(pady=10)
        tk.Button(self.frame_menu, text="Se déconnecter", bg="#8c1c1c", fg="white", command=self.afficher_accueil).pack(pady=10)

    def interface_stockage(self, user):
        import json
        import os
        from tkinter import messagebox

        for widget in self.fenetre.winfo_children():
            widget.destroy()

        self.frame_user = tk.Frame(self.fenetre, bg="#102a3b")
        self.frame_user.pack(expand=True, fill="both")

        tk.Label(
            self.frame_user,
            text="Stockage des mots de passe",
            font=("Helvetica", 16),
            bg="#102a3b",
            fg="white"
        ).pack(pady=10)

        # Champs à remplir
        champs = {}
        for label in ["Site", "Nom d'utilisateur", "Mot de passe", "Réponse secrète (optionnel)"]:
            tk.Label(self.frame_user, text=label, bg="#102a3b", fg="white").pack()
            champs[label] = tk.Entry(self.frame_user, width=40)
            champs[label].pack(pady=2)

        # Zone d’affichage avec scrollbar
        frame_liste = tk.Frame(self.frame_user)
        frame_liste.pack(pady=10)

        scrollbar = tk.Scrollbar(frame_liste)
        scrollbar.pack(side="right", fill="y")

        liste_mdp = tk.Text(frame_liste, height=10, width=60, yscrollcommand=scrollbar.set)
        liste_mdp.pack(side="left", fill="both")
        scrollbar.config(command=liste_mdp.yview)

        liste_mdp.insert(tk.END, "Sites enregistrés :\n")
        liste_mdp.configure(state='disabled')

        # Préparer fichier JSON
        fichier_stockage = f".secrets/mdp_{user._id}.json"

        if not hasattr(self, "stockage"):
            self.stockage = {}
        if user._id not in self.stockage:
            if os.path.exists(fichier_stockage):
                if os.path.exists(fichier_stockage):
                    with open(fichier_stockage, "rb") as f:
                        self.stockage[user._id] = dechiffrer_json(f.read())

            else:
                self.stockage[user._id] = []

        # Charger les entrées existantes
        for entree in self.stockage[user._id]:
            site, ndc, mdp, rep = entree
            liste_mdp.configure(state='normal')
            liste_mdp.insert(tk.END, f"{site} | {ndc} | {mdp} | {rep or '---'}\n")
            liste_mdp.configure(state='disabled')

        def sauvegarder():
            with open(fichier_stockage, "wb") as f:
                f.write(chiffrer_json(self.stockage[user._id]))


        def ajouter_site():
            site = champs["Site"].get().strip()
            ndc = champs["Nom d'utilisateur"].get().strip()
            mdp = champs["Mot de passe"].get().strip()
            rep = champs["Réponse secrète (optionnel)"].get().strip()

            if not site or not ndc or not mdp:
                messagebox.showerror("Erreur", "Tous les champs obligatoires doivent être remplis.")
                return

            self.stockage[user._id].append((site, ndc, mdp, rep))
            sauvegarder()

            liste_mdp.configure(state='normal')
            liste_mdp.insert(tk.END, f"{site} | {ndc} | {mdp} | {rep or '---'}\n")
            liste_mdp.configure(state='disabled')

            for champ in champs.values():
                champ.delete(0, tk.END)

        # Boutons
        frame_boutons = tk.Frame(self.frame_user, bg="#102a3b")
        frame_boutons.pack(pady=10)

        tk.Button(frame_boutons, text="Ajouter", bg="#1c4966", fg="white", command=ajouter_site).pack(side="left", padx=10)
        tk.Button(frame_boutons, text="Retour", bg="#8c1c1c", fg="white", command=lambda: self.interface_utilisateur(user)).pack(side="left", padx=10)

    def interface_generateur(self):

        for widget in self.fenetre.winfo_children():
            widget.destroy()

        self.frame_gen = tk.Frame(self.fenetre, bg="#102a3b")
        self.frame_gen.pack(expand=True, fill="both")

        tk.Label(self.frame_gen, text="Générateur de mot de passe", font=("Helvetica", 16), bg="#102a3b", fg="white").pack(pady=10)

        g = Generateur()
        entry_gen = tk.Entry(self.frame_gen, width=40)
        entry_gen.pack(pady=(10, 0))

        def generer_mdp():
            mdp = g.genMdp()
            entry_gen.delete(0, tk.END)
            entry_gen.insert(0, mdp)

        def copier_mdp():
            mdp = entry_gen.get()
            self.fenetre.clipboard_clear()
            self.fenetre.clipboard_append(mdp)
            messagebox.showinfo("Copié", "Mot de passe copié !")

        tk.Button(self.frame_gen, text="Générer un mot de passe", bg="#1c4966", fg="white", command=generer_mdp).pack(pady=5)
        tk.Button(self.frame_gen, text="Copier le mot de passe", bg="#1c4966", fg="white", command=copier_mdp).pack(pady=5)
        tk.Button(self.frame_gen, text="Retour", bg="#8c1c1c", fg="white", command=lambda: self.interface_utilisateur(self.user_connecte)).pack(pady=10)

        

    # Lance l'application ! :) 
    def lancer(self):
        self.fenetre.mainloop()
        
        
        
        
    
