# <--- Partie Thomas --->
# Spécifiez le chemin du fichier
fichiers_chemins = [
    r"C:\Users\thomas\OneDrive\Documents\Bureau\Repositories\Sujet-QCM-Python\Liste de question avec des proposition.txt",
    r"C:\Users\thomas\OneDrive\Documents\Bureau\Repositories\Sujet-QCM-Python\Liste de question avec des proposition2.txt",
    r"C:\Users\thomas\OneDrive\Documents\Bureau\Repositories\Sujet-QCM-Python\Liste de question avec des proposition3.txt",
    r"C:\Users\thomas\OneDrive\Documents\Bureau\Repositories\Sujet-QCM-Python\Liste de question avec des proposition4.txt",
    r"C:\Users\thomas\OneDrive\Documents\Bureau\Repositories\Sujet-QCM-Python\Liste de question avec des proposition5.txt"
]

# Choisir un fichier spécifique (ex: le premier de la liste)
fichier_choisi = fichiers_chemins[0]  # Tu peux changer l'index ici (0 à 4)

# Essayez d'ouvrir le fichier avec l'encodage 'latin-1'
with open(fichier_choisi, 'r', encoding='latin-1') as file:
    contenu = file.read()
    print(contenu)  # Affiche le contenu du fichier pour vérifier