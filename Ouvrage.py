
import Reference

class Ouvrage(Reference.Reference):

    """ constructeur de la classe ouvrage qui représente un objet ouvrage dans une bibliothèque"""

    # https: // openclassrooms.com / courses / apprenez - a - programmer - en - python / les - proprietes - 9  # /id/r-2233088

    # Tout d'abord, dans le constructeur, on ne crée pas un attributself.lieu_residencemaisself._lieu_residence.
    # Il n'y a qu'un petit caractère de différence, le signe souligné _ placé en tête du nom de l'attribut. Et pourtant, ce signe
    # change beaucoup de choses. La convention veut qu'on n'accède pas, depuis l'extérieur de la classe, à un
    #  attribut commençant par un souligné _. C'est une convention, rien ne vous l'interdit… sauf, encore une
    # fois, le bon sens.
    def __init__(self, c_auteurs, c_editeurs, c_ville, c_titre, c_annee, c_identifiant):

        self._m_editeurs = c_editeurs
        self._m_auteurs = c_auteurs
        self._m_ville = c_ville
        self._m_titre = c_titre
        self._m_annee = c_annee
        self._m_identifiant = c_identifiant

    #On définit une première méthode, commençant elle aussi par un souligné _, nommée_get_lieu_residence.
    # C'est la même règle que pour les attributs : on n'accède pas, depuis l'extérieur de la classe, à une
    # méthode commençant par un souligné _. Si vous avez compris ma petite explication sur les accesseurs et
    #  mutateurs, vous devriez comprendre rapidement à quoi sert cette méthode : elle se contente de renvoyer
    # le lieu de résidence. Là encore, l'attribut manipulé n'est paslieu_residencemais_lieu_residence. Comme on
    # est dans la classe, on a le droit de le manipuler.

    def _reqAuteurs(self):
        return self._m_auteurs

    def _reqTitre(self):
        return self._m_titre

    def _reqIdentifiant(self):
        return self._m_identifiant

    def _reqAnnee(self):
        return self._m_annee

    def _reqVille(self):
        return self._m_ville

    def _reqEditeur(self):
        return self._m_editeurs

    # On va dire à Python que notre attribut lieu_residence pointe vers une
    # propriété

    m_auteurs = property(_reqAuteurs)

    m_titre = property(_reqTitre)

    m_identifiant = property(_reqIdentifiant)

    m_annee = property(_reqAnnee)

    m_ville = property(_reqVille)

    m_editeurs = property(_reqEditeur)

    #   Définition des setters en python en utilisant les méthodes spéciales
    #
    # Cette méthode définit l'accès à un attribut destiné à être modifié. Si vous écrivez objet.nom_attribut = nouvelle_
    # valeur, la méthode spéciale__setattr__sera appelée ainsi :objet.__setattr__("nom_attribut", nouvelle_valeur).
    # Là encore, le nom de l'attribut recherché est passé sous la forme d'une chaîne de caractères.

    # def __setattr__(self, _m_auteurs, value):
    #     object.__setattr__(self, _m_auteurs, value)
    #     self.enregistrer()

    def asgAuteurs(self, p_auteurs):
        """ Méthode qui permet de modifier les auteurs de l’ouvrage en assignant de nouveaux auteurs à l’ouvrage
        courant. Les nouveaux auteurs doit bien entendu être valides tels que décrits plus haut pour les auteurs."""
        self._m_auteurs = p_auteurs


    def reqOuvrageFormate(self):

        """ Méthode qui retourne dans un objet string les informations sur un Ouvrage formatées sous le
        format suivant :
        Homayoon Beigi. Fundamentals of Speaker Recognition. New York : Springer, 2011. 978-0-387-77591-3. """

        return (str(self._m_auteurs) +". "+ str(self._m_titre) +". "+ str(self._m_ville) +": "+ str(self._m_editeurs) +", "+ str(self._m_annee) +". "+ str(self._m_identifiant) +".")


    def validerCodeIsbn (sefl, p_isbn):

        """ Cette méthode a pour but de vérifier si le numéro isbn n'est pas inventé et respecte bien les propriétés d
        d'un numéro isbn avant de le tranmettre à l'attribut m_identifiant"""

        return True

    # surcharge de l'opérateur == qui vérifie si deux objets sont identiques, qui le seront si et seulement si
    # elle partagent les mêmes attributs

    def __eq__(self, other):
        """ surcharge de l'opérateur de comparaison ==, elle retourne un booléen
        opérateurs de comparaison entre deux ouvrages, deux ouvrages sont identiques si et seulement si elles ont tous les attributs
        identiques"""


    # La méthode spéciale__getattr__permet de définir une méthode d'accès à nos attributs plus large que celle
    # que Python propose par défaut. En fait, cette méthode est appelée quand vous tapezobjet.attribut(non pas
    # pour modifier l'attribut mais simplement pour y accéder). Python recherche l'attribut et, s'il ne le trouve
    # pas dans l'objet et si une méthode__getattr__existe, il va l'appeler en lui passant en paramètre le nom
    # de l'attribut recherché, sous la forme d'une chaîne de caractères.

    # def __getattr__(self, m_auteurs):
    #     print("Lecture des auteurs")

    @m_auteurs.setter
    def m_auteurs(self, value):
        self._m_auteurs = value


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

    n_ouvrage = Ouvrage(auteur, editeurs, ville, titre, annee, id)

    print(n_ouvrage.m_auteurs)

    print(n_ouvrage.m_identifiant)

    print(n_ouvrage.m_annee)

    print(n_ouvrage.m_ville)

    print(n_ouvrage.m_editeurs)

    print(n_ouvrage.m_titre)