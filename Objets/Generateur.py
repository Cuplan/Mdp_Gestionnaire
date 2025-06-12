import string, random

# Classe qui permet la gestion des mots de passe
class Generateur:
    # Initialisation de la classe 
    def __init__(self, longueurMin=12, longueurMax=36, noAmbigus=True):
        self.longueurMin = longueurMin
        self.longueurMax = longueurMax
        self.noAmbigus = noAmbigus
        self.ambigus = 'Il10O'
        
    # Fonction de génération
    def genMdp(self):
        # 1. Créer les groupes de base
        minus = list(string.ascii_lowercase)
        majus = list(string.ascii_uppercase)
        chiffres = list(string.digits)
        symboles = list('!"/$%?&*()-_+')

        # 2. Retirer les ambigus si demandé
        if self.noAmbigus:
            # On recherche si le cara is not dans ambigus; si oui on l'enlève
            minus = [c for c in minus if c not in self.ambigus]
            majus = [c for c in majus if c not in self.ambigus]
            chiffres = [c for c in chiffres if c not in self.ambigus]

        # 3. Fusionner tous les groupes dans un seul pool
        pool = minus + majus + chiffres + symboles
        # Une longueur random
        longueur = random.randint(self.longueurMin, self.longueurMax)

        # 4. Générer un mot de passe aléatoire
        mdp = [random.choice(pool) for _ in range(longueur)]
        random.shuffle(mdp)

        return "".join(mdp)
    
    
