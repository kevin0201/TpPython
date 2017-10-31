
# On importe notre fichier qui contient la classe Ouvrage
import Ouvrage

if __name__ == '__main__' :

    print("**************** Ce programme va vous permettre de créer un ouvrage *****************")

    print("Entrer les informations pour créer un ouvrage valide dans la biblio")

    auteur = input("Entrer le ou les auteurs ici --> : ")

    editeurs = input("Entrer le ou les éditeurs ici --> : ")

    ville = input("Entrer la ville d'édition ici --> : ")

    titre = input("Entrer le titre de l'ouvrage ici --> : ")

    annee = input("Entrer l'année de parution ici --> : ")

    id = input("Entrer l'identifiant isbn ou issn ici -->: ")

    # Création du nouvel ouvrage :
    # Dans le fichier Ouvrage on a la classe Ouvrage, pour acceder à la classe on fait Fichier.Classe
    # Donc on fait Ouvrage(fichier).Ouvrage(Class) pour accéder à la classe ouvrage contenue dans le fichier ouvrage
    # Sachant aussi qu'il faut importer le fichier afin de pouvoir avoir accès à toutes ses classes et fonctions
    # qui y sont écrites.

    n_ouvrage = Ouvrage.Ouvrage(auteur, editeurs, ville, titre, annee, id)

    print(n_ouvrage.m_auteurs)
    print(n_ouvrage.m_identifiant)
    print(n_ouvrage.m_annee)
    print(n_ouvrage.m_ville)
    print(n_ouvrage.m_editeurs)
    print(n_ouvrage.m_titre)