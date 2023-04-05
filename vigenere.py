import argparse
import os

# Fonction pour récupérer l'indice d'une lettre dans l'alphabet
def indice_alphabet(lettre):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return alphabet.index(lettre.lower())

# Fonction pour effectuer le chiffrement/déchiffrement de Vigenère
def vigenere(texte, cle, mode):
    texte_chiffre = ''
    for i, lettre in enumerate(texte):
        if lettre.isalpha():
            # Récupération de l'indice de la lettre du texte dans l'alphabet
            indice_texte = indice_alphabet(lettre)

            # Récupération de l'indice de la lettre de la clé dans l'alphabet
            indice_cle = indice_alphabet(cle[i % len(cle)])

            # Calcul du nouvel indice en utilisant la méthode de Vigenère
            if mode == 'chiffrement':
                nouvel_indice = (indice_texte + indice_cle) % 26
            else:
                nouvel_indice = (indice_texte - indice_cle) % 26

            # Récupération de la lettre correspondante à l'indice obtenu et ajout à la chaîne de texte chiffré/déchiffré
            lettre_chiffre = chr(nouvel_indice + ord('a'))
            texte_chiffre += lettre_chiffre
        else:
            texte_chiffre += lettre

    return texte_chiffre

# Définition des arguments en ligne de commande
parser = argparse.ArgumentParser(description='Chiffrement/Déchiffrement de Vigenère')
parser.add_argument('-m', '--mode', choices=['chiffrement', 'dechiffrement'], required=True, help='Le mode de l\'opération à effectuer : chiffrement ou déchiffrement')
parser.add_argument('-i', '--input', type=str, required=True, help='Le nom du fichier d\'entrée')
parser.add_argument('-o', '--output', type=str, required=True, help='Le nom du fichier de sortie')
parser.add_argument('-k', '--key', type=str, required=True, help='La clé de chiffrement/déchiffrement')
args = parser.parse_args()

# Chemin d'accès au fichier d'entrée
chemin_entree = os.path.join(args.input)

# Ouverture du fichier d'entrée en mode lecture
with open(chemin_entree, 'r') as fichier_entree:
    texte = fichier_entree.read()

# Chiffrement ou déchiffrement du texte avec la clé
texte_traite = vigenere(texte, args.key, args.mode)

# Écriture du texte chiffré/déchiffré dans le fichier de sortie
with open(args.output, 'w') as fichier_sortie:
    fichier_sortie.write(texte_traite)
