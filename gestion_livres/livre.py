class Livre:
    def __init__(self, titre, auteur, genre, isbn):
        self.titre = titre
        self.auteur = auteur
        self.genre = genre
        self.isbn = isbn

    def __str__(self):
        return f"{self.titre} - {self.auteur} - {self.genre} - {self.isbn}"
