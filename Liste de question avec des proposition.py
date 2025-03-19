import os

# Liste des fichiers de questions
fichiers_chemins = [
    r"C:\Users\thomas\OneDrive\Documents\Bureau\Repositories\Sujet-QCM-Python\Liste de question avec des proposition.txt",
    r"C:\Users\thomas\OneDrive\Documents\Bureau\Repositories\Sujet-QCM-Python\Liste de question avec des proposition2.txt",
    r"C:\Users\thomas\OneDrive\Documents\Bureau\Repositories\Sujet-QCM-Python\Liste de question avec des proposition3.txt",
    r"C:\Users\thomas\OneDrive\Documents\Bureau\Repositories\Sujet-QCM-Python\Liste de question avec des proposition4.txt",
    r"C:\Users\thomas\OneDrive\Documents\Bureau\Repositories\Sujet-QCM-Python\Liste de question avec des proposition5.txt"
]

# Fonction pour afficher les fichiers et choisir celui à utiliser
def choisir_fichier():
    print("\n📂 Liste des fichiers de questions :")
    for i, fichier in enumerate(fichiers_chemins, start=1):
        print(f"{i}. {os.path.basename(fichier)}")

    while True:
        try:
            choix = int(input("\n👉 Entrez le numéro du fichier à utiliser : "))
            if 1 <= choix <= len(fichiers_chemins):
                return fichiers_chemins[choix - 1]
            else:
                print("⚠️ Numéro invalide, veuillez entrer un numéro entre 1 et", len(fichiers_chemins))
        except ValueError:
            print("❌ Entrée invalide, veuillez entrer un chiffre.")

# Fonction pour charger les questions depuis un fichier
def charger_questions(fichier):
    questions = []
    try:
        with open(fichier, 'r', encoding='latin-1') as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                question = lines[i].strip()  # Question
                choix = [lines[i + j].strip() for j in range(1, 5)]  # Les 4 choix
                reponse = lines[i + 5].strip().split(": ")[1]  # Réponse sous forme "Réponse: X"
                questions.append({
                    "question": question,
                    "choix": choix,
                    "reponse": reponse
                })
                i += 6  # Passer à la question suivante
    except Exception as e:
        print(f"⚠️ Erreur lors de la lecture du fichier : {e}")
    return questions

# Fonction pour poser les questions et gérer le score
def poser_question(question_data):
    print("\n" + question_data["question"])
    for option in question_data["choix"]:
        print(option)

    choix = input("Entrez le numéro de votre choix (1-4): ")
    
    if choix == question_data["reponse"]:
        print("✅ Bonne réponse !")
        return True
    elif choix in ["1", "2", "3", "4"]:
        print(f"❌ Mauvaise réponse. La bonne réponse était : {question_data['choix'][int(question_data['reponse'])-1]}.")
        return False
    else:
        print("⚠️ Choix invalide, veuillez entrer un numéro entre 1 et 4.")
        return False

# Fonction principale pour jouer
def jouer():
    while True:
        fichier = choisir_fichier()  # Demander le fichier à utiliser
        questions = charger_questions(fichier)  # Charger les questions
        
        if not questions:
            print("⚠️ Aucun fichier valide trouvé. Veuillez réessayer.")
            continue

        score = 0  # Initialiser le score
        for i, question in enumerate(questions):
            print(f"\n📝 Question {i+1}:")
            if poser_question(question):  # Vérifier la réponse
                score += 1

        # Affichage du score final
        print(f"\n🎯 Score final : {score}/{len(questions)}.")

        # Demander si on veut rejouer
        rejouer = input("\n🔄 Voulez-vous rejouer ? (o/n): ").lower()
        if rejouer != 'o':
            print("👋 Merci d'avoir joué ! À bientôt.")
            break

# Lancer le jeu
jouer()
