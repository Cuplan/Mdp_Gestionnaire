# fichier_securite.py
import os
import json
from cryptography.fernet import Fernet

# Dossier sécurisé
DOSSIER_SECRETS = ".secrets"
FICHIER_CLE = os.path.join(DOSSIER_SECRETS, "cle_secrete.key")


def generer_cle():
    """Génère une clé et la stocke dans un dossier sécurisé (une seule fois)."""
    if not os.path.exists(DOSSIER_SECRETS):
        os.makedirs(DOSSIER_SECRETS)
    if not os.path.exists(FICHIER_CLE):
        key = Fernet.generate_key()
        with open(FICHIER_CLE, "wb") as f:
            f.write(key)
        print("✅ Clé générée et sauvegardée dans .secrets/")
    else:
        print("🔐 Clé déjà existante.")


def charger_cle():
    """Charge la clé de chiffrement."""
    if not os.path.exists(FICHIER_CLE):
        raise FileNotFoundError(" Clé de chiffrement introuvable. Génère-la avec generer_cle().")
    with open(FICHIER_CLE, "rb") as f:
        return Fernet(f.read())


def chiffrer_json(donnees):
    """Prend un objet Python, retourne des bytes chiffrés."""
    fernet = charger_cle()
    donnees_json = json.dumps(donnees).encode()
    return fernet.encrypt(donnees_json)


def dechiffrer_json(chiffre_bytes):
    """Prend des bytes chiffrés, retourne l'objet Python original."""
    fernet = charger_cle()
    texte_json = fernet.decrypt(chiffre_bytes)
    return json.loads(texte_json.decode())
