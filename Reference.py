
class Reference:

    def __init__(self, auteurs, titre, annee, identifiant):

        # Rappel on n'accede pas au attributs commençant par "_" en dehors de la classe sans pas passer par des getters ou les accesseurs
        # lorsque l'on défini le nom de l'attribut en commençan par "_" il faut lui faire un getter qui permettra d'y acceder par objet.attribut

        self._m_auteurs = auteurs
        self._m_titre = titre
        self._m_anneeEdition = annee
        self._m_identifiant = identifiant

    # les getters des attributs de la classe

    def _reqAuteurs(self):
        return self._m_auteurs

    def _reqTitre(self):
        return self._m_titre

    def _reqIdentifiant(self):
        return self._m_identifiant

    def _reqAnnee(self):
        return self._m_anneeEdition

    # on défini les gettes et les setters (ainsi que les deleter et les helper) de chaque attribut via les propriétés et la fonction property

    # property() permet de définir les getters, les setteurs, des deleteurs et les helpers d'un attribut

     # Vu que j'accede à l'attribut à partir de la classe où il est défini je peux ne pas mettre le "_" qui le précède
    # c'est y accéder en dehors de la classe qui n'est pas conseillé

    m_auteur = property(_reqAuteurs)

    m_titre = property(_reqTitre)

    m_identifiant = property(_reqIdentifiant)

    m_anneeEdition =  property(_reqAnnee)

    def __eq__(self, other):
        """ Surchage de l'opération de comparaison == qui compare si deux objets sont identiques,
        deux objets seront identiques si et seulement si les deux  on tous les attributs qui sont identiques"""

        if self._m_anneeEdition==other._m_anneeEdition and self._m_identifiant == other._m_identifiant and self._m_titre == other._m_titre and self._m_auteurs ==  other._m_auteurs :
            return True
        else : return False

