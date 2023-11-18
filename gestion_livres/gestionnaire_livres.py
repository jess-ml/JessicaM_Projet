from .livre import Livre

class GestionnaireLivres:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, titre, auteur, genre, isbn):
        nouveau_livre = Livre(titre, auteur, genre, isbn)
        self.livres.append(nouveau_livre)

    def supprimer_livre(self, titre):
        self.livres = [livre for livre in self.livres if livre.titre != titre]

    def modifier_livre(self, ancien_titre, nouveau_titre, auteur, genre, isbn):
        for livre in self.livres:
            if livre.titre == ancien_titre:
                livre.titre = nouveau_titre
                livre.auteur = auteur
                livre.genre = genre
                livre.isbn = isbn
                break

    def rechercher_livres(self, critere, valeur):
        if critere == "titre":
            return [livre for livre in self.livres if valeur.lower() in livre.titre.lower()]
        elif critere == "auteur":
            return [livre for livre in self.livres if valeur.lower() in livre.auteur.lower()]
        elif critere == "isbn":
            return [livre for livre in self.livres if valeur.lower() in livre.isbn.lower()]
        else:
            return []

    def lister_livres(self):
        return [str(livre) for livre in self.livres]

# Ajoute d'autres méthodes si nécessaire
