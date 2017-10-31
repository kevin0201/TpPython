
import Reference

class Journal(Reference.Reference):

    @property
    def m_volume(self):
        return self._m_volume

    def __init__(self, auteurs, titre, annee, identifiant, nom, volume, numero, page):

        Reference.__init__(auteurs, titre, annee, identifiant) # Journal hérite de Reference donc, ici on initialise les attributs de Reference qui est la classe mère
        #Après initialisation des attributs de la classe mère qui ont été hérité on initialise les attributs propres de la classe fille
        self._m_nom = nom # nom du journal, ce n'est pas le nom de l'auteur du journal
        self._m_volume = volume
        self._m_numero = numero
        self._m_page = page


    # Accesseurs pour tous les attributs


    def _reqNom(self):
        return self._m_nom


    def _reqVolume(self):
        return self._m_numero


    def _reqPage(self):
        return  self._m_page


    def _reqNumero(self):
        return self._m_numero


    # Définition des property pour accès aux attributs


    m_nom = property(_reqNom)


    m_volume =  property(_reqVolume())


    m_numero = property(_reqNumero)


    m_page = property(_reqPage)


    def reqReferenceFormate(self):
        return (str(self.m_auteurs) + str(self.m_titre)+ str(self.m_nom)+(self.m_volume)+(self.m_numero)+(self.m_page)+(self.m_anneeEdition)+self.m_identifiant)

    # Ici on essaie de faire une copie de l'objet pour le stocker dans un autre objet,
    # A vérifier si c'est fonctionnel

    def clone(self):
         return self
