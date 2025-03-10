# Importer le fichier avec le chemin complet
fichier_chemin = r"C:\Users\thomas\OneDrive\Documents\Bureau\Repositories\Sujet-QCM-Python\Liste de question avec des proposition.txt"

# Utilisez ce chemin pour lire le fichier
with open(fichier_chemin, 'r') as file:
    contenu = file.read()
    print(contenu)  # Affiche le contenu du fichier pour vérification