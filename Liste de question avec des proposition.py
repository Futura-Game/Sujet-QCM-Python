# Spécifiez le chemin du fichier
fichier_chemin = r"C:\Users\turbo\Desktop\repositories\Sujet-QCM-Python\Liste de question avec des proposition.txt"

# Essayez d'ouvrir le fichier avec l'encodage 'latin-1'
with open(fichier_chemin, 'r', encoding='latin-1') as file:
    contenu = file.read()
    print(contenu)  # Affiche le contenu du fichier pour vérifier
