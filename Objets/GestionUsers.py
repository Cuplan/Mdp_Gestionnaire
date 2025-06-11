class GestionnaireUtilisateurs:
    utilisateurs = []
    compteur_id = 1

    def ajouter_user(cls, ndc, mdp):
        ...
        # crée un Users avec id unique, l’ajoute à la liste

    def chercher_user(cls, ndc):
        ...
        # retourne l’objet Users correspondant au nom

    def authentifier(cls, ndc, mdp):
        ...
        # utilise chercher_user, puis appelle user.connexion()
